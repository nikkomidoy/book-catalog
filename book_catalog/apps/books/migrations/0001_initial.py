# Generated by Django 4.2.4 on 2023-08-16 03:23

import book_catalog.apps.books.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(help_text="Summary of the book", max_length=1000)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("summary", models.TextField(help_text="Summary of the book", max_length=1000)),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True,
                        help_text="Book cover image in png/jpg file",
                        null=True,
                        upload_to=book_catalog.apps.books.utils.get_cover_image_upload_path,
                        validators=[book_catalog.apps.books.utils.valid_jpeg_or_png],
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="authors.author"),
                ),
                ("categories", models.ManyToManyField(help_text="Category of the book", to="books.category")),
            ],
        ),
    ]
