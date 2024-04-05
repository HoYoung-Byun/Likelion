# Generated by Django 5.0.4 on 2024-04-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="community",
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
                ("title", models.CharField(max_length=200)),
                ("writer", models.CharField(max_length=100)),
                ("pub", models.DateTimeField()),
                ("body", models.TextField()),
            ],
        ),
    ]