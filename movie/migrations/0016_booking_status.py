# Generated by Django 3.1 on 2020-08-31 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_remove_booking_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]