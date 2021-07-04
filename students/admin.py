from django.contrib import admin
from .models import Student , Address , Gender

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("first_name","last_name",),}  
    #prepopulated_fields = {"slug":("full_name()",),}  
    #list_display = ["first_name","DOB"]
    list_display = ["full_name","DOB"]
    list_filter = ["gender"] 


admin.site.register(Student,StudentAdmin)
admin.site.register(Address)
admin.site.register(Gender)


