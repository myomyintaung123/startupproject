# Generated by Django 4.2.3 on 2023-09-23 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0003_trainer_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='computerknowledge',
            new_name='computerKnowledge',
        ),
    ]
