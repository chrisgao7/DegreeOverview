# Generated by Django 2.2.12 on 2021-05-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='User Name')),
                ('password', models.CharField(max_length=32, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('fullname', models.CharField(max_length=30, verbose_name='Full Name')),
                ('programme', models.CharField(max_length=15, verbose_name='Programme')),
                ('is_lecturer', models.BooleanField(default=False, verbose_name='Lecturer or Not')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='StuID')),
                ('enrollmentYear', models.IntegerField(default=2005, verbose_name='Enrollment Year')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Account')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'student',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='NonCourseDesigner',
            fields=[
                ('fullname', models.CharField(max_length=30, verbose_name='Full Name')),
                ('programme', models.CharField(max_length=15, verbose_name='Programme')),
                ('is_lecturer', models.BooleanField(default=False, verbose_name='Lecturer or Not')),
                ('is_designer', models.BooleanField(default=False, verbose_name='Designer or Not')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='StaffID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Account')),
            ],
            options={
                'verbose_name': 'noncourse_designer',
                'verbose_name_plural': 'noncourse_designer',
                'db_table': 'noncourse_designer',
            },
        ),
        migrations.CreateModel(
            name='CourseDesigner',
            fields=[
                ('fullname', models.CharField(max_length=30, verbose_name='Full Name')),
                ('programme', models.CharField(max_length=15, verbose_name='Programme')),
                ('is_lecturer', models.BooleanField(default=False, verbose_name='Lecturer or Not')),
                ('is_designer', models.BooleanField(default=False, verbose_name='Designer or Not')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='StaffID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Account')),
            ],
            options={
                'verbose_name': 'course_designer',
                'verbose_name_plural': 'course_designer',
                'db_table': 'course_designer',
            },
        ),
    ]
