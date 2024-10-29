from django import forms
from .models import Slot

class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['start_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CallFeedbackForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['satisfaction', 'notes']
        widgets = {
            'satisfaction': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }