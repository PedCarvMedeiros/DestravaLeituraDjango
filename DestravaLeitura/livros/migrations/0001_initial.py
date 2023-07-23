# Generated by Django 4.1 on 2023-07-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LivroInfo",
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
                ("nome", models.TextField(blank=True)),
                ("autor", models.TextField(blank=True)),
                ("genero", models.TextField(blank=True)),
                ("xerox", models.TextField(blank=True)),
                ("emprestado", models.TextField(blank=True)),
            ],
        ),
    ]