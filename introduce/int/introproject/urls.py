from django.contrib import admin
from django.urls import path
import intro.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', intro.views.home, name = "home"),
]
