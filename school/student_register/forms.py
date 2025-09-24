from django import forms
from .models import student_registration

# this is the Form 
class RegistrationForm(forms.ModelForm):
    class Meta :
        model = student_registration # We are linking the form with the model
        fields = '__all__' # This means we need all the columns for the form 

        # The labels is used to change the name of the column when it comes to the forms 
        labels = {
            'student_name' : 'Name',
            'student_class' : 'Class',
            'student_roll_no' : 'Roll Number'
        }