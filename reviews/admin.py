from django.contrib import admin
from . models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}
    list_display = ["name","rating"]

admin.site.register(Review,ReviewAdmin) 
