from django import forms
from django.forms import fields, models 
from . models import Review 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ("slug",)
        #fields = "__all__"
        labels = {
            "name":"Your Name:",
            "text":"Your Comment:",
            "rating":"Your Rating:",
            "recommended":"Would You Recommended To Others ?"
        } 
        error_message = {
            "name":{
                "required":"Your name must not be empty",
                "min_length":"please enter minimum 5 letters"
            }

        }       