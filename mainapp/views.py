from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomepageView(TemplateView):
    """Main Index Page View"""

    template_name = "main_site/index.html"


class AboutpageView(TemplateView):
    """About Page View"""

    template_name = "main_site/about.html"


class ServicespageView(TemplateView):
    """Services Page View"""

    template_name = "main_site/services.html"


class ContactpageView(TemplateView):
    """Contact Page View"""

    template_name = "main_site/contact.html"
