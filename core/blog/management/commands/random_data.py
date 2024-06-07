from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from ...models import Post, Category
from random import choice

category_exaples = (
    "Cloth",
    "Fun",
    "Electronic",
)


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email=self.faker.email(),
            username=self.faker.first_name(),
            password="dummydummy",
        )
        profile = Profile.objects.get(user=user)
        profile.bio = self.faker.paragraph(nb_sentences=3)
        profile.save()

        for name in category_exaples:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author=profile,
                title=self.faker.paragraph(nb_sentences=1),
                content=self.faker.paragraph(nb_sentences=5),
                category=Category.objects.get(name=choice(category_exaples)),
            )
