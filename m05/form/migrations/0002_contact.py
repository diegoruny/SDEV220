# Generated by Django 5.1.1 on 2024-09-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("form", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("contact_Name", models.CharField(max_length=50)),
                ("contact_Email", models.EmailField(max_length=254)),
                ("contact_Date", models.DateField()),
                ("contact_Message", models.CharField(max_length=200)),
                ("timestamp_Date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
