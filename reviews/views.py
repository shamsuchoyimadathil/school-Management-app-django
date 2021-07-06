from django import views
from django.conf.urls import url
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic import ListView , DetailView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from . forms import ReviewForm
from . models import Review

# Create your views here.

class Reviews(LoginRequiredMixin,ListView):
    template_name = "reviews/reviews.html"
    model = Review 
    context_object_name = "reviews"
    ordering = ['-id']


class AddReviews(LoginRequiredMixin,View):
    def get(self,request):
        form = ReviewForm 
        return render(request,"add_reviews/add-reviews.html",{
            "form":form
        })

    def post(self,request):
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/review-sec")

        return render(request,"add_reviews/add-reviews.html",{
            "form":form
        })
    

class DetailReview(LoginRequiredMixin,DetailView):
    template_name = "add_reviews/detail-review.html"
    model = Review
    context_object_name = "detail__review"