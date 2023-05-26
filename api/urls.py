from django.urls import include, path
from rest_framework import routers
from .views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'your-model', BlogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]