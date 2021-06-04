from enum import unique
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import *
from course.models import *

# Create your models here.


class GradeReport(models.Model):
    StudentName = models.CharField("Student Name", max_length=30, default='')
    Marks = models.IntegerField(
        "Marks", validators=[MaxValueValidator(100), MinValueValidator(1)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Grade_Report'

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s' % (self.student, self.assessment, self.Marks)


class Student_Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Semester = models.IntegerField("Semester", default=2005)

    class Meta:
        db_table = 'Student_Course'
        unique_together = ('student', 'course')

    def __str__(self):
        # redesign the output format
        return '%s|%s' % (self.student, self.course)
