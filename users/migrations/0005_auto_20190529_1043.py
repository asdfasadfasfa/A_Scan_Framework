# Generated by Django 2.2.1 on 2019-05-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180703_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='iphone',
            field=models.CharField(default='88888888', max_length=13),
        ),
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.CharField(default='Engineer', max_length=30),
        ),
    ]
