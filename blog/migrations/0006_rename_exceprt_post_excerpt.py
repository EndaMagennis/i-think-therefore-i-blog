# Generated by Django 4.2.8 on 2023-12-31 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='exceprt',
            new_name='excerpt',
        ),
    ]
