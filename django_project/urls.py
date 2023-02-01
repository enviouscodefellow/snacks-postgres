from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from pages.views import SnackViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api', SnackViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
