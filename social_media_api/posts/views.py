from rest_framework import viewsets, permissions, filters, generics, status
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

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

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get all the users this user is following
        following_users = user.following.all()
        # Get posts only from those followed users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
      


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response({'message': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # create notification
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )

        return Response({'message': 'Post liked!'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if like:
            like.delete()
            return Response({'message': 'Post unliked!'}, status=status.HTTP_200_OK)

        return Response({'message': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

