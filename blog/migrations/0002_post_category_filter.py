# Generated by Django 3.0.4 on 2020-04-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_filter',
            field=models.PositiveIntegerField(choices=[(0, 'love'), (1, 'life')], default='1'),
        ),
    ]
