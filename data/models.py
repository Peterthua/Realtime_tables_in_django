from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    # Basic information
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254)  # Consider making this unique

    # Optional fields
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    # Preferences or settings (optional)
    receive_email_notifications = models.BooleanField(default=True)
    language_preference = models.CharField(max_length=10, choices=[
        ('en', 'English'),
        ('es', 'Spanish'),
        ('sw', 'Swahili'),
        ('fr', 'French')
        # Add more language choices as needed
    ])

    def __str__(self):
        return f"Profile for {self.first_name} {self.last_name}"


STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('archive', 'Archive')
)


class Post(models.Model):
    title = models.CharField(max_length=50, unique_for_date='created_at')
    content = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS, default='draft')

    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', 'id']
