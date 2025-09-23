from django.contrib import admin
from .models import student_registration
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('student_name','student_class','student_roll_no')

admin.site.register(student_registration,RegisterAdmin)