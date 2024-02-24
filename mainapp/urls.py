from django.urls import path, include
from mainapp.views import HomepageView, AboutpageView, ServicespageView, ContactpageView

app_name = "mainapp"

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("about", AboutpageView.as_view(), name="aboutpage"),
    path("service", ServicespageView.as_view(), name="servicepage"),
    path("contact", ContactpageView.as_view(), name="contactpage"),
]
