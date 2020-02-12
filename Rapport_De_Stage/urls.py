from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Restaurant Administration"
admin.site.site_title = "Modern Restaurant"
admin.site.index_title = "Welcome to Modern Restaurant"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')),
    path('manager/', include('apps.manager.urls')),
    path('client/', include('apps.table.urls')),
    path('service/', include('apps.service.urls')),
    path('commercial/', include('apps.commercial.urls')),
    path('cuisine/', include('apps.cuisine.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)