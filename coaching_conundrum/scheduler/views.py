from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SlotForm
from .models import Slot
from django.core.exceptions import ValidationError
from django.utils import timezone
from .forms import CallFeedbackForm
from django.core.exceptions import PermissionDenied

def home(request):
    return render(request, 'scheduler/home.html')

@login_required
def add_slot(request):
    if request.method == 'POST':
        form = SlotForm(request.POST)
        if form.is_valid():
            slot = form.save(commit=False)  # Create a slot instance, but don't save it yet
            slot.coach = request.user  # Assign the logged-in user as the coach
            print(f"Coach assigned: {slot.coach}")  # Print for debugging

            try:
                slot.check_for_overlap()  # Check if the slot overlaps
                slot.save()  # Save the slot
                return redirect('coach_slots')  # Redirect to coach slots view
            except ValidationError as e:
                form.add_error(None, e.message)  # Add validation error to the form
    else:
        form = SlotForm()

    return render(request, 'scheduler/add_slot.html', {'form': form})

@login_required
def coach_slots(request):
    # Restrict access to coaches only
    if not hasattr(request.user, 'coachprofile'):
        raise PermissionDenied
    
    # Get the logged-in user's upcoming slots
    upcoming_slots = Slot.objects.filter(coach=request.user, start_time__gte=timezone.now()).order_by('start_time')
    
    # Get past slots where start_time is in the past
    past_slots = Slot.objects.filter(coach=request.user, start_time__lt=timezone.now()).order_by('-start_time')
    
    return render(request, 'scheduler/coach_slots.html', {
        'upcoming_slots': upcoming_slots,
        'past_slots': past_slots,
    })


@login_required
def available_slots(request):
    # Restrict access to students only
    if not hasattr(request.user, 'studentprofile'):
        raise PermissionDenied
    
    # Fetch available slots that are upcoming
    upcoming_slots = Slot.objects.filter(student__isnull=True, start_time__gte=timezone.now()).order_by('start_time')
    
    # Fetch past slots that were not booked
    past_slots = Slot.objects.filter(student__isnull=True, start_time__lt=timezone.now()).order_by('-start_time')
    
    return render(request, 'scheduler/available_slots.html', {
        'upcoming_slots': upcoming_slots,
        'past_slots': past_slots,
    })

@login_required
def book_slot(request, slot_id):
    # Fetch the specific slot
    slot = get_object_or_404(Slot, id=slot_id)

    # Ensure the slot is still available
    if slot.student is not None:
        return redirect('available_slots')  # Slot is already booked, redirect back to available slots

    # Book the slot by assigning the current user as the student
    slot.student = request.user
    slot.save()

    # Redirect to a page that shows booked slots or a success message
    return redirect('available_slots')

@login_required
def booked_slots(request):
    # Restrict access to students only
    if not hasattr(request.user, 'studentprofile'):
        raise PermissionDenied
    
    # Show slots booked by the current user (student)
    slots = Slot.objects.filter(student=request.user).order_by('start_time')
    return render(request, 'scheduler/booked_slots.html', {'slots': slots})

@login_required
def past_calls(request):
    # Restrict access to coaches only
    if not hasattr(request.user, 'coachprofile'):
        raise PermissionDenied
    
    # Get the logged-in user's completed slots if they are a coach
    past_slots = Slot.objects.filter(coach=request.user, end_time__lt=timezone.now(), student__isnull=False).order_by('-start_time')
    return render(request, 'scheduler/past_calls.html', {'past_slots': past_slots})

@login_required
def add_feedback(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id, coach=request.user, end_time__lt=timezone.now())

    if request.method == 'POST':
        form = CallFeedbackForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            return redirect('past_calls')
    else:
        form = CallFeedbackForm(instance=slot)

    return render(request, 'scheduler/add_feedback.html', {'form': form, 'slot': slot})

@login_required
def feedback_detail(request, slot_id):
    # Get the slot for the given slot_id, ensuring it belongs to the current coach
    slot = get_object_or_404(Slot, id=slot_id, coach=request.user)

    # Render the details, including satisfaction and notes
    return render(request, 'scheduler/feedback_detail.html', {'slot': slot})

def custom_permission_denied_view(request, exception=None):
    return render(request, 'scheduler/403.html', status=403)
