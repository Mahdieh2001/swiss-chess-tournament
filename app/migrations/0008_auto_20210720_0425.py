# Generated by Django 3.2.5 on 2021-07-19 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210719_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='points1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='points2',
            field=models.FloatField(null=True),
        ),
    ]
