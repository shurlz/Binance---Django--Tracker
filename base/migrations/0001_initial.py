# Generated by Django 4.1.1 on 2022-11-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="coinStore",
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
                ("name", models.CharField(max_length=300)),
                ("symbol", models.CharField(max_length=300)),
                ("price", models.CharField(max_length=300)),
                ("change", models.CharField(max_length=300)),
                ("volume", models.CharField(max_length=300)),
                ("market_cap", models.CharField(max_length=300)),
                ("date", models.DateField()),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
