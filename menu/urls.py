from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="base"),
    path("cars/", TemplateView.as_view(template_name="cars.html"), name="cars"),
    path(
        "mercedes/",
        TemplateView.as_view(template_name="mercedes.html"),
        name="mercedes",
    ),
    path("toyota/", TemplateView.as_view(template_name="toyota.html"), name="toyota"),
    path("300/", TemplateView.as_view(template_name="300.html"), name="300"),
    path("prado/", TemplateView.as_view(template_name="prado.html"), name="prado"),
]
