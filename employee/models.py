from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique= True)
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add= True)
    modified_at = models.DateTimeField(auto_now= True)
    photo = models.ImageField(upload_to='media')
                                        
    def __str__(self):
        return self.first_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

