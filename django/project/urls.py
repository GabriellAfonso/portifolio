from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from url_shortener.views import redirect_view

urlpatterns = [
    path('', include('portifolio.urls')),
    path('webchat/', include('webchat.urls')),
    path('shortener/', include('url_shortener.urls')),
    path('picpay/', include('picpay.urls')),
    path('igreja/', include('igreja.urls')),
    path('admin/', admin.site.urls),
    path('s/<str:short_url>/', redirect_view, name='redirect_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
