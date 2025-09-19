from django.urls import include, path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books_all',
                BookViewSet,
                basename='book_all')

urlpatterns = [
    # Maps to the BookList view
    path('books/', BookList.as_view(), name='book-list'),
    # This includes all routes registered with the router
    path('', include(router.urls))
]
