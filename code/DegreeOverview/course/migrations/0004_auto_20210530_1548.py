# Generated by Django 2.2.12 on 2021-05-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20210530_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CourseName',
            field=models.CharField(default='', max_length=50, verbose_name='Course Name'),
        ),
    ]