# Generated by Django 4.1 on 2024-03-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="plot_info",
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
                ("user_name", models.CharField(max_length=20, null=True)),
                ("period1", models.PositiveIntegerField()),
                ("period2", models.PositiveIntegerField(null=True)),
                ("period3", models.PositiveIntegerField(null=True)),
                ("select1", models.CharField(max_length=20)),
                ("select2", models.CharField(max_length=20)),
                ("select3", models.CharField(max_length=20)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("analysis_type", models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="user_info",
            fields=[
                (
                    "email",
                    models.EmailField(
                        default="", max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("password", models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
