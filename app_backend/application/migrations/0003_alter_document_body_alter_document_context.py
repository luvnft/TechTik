# Generated by Django 5.0.6 on 2024-07-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0002_alter_document_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="body",
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name="document",
            name="context",
            field=models.CharField(max_length=100000),
        ),
    ]
