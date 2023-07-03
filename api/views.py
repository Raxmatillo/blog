from rest_framework import viewsets, permissions
from rest_framework.response import Response

from blogs.models import Blog, Category

from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .serializers import CategorySerializer, BlogSerializer



class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    lookup_field = 'slug'
    
    @action(detail=True, methods=['get'])
    def detail_view(self, request, slug=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]