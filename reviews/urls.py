from django.urls import path 

from . import views


urlpatterns = [
    path("",views.Reviews.as_view(),name="reviews"),
    path("add-reviews",views.AddReviews.as_view(),name="add-review"),
    path("detail-review/<slug:slug>/",views.DetailReview.as_view(),name="detail")
    
]

