# Generated by Django 2.2.12 on 2021-05-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210520_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='type',
            field=models.CharField(default='', max_length=20, verbose_name='Type'),
        ),
    ]
