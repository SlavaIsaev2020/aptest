# Generated by Django 2.0.4 on 2018-04-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_auto_20180420_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lastName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
