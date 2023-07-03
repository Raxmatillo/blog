from django.urls import path

from .views import BlogViewSet, CategoryViewSet


urlpatterns = [
    path('detail/<slug:slug>/', BlogViewSet.as_view({'get': 'detail_view'}), name='your-model-detail-view'),
]