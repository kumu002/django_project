# Generated by Django 5.0.3 on 2024-05-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_users_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
