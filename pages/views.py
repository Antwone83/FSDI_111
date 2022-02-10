from re import template
from django.views.generic import TemplateView

# OOP --> Object Oriented Programming
class HomePageView(TemplateView):
    template_name = "index.html"
# Create your views here.
class AboutPageView(TemplateView):
    template_name = "about.html"