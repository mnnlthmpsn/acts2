# Generated by Django 3.0.5 on 2020-04-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200406_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.CharField(default='default', max_length=1000),
            preserve_default=False,
        ),
    ]
