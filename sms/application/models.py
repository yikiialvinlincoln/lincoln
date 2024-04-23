from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    age = models.IntegerField()
    gender = models.CharField(max_length=255)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_desc = models.Text()
    course_duration = models.Integerfield()
    course_price = models.FloatField()
    start_date = models.Datefield()

class EnrolledStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True) 
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()       
