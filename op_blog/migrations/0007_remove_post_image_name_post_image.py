# Generated by Django 4.0.3 on 2022-03-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('op_blog', '0006_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
