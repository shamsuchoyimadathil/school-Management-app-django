from django import forms
from django.db.models.base import Model 
from .models import Student

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        exclude = ("slug", )
        labels = {
           "DOB":"Date Of Birth" 
        }
        widgets = {
            "DOB":DateInput()
            #"Date_of_birth":DateInput(attrs={'type':'date'})
        }
        error_message ={
            "first_name":{
                "required":"must not be empty",
                "max_length":"must be shorter name"
            },
            "last_name":{
                "required":"must not be empty",
                "max_length":"must be shorter name"
            }
        }
