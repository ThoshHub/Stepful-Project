from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Slot(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='slots')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='booked_slots')
    satisfaction = models.IntegerField(null=True, blank=True)  # Satisfaction rating (1-5)
    notes = models.TextField(null=True, blank=True)  # Free-form notes for the call

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + timedelta(hours=2)
        super(Slot, self).save(*args, **kwargs)

    def check_for_overlap(self):
        # Logic for checking overlap
        if not self.end_time:
            self.end_time = self.start_time + timedelta(hours=2)
        
        overlapping_slots = Slot.objects.filter(
            coach=self.coach,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )
        if overlapping_slots.exists():
            raise ValidationError("This slot overlaps with an existing slot.")

    def __str__(self):
        return f"{self.coach.username} | {self.start_time} - {self.end_time}"