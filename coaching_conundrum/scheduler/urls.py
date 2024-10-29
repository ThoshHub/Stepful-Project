from django.urls import path
from . import views
from django.conf.urls import handler403

urlpatterns = [
    path('add-slot/', views.add_slot, name='add_slot'),
    path('coach-slots/', views.coach_slots, name='coach_slots'),
    path('available-slots/', views.available_slots, name='available_slots'),
    path('book-slot/<int:slot_id>/', views.book_slot, name='book_slot'),

    path('booked-slots/', views.booked_slots, name='booked_slots'),
    path('past-calls/', views.past_calls, name='past_calls'),
    path('add-feedback/<int:slot_id>/', views.add_feedback, name='add_feedback'),
    path('feedback/<int:slot_id>/', views.feedback_detail, name='feedback_detail'),
]

# Global handler for 403 errors
handler403 = 'scheduler.views.custom_permission_denied_view'