from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, IntegerField

# Create your models here.


class Account(models.Model):
    username = models.CharField("User Name", max_length=30, unique=True)
    password = models.CharField("Password", max_length=32)
    type = CharField("Type", max_length=20, default='')
    # is_lecturer = models.BooleanField("Lecturer or Not", default=False)
    # is_designer = models.BooleanField("Designer or Not", default=False)

    class Meta:
        db_table = 'account'

    def __str__(self):
        # redesign the output format
        return 'User' + self.username


class User(models.Model):
    ''' This class is the parent of Student, CourseDesigner and NonCourseDesigner'''
    fullname = CharField("Full Name", max_length=30)
    programme = CharField("Programme", max_length=15)

    class Meta:
        abstract = True  # this is the abstract class


class Student(User):
    id = AutoField("StuID", primary_key=True)
    enrollmentYear = IntegerField("Enrollment Year", default=2005)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'
        verbose_name = 'student'
        verbose_name_plural = verbose_name

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s_%s' % (self.id, self.fullname, self.programme, self.enrollmentYear)


class Lecturer(User):
    # 1 is course designer, 0 is non-course designer, default is non-course designer
    # is_lecturer = models.BooleanField("Lecturer or Not", default=True)
    # is_designer = models.BooleanField("Designer or Not", default=False)

    class Meta:
        abstract = True  # this is the abstract class


class CourseDesigner(Lecturer):
    id = AutoField("StaffID", primary_key=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_designer'
        verbose_name = 'course_designer'
        verbose_name_plural = verbose_name

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s' % (self.id, self.fullname, self.programme)


class NonCourseDesigner(Lecturer):
    id = AutoField("StaffID", primary_key=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'noncourse_designer'
        verbose_name = 'noncourse_designer'
        verbose_name_plural = verbose_name

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s' % (self.id, self.fullname, self.programme)
