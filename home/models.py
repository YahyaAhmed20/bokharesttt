from django.db import models

SEATING_CHOICES = [
    ('indoor', 'Indoor'),
    ('outdoor', 'Outdoor'),
]

class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    time = models.CharField(max_length=50)
    persons = models.PositiveIntegerField()
    seating = models.CharField(max_length=10, choices=SEATING_CHOICES)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.time}"
