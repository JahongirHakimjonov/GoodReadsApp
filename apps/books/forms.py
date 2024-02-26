from django.forms import ModelForm, IntegerField, Widget, Textarea
from apps.books.models import BookReview, BookAuthor, Book


# class Textarea(Widget):
#     template_name = "django/forms/widgets/textarea.html"
#
#     def __init__(self, attrs=None):
#         # Use slightly better defaults than HTML's 20x2 box
#         default_attrs = {"cols": "10", "rows": "3"}
#         if attrs:
#             default_attrs.update(attrs)
#         super().__init__(default_attrs)


class AddBookReviewForm(ModelForm):
    rating = IntegerField(min_value=1, max_value=5)
    body = Textarea(attrs={"rows": "3"})

    class Meta:
        model = BookReview
        fields = ("body", "rating")


class AddAuthorForm(ModelForm):
    class Meta:
        model = BookAuthor
        fields = ['first_name', 'last_name', 'birthdate', 'website', 'avatar', 'about', 'email']


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'slug', 'description', 'published_date', 'ISBN', 'language', 'page_count', 'cover_image',
                  'genre', 'authors']
