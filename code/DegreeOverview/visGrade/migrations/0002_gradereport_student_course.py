# Generated by Django 2.2.12 on 2021-05-30 21:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0004_auto_20210530_1548'),
        ('user', '0005_auto_20210522_1020'),
        ('visGrade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(default='', max_length=30, verbose_name='Student Name')),
                ('Marks', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Marks')),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Assessment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student')),
            ],
            options={
                'db_table': 'Grade_Report',
            },
        ),
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.IntegerField(default=2005, verbose_name='Semester')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student')),
            ],
            options={
                'db_table': 'Student_Course',
                'unique_together': {('student', 'course')},
            },
        ),
    ]
