from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify

# Create your models here.

class Gender(models.Model):
    gender = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.gender}"


class Student(models.Model):
    first_name = models.CharField( default="", max_length=50)
    last_name = models.CharField(max_length=50)
    DOB = models.DateField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    address_line_1 = models.CharField(default="", null=True, blank=True, max_length=150)
    address_line_2 = models.CharField(default="", null=True, blank=True, max_length=150)
    city = models.CharField(max_length=30)
    zipcode = models.CharField( max_length=10)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)

    @property
    def  full_name(self):
        return f"{self.first_name} {self.last_name}" 

    @property
    def full_address(self):
        return f"{self.address_line_1} , {self.address_line_2}"


    def save(self,*args, **kwargs):
        self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
