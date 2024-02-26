from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from apps.books.forms import AddAuthorForm, AddBookForm

from apps.books.forms import AddBookReviewForm
from apps.books.models import Book, BookReview, BookAuthor
from apps.users.models import User


class BookListView(ListView):
    model = Book
    template_name = 'books/book-list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('title')  # Order by the 'title' field.
        return queryset


class BookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        form = AddBookReviewForm()
        context = {
            "book": book,
            "form": form
        }
        return render(request, "books/book-detail.html", context=context)


class AddReviewView(View):
    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        user = User.objects.get(username=request.user.username)
        form = AddBookReviewForm(request.POST)
        if form.is_valid():
            BookReview.objects.create(
                user=user,
                book=book,
                body=form.cleaned_data.get("body"),
                rating=form.cleaned_data.get("rating")
            )
            return redirect(reverse("books:book-detail", kwargs={"slug": book.slug}))
        else:
            context = {
                "book": book,
                "form": form
            }
            return render(request, "books/book-detail.html", context=context)


class UpdateReviewView(View):
    def get(self, request, pk):
        review = get_object_or_404(BookReview, id=pk)
        form = AddBookReviewForm(instance=review)
        return render(request, "books/update-review.html", {"form": form, "review": review})

    def post(self, request, pk):
        review = get_object_or_404(BookReview, id=pk)
        form = AddBookReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(reverse("books:book-detail", kwargs={"slug": review.book.slug}))
        else:
            return render(request, "books/update-review.html", {"form": form, "review": review})


class DeleteReviewView(View):
    def get(self, request, pk):
        review = get_object_or_404(BookReview, id=pk)
        book_slug = review.book.slug
        review.delete()
        return redirect(reverse("books:book-detail", kwargs={"slug": book_slug}))


class AddAuthorView(View):
    def get(self, request):
        form = AddAuthorForm()
        return render(request, "books/add-author.html", {"form": form})

    def post(self, request):
        form = AddAuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            return redirect(reverse("books:author-detail", kwargs={"pk": author.pk}))
        else:
            return render(request, "books/add-author.html", {"form": form})


class AddBookView(View):
    def get(self, request):
        form = AddBookForm()
        return render(request, "books/add-book.html", {"form": form})

    def post(self, request):
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:book-list')
        else:
            return render(request, "books/add-book.html", {"form": form})


class AuthorDetailView(View):
    def get(self, request, pk):
        author = get_object_or_404(BookAuthor, id=pk)
        return render(request, "books/author-detail.html", {"author": author})


class GenreView(View):
    paginate_by = 10

    def get(self, request, pk):
        books = Book.objects.filter(genre=pk)
        return render(request, "books/genre-page.html", {"books": books})
