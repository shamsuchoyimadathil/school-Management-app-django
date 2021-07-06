from django.views.generic.base import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPage(LoginRequiredMixin,TemplateView):
    template_name = "main_page/main-page.html" 

