# Generated by Django 4.1.5 on 2023-01-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Report",
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
                ("GRAFFITI", models.IntegerField()),
                ("FADED_SIGNAGE", models.IntegerField()),
                ("POTHOLES", models.IntegerField()),
                ("GARBAGE", models.IntegerField()),
                ("CONSTRUCTION_ROAD", models.IntegerField()),
                ("BROKEN_SIGNAGE", models.IntegerField()),
                ("BAD_STREETLIGHT", models.IntegerField()),
                ("BAD_BILLBOARD", models.IntegerField()),
                ("SAND_ON_ROAD", models.IntegerField()),
                ("CLUTTER_SIDEWALK", models.IntegerField()),
                ("UNKEPT_FACADE", models.IntegerField()),
            ],
        ),
    ]