# Generated by Django 4.1.7 on 2023-03-27 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mysite', '0026_alter_author_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user',
            new_name='user_id',
        ),
    ]
