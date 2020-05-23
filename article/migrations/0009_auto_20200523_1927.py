# Generated by Django 2.0 on 2020-05-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20200523_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.CharField(choices=[('LST', 'lost'), ('FND', 'found'), ('SLL', 'sell'), ('GIV', 'give_away'), ('REQ', 'request')], default='REQ', max_length=3),
        ),
        migrations.AddField(
            model_name='article',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
