# Generated by Django 5.0.4 on 2024-04-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
