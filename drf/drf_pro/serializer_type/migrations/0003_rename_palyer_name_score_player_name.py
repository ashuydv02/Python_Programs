# Generated by Django 4.2.13 on 2024-07-16 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("serializer_type", "0002_score"),
    ]

    operations = [
        migrations.RenameField(
            model_name="score",
            old_name="palyer_name",
            new_name="player_name",
        ),
    ]