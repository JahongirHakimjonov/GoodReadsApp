from django.urls import path

from apps.books.views import (
    BookListView,
    BookDetailView,
    AddReviewView,
    UpdateReviewView,
    AddAuthorView,
    AddBookView,
    DeleteReviewView,
    AuthorDetailView,
    GenreView
)

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('review/add/<int:pk>', AddReviewView.as_view(), name="add-review"),
    path('delete-review/<int:pk>/', DeleteReviewView.as_view(), name='delete-review'),
    path('review/update/<int:pk>', UpdateReviewView.as_view(), name="update-review"),
    path('author/add/', AddAuthorView.as_view(), name="add-author"),
    path('book/add/', AddBookView.as_view(), name="add-book"),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('books/genre/<int:pk>/', GenreView.as_view(), name='genre-page')
]
