# Generated by Django 4.1.5 on 2023-01-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("complaints", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="image",
            field=models.CharField(max_length=100, null=True),
        ),
    ]