from rest_framework import viewsets, permissions, filters
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all().order_by('-created_at')
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  serializer_class = PostSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  
  # You can filter by author or title
  filterset_fields = ['author', 'title']
  search_fields = ['title', 'content']
  ordering_fields = ['created_at', 'title']
    
  
  def perform_create(self, serializer):
     # Automatically assign the logged-in user as the author
    serializer.save(author=self.request.user)
    
class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all().order_by('-created_at')
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  serializer_class = CommentSerializer
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['author', 'post']
  search_fields = ['content']
  
  def perform_create(self, serializer):
     # Automatically assign the logged-in user as the author
    serializer.save(author=self.request.user)