from django import forms
from django.core.exceptions import ValidationError

from .models import Course

class AddBasketForm(forms.Form):
    course_id = forms.IntegerField()

    def clean_course(self):
        course_id = self.cleaned_data['course_id']
        if not Course.objects.filter(id=course_id).exists():
            raise ValidationError('Такого курса не существует')
            


