# Generated by Django 5.0.4 on 2024-04-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/profile.png', upload_to='images/'),
        ),
    ]
