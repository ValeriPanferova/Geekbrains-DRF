# Generated by Django 4.0 on 2022-01-14 20:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7871f343-b197-4180-a715-4b473d7711d3'), primary_key=True, serialize=False),
        ),
    ]
