from django.contrib import admin
from .models import Student , Gender

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("first_name","last_name",),}  
    list_display = ["full_name","DOB"]
    list_filter = ["gender"] 


admin.site.register(Student,StudentAdmin)
admin.site.register(Gender)


