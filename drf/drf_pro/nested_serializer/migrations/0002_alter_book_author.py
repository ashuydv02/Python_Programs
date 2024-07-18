# Generated by Django 4.2.13 on 2024-07-18 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nested_serializer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="nested_serializer.author",
            ),
        ),
    ]
