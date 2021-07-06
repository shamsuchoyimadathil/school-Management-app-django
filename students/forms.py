from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit , Layout ,Row ,Column
from crispy_forms.bootstrap import FormActions


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
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout( 
            Row(
                Column('first_name'),
                Column('last_name'),

            ),
            Column(
                'DOB',
                'gender'
            ),
            Row(
                Column('address_line_1'),
                Column('address_line_2')
            ),
            Column(
                'city',
                'zipcode'
            ),

            FormActions(
                Submit('add_student','Save Info', css_class="btn btn-primary col text-center")
            ) 
        )

