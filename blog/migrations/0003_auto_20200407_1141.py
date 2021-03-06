# Generated by Django 3.0.4 on 2020-04-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_filter2',
            field=models.PositiveIntegerField(choices=[(0, 'none'), (1, 'love'), (2, 'life'), (3, 'family'), (4, 'friends'), (5, 'others')], default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category_filter',
            field=models.PositiveIntegerField(choices=[(0, 'love'), (1, 'life'), (2, 'family'), (3, 'friends'), (4, 'others')], default='1'),
        ),
    ]
