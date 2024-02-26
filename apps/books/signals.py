from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from apps.books.models import BookReview


@receiver(post_save, sender=BookReview)
def send_email_to_author(sender, instance, created, **kwargs):
    if created:
        author = instance.book.author

        send_mail(
            'New review for your book',
            f'{instance.user.username} has left a new review for your book: {instance.body}. Rating: {instance.rating}',
            'hakimjonovjahongir0@gmail.com',
            [author.email],
            fail_silently=False,
        )
