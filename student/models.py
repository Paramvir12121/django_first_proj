from django.db import models

# Create your models here.

class Student(models.Model):
    #host =
    #topic = 
    name= models.CharField(max_length=200)
    student_no = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    #participants =
    update = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_no, self.name