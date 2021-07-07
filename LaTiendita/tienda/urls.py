from django.urls import path
from django.conf.urls import include
from tienda import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path("/", views.index ),

]