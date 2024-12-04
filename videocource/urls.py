
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminbegi/', admin.site.urls),
    path('', include("front.urls")),
    path('adminka/', include("adminka.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('user/', include('authenticated.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)