# Generated by Django 5.1.1 on 2024-12-10 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_teacher', '0009_quiz_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='type',
            new_name='type_of',
        ),
    ]