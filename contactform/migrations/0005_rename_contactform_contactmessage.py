# Generated by Django 5.0.3 on 2024-04-11 19:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contactform", "0004_alter_contactform_email_alter_contactform_message"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Contactform",
            new_name="ContactMessage",
        ),
    ]
