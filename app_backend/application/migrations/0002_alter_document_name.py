# Generated by Django 5.0.6 on 2024-07-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="name",
            field=models.CharField(max_length=300),
        ),
    ]
