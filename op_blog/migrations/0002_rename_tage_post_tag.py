# Generated by Django 4.0.3 on 2022-03-19 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('op_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tage',
            new_name='tag',
        ),
    ]