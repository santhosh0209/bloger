# Generated by Django 3.0.4 on 2020-04-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, upload_to='images')),
                ('category', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]
