from django.db import models

# Create your models here.
class student_registration(models.Model):
    student_name = models.CharField(max_length=250)
    student_class = models.CharField(max_length=15)
    student_roll_no = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.student_name
    