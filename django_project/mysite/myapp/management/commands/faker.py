from django.core.management.base import BaseCommand
from myapp.models import Category, Product
from faker import Faker
import random
import requests
from django.core.files.base import ContentFile
import uuid

class Command(BaseCommand):
    help = 'Populate database with fake Categories and products...'

    def handle(self, *args, **kwargs):
        faker = Faker()

        categories = []
        category = Category.objects.all()
        for category_ in category:
            categories.append(category_)

        for _ in range(20):
            product_name = faker.word().capitalize() + " " + faker.word().capitalize()
            price = random.randint(10, 1000)
            description = faker.sentence(nb_words=10)
            category = random.choice(categories)

            product = Product.objects.create(
                name=product_name,
                price=price,
                description=description,
                category=category
            )
            
            image_url = f'https://picsum.photos/seed/{uuid.uuid4()}/200/300'
            response = requests.get(image_url)
            product.image.save(f'{uuid.uuid4()}.jpg', ContentFile(response.content))

            product.save()
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}, Category: {product.category.name}'))
