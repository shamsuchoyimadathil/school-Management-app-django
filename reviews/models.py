from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=50, default="")
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    recommended = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)