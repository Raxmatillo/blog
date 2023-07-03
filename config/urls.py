from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from api import views


from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs/', include('api.urls')),


    path('admin/', admin.site.urls),
    path('froala_editor/', include('froala_editor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # re_path(r'^', include('blogs.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)