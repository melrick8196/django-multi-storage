# Generated by Django 3.0.5 on 2020-04-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20200415_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestorage',
            name='server_reply',
            field=models.TextField(null=True),
        ),
    ]
