from django import forms
from .models import student_registration

class RegistrationForm(forms.ModelForm):
    class Meta :
        model = student_registration
        fields = '__all__'

        labels = {
            'student_name' : 'Name',
            'student_class' : 'Class',
            'student_roll_no' : 'Roll Number'
        }