# Generated by Django 4.2.13 on 2024-07-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("serializer_type", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Score",
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
                ("palyer_name", models.CharField(max_length=100)),
                ("score", models.IntegerField()),
            ],
        ),
    ]
