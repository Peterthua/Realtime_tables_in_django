from django.contrib import admin
from .models import Profile, Post


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'birth_date', 'location', 'bio', 'receive_email_notifications',
                    'language_preference')
    list_filter = ('first_name', 'last_name', 'email', 'birth_date', 'location', 'bio', 'receive_email_notifications',
                   'language_preference')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('title', 'author', 'status', 'created_at')
