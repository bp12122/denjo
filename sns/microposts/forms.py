from django import forms
from .models import Hope
from django.utils import timezone

class HopeCreateForm(forms.ModelForm):
   class Meta:
       model = Hope
       fields = (
        'number_of_people',
        'price',
        'place',
        'date_and_time',
        'memo',
       )
       widgets = {
        'number_of_people': forms.Textarea(
            attrs={'rows': 1, 'cols': 3,
                   'placeholder': '人数'}
        ),
        'price': forms.Textarea(
            attrs={'rows': 1, 'cols': 5,
                   'placeholder': '金額/人'}
        ),
        'place': forms.Textarea(
            attrs={'rows': 1, 'cols': 10,
                   'placeholder': '場所'}
        ),
        'date_and_time': forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        'memo': forms.Textarea(
            attrs={'rows': 3, 'cols': 30,
                   'placeholder': '備考'}
        ),
       }

class HopeUpdateForm(forms.ModelForm):
   class Meta:
       model = Hope
       fields = (
        'number_of_people',
        'price',
        'place',
        'date_and_time',
        'memo',
       )
       widgets = {
        'number_of_people': forms.Textarea(
            attrs={'rows': 1, 'cols': 3}
        ),
        'price': forms.Textarea(
            attrs={'rows': 1, 'cols': 5}
        ),
        'place': forms.Textarea(
            attrs={'rows': 1, 'cols': 10}
        ),
        'date_and_time': forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        'memo': forms.Textarea(
            attrs={'rows': 3, 'cols': 30}
        ),
       }