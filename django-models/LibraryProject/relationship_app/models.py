from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Other models (Author, Book, Library, Librarian)
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

# UserProfile Model
class UserProfile(models.Model):
    """
    Extends the Django User model to include a role field.
    """
    ROLE_CHOICES = (
        ('Admin', 'Admin'),       # Role for administrators
        ('Librarian', 'Librarian'), # Role for librarians
        ('Member', 'Member'),     # Role for members
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with User
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')  # Role field
    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()