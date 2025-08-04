from django import forms
from .models import Reservation

# أيام الأسبوع كخيارات:
WEEKDAYS = [
    ('', 'Select a day'),  # قيمة فارغة للاختيار الاختياري
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

class ReservationForm(forms.ModelForm):
    time = forms.ChoiceField(choices=WEEKDAYS, required=False, widget=forms.Select(
        attrs={
            'class': 'custom-select bg-transparent border-primary px-4',
            'style': 'height: 49px;',
        }
    ))

    class Meta:
        model = Reservation
        fields = ['full_name', 'phone', 'email', 'time', 'persons', 'seating', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Full Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Phone Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Email (optional)'
            }),
            # تم استبداله أعلاه
            # 'time': forms.TextInput(...),
            'persons': forms.NumberInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Number of Persons',
                'min': 1,
                'max': 20
            }),
            'seating': forms.Select(attrs={
                'class': 'custom-select bg-transparent border-primary px-4',
                'style': 'height: 49px;'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Additional Notes (e.g. birthday, child, etc.)',
                'rows': 3
            }),
        }