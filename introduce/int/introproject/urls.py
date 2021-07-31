from django.contrib import admin
from django.urls import path, include
import intro.views
import portfolio.views
import hobby.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', intro.views.home, name = "home"),
    path('intro/', include('intro.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('hobby/', hobby.views.hobby, name="hobby"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
