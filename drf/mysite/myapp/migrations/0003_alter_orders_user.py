# Generated by Django 4.2.13 on 2024-07-12 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_orders_customuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.customuser"
            ),
        ),
    ]
