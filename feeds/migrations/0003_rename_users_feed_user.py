# Generated by Django 4.2.3 on 2023-07-27 05:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("feeds", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feed",
            old_name="users",
            new_name="user",
        ),
    ]
