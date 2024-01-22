from django.core.management.base import BaseCommand
from ...models import Profile
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Populate the profile table with fake data'

    def handle(self, *args, **kwargs):
        for _ in range(5):
            profile_data = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'birth_date': fake.date_of_birth(),
                'location': fake.city(),
                'bio': fake.paragraph(nb_sentences=3),
                'receive_email_notifications': fake.boolean(),
                'language_preference': fake.language_code()
            }
            Profile.objects.create(**profile_data)
        self.stdout.write(self.style.SUCCESS('Successfully populated the profile table'))
