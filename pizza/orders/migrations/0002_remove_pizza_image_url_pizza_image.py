# Generated by Django 5.0.6 on 2024-06-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pizza',
            name='image',
            field=models.ImageField(default='/static/images/pizza-6.jpg', upload_to='images/'),
            preserve_default=False,
        ),
    ]
