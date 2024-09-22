from django.db import models


# Create your models here.
class Contact(models.Model):
    contact_Name = models.CharField(max_length=50)
    contact_Email = models.EmailField(max_length=254)
    contact_Date = models.DateField()
    contact_Message = models.TextField(max_length=800)
    timestamp_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    department_ID = models.CharField(max_length=20, unique=True, primary_key=True)
    department_Name = models.CharField(max_length=50)
    department_Floor = models.CharField(max_length=50)
    department_Dean = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    program_ID = models.CharField(max_length=20, unique=True, primary_key=True)
    program_Name = models.CharField(max_length=50)
    degree_Type = models.CharField(max_length=50)
    department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_ID = models.CharField(max_length=20, unique=True, primary_key=True)
    student_FirstName = models.CharField(max_length=50)
    student_LastName = models.CharField(max_length=50)
    student_GPA = models.DecimalField(max_digits=3, decimal_places=2)
    student_Age = models.IntegerField()
    student_ProgramID = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
