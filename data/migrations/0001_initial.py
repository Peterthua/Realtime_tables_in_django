# Generated by Django 5.0.1 on 2024-01-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('receive_email_notifications', models.BooleanField(default=True)),
                ('language_preference', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('sw', 'Swahili'), ('fr', 'French')], max_length=10)),
            ],
        ),
    ]
