# Generated by Django 4.2.13 on 2024-07-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("address", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=20)),
                ("phone_no", models.IntegerField()),
            ],
        ),
    ]
