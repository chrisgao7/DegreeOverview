from django.db import models

# Create your models here.


class Course(models.Model):
    CourseID = models.AutoField('Course ID', primary_key=True)
    CourseName = models.CharField('Course Name', max_length=50, default='')
    Code = models.CharField('Course Code', max_length=10, default='')
    Type = models.CharField('Course Type', max_length=10, default='')
    Program = models.CharField('Course Program', max_length=10, default='')

    class Meta:
        db_table = 'Course'

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s_%s_%s' % (self.CourseID, self.CourseName, self.Code, self.Type, self.Program)


class CILO(models.Model):
    CILOID = models.AutoField('CILO ID', primary_key=True)
    CILOName = models.CharField('CILO Name', max_length=25, default='')
    Description = models.TextField('CILO Description', default='')
    PreCILO = models.CharField('Previous CILO', max_length=100, default='')
    # CourseID = models.CharField('CILO Program', max_length=25)
    AcademicYear = models.IntegerField("Academic Year", default=2005)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CILO'

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s_%s_%s' % (self.CILOID, self.CILOName, self.Description, self.PreCILO, self.AcademicYear)


class Assessment(models.Model):
    AssessmentID = models.AutoField('Assessment ID', primary_key=True)
    MethodName = models.CharField('Method Name', max_length=25, default='')
    Percentage = models.FloatField('Percentage', default=0.0)
    CILOIDs = models.CharField('CILOIDs', max_length=25, default='')
    # CourseID = models.CharField('CILO ID', max_length=25)
    AcademicYear = models.IntegerField("Academic Year", default=2005)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Assessment'

    def __str__(self):
        # redesign the output format
        return '%s_%s_%s_%s_%s' % (self.AssessmentID, self.MethodName, self.Percentage, self.CILOIDs, self.AcademicYear)
