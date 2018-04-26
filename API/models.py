from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100,default='')
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return str(self.name)