# Generated by Django 4.2.4 on 2023-08-16 03:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("birth_date", models.DateField(blank=True, null=True)),
            ],
            options={
                "ordering": ["last_name", "first_name"],
            },
        ),
    ]
