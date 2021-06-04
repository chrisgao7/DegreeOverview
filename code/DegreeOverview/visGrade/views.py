from visGrade.models import GradeReport, Student_Course
from user.models import Account, Student
from course.models import Course
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import F, Q
from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pyecharts.globals import ThemeType
from pyecharts.charts import Pie
from random import randint
from django.contrib import messages
from jinja2 import Environment, FileSystemLoader
import numpy as np
import datetime

from django.conf import settings

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader(
    "./visGrade/templates/visGrade"))
# Create your views here.


def calculatePerformance(preCILOs, percentages, marks, ciloNames):
    data = dict()  # store the total cilo grade
    data2 = dict()  # store the student actual cilo grade
    # initialize the dict, Key is ciloName, value is cilo grade
    for i in range(0, len(ciloNames)):
        ciloName = ciloNames[i]
        data.setdefault(ciloName, 0)
        data2.setdefault(ciloName, 0)
    for ciloName in ciloNames:
        for i in range(0, len(preCILOs)):
            preCILO = preCILOs[i]
            if '-' in preCILO:
                x = preCILO.split('-')
                if ciloName in x:
                    data[ciloName] += percentages[i] / len(x)
                    data2[ciloName] += marks[i] / len(x)
            else:
                if ciloName == preCILO:
                    data[ciloName] += percentages[i]
                    data2[ciloName] += marks[i]
    return data.values(), data2.values()


def showPerformance(request):
    if(request.session.get('utype', 'none') != 'Student' or request.session.get('uid', 'none') == 'none'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'POST':
            # get the user's account id
            uid = request.session.get('uid', 'none')
            # according to account id to get student id
            account = Account.objects.get(id=uid)
            studentID = account.student.id
            # get all the courses id that student has learned
            takenCourses = Student_Course.objects.filter(
                student_id=studentID).values('course_id', 'Semester')
            # judge if student take any course
            if takenCourses.count() == 0:
                messages.error(
                    request, 'The student have not taken any course')
                return HttpResponseRedirect('showPerformance')

            # use list to store all the course object
            courses = []
            # 用字典去存course的名称和type
            for ob in takenCourses:
                courseID = ob['course_id']
                temp = Course.objects.get(CourseID=courseID)
                courses.append(temp)
            # get the value of course name and its academic year
            courseName = request.POST['courseName']
            semester = request.POST['semester']
            # judge if the course name or semester input is empty
            if (not courseName) and (not semester):
                messages.error(
                    request, 'Please input Course Name and Semester!!!')
                return HttpResponseRedirect('showPerformance')
            elif not courseName:
                messages.error(
                    request, 'Please input Course Name!!!')
                return HttpResponseRedirect('showPerformance')
            elif not semester:
                messages.error(
                    request, 'Please input Semester!!!')
                return HttpResponseRedirect('showPerformance')

            coursesByInput = Course.objects.filter(CourseName=courseName)
            if not coursesByInput:
                messages.error(request, 'Please input correct course name!')
                return HttpResponseRedirect('showPerformance')
            if not set(courses).intersection(set(coursesByInput)):
                messages.error(request, 'Sorry! you have not take this course')
                return HttpResponseRedirect('showPerformance')
            else:
                # print('input course name:' + courseName)
                course = None
                # judge if the input course exit in student taken courses set
                for ob in courses:
                    if ob.CourseName == courseName:
                        course = ob
                        takenSemester = Student_Course.objects.filter(student_id=studentID).get(
                            course_id=course.CourseID).Semester
                        print('Course Name: %s; Taken Semester: %d' %
                              (course.CourseName, takenSemester))
                if not course:
                    messages.error(
                        request, 'Please input correct course name!')
                    return HttpResponseRedirect('showPerformance')
                if takenSemester != int(semester):
                    messages.error(
                        request, 'Please check selected semester! Semester should be %d' % takenSemester)
                    return HttpResponseRedirect('showPerformance')
                # 拿到assessment的所有CILOIDs， 根据这个计算每个CILO的performance
                # 并 循环输出table渲染到页面。表单根据 method的方法改变
                assessments = course.assessment_set.filter(
                    AcademicYear=int(semester))
                cilos = course.cilo_set.filter(AcademicYear=int(semester))
                studentName = Student.objects.get(id=studentID).fullname
                assessmentMethods = []  # To store all the assessment methods name
                percentages = []
                preCILOs = []
                marks = []
                total_marks = 0
                try:
                    for assessment in assessments:
                        '''
                        get all marks, percentages, preCILOs of each assessment, and compute total marls
                        '''
                        assessmentID = assessment.AssessmentID
                        mark = GradeReport.objects.filter(student_id=studentID).get(
                            assessment_id=assessmentID).Marks
                        assessmentMethods.append(assessment.MethodName)
                        marks.append(mark)
                        percentages.append(assessment.Percentage)
                        preCILOs.append(assessment.CILOIDs)
                        total_marks += mark
                except Exception as e:
                    print('---Get assessments error %s' % (e))
                    messages.error(
                        request, 'Assessments get error')
                    return HttpResponseRedirect('showPerformance')
                ciloNames = []
                for cilo in cilos:
                    # get all CILO names
                    ciloName = cilo.CILOName
                    ciloNames.append(ciloName)
                totalPer, outcomes = calculatePerformance(
                    preCILOs, percentages, marks, ciloNames)

                # store values into session
                request.session['ciloNames'] = ciloNames
                request.session['totalPer'] = list(totalPer)
                request.session['outcomes'] = list(outcomes)

            return render(request, 'performance.html', locals())
        else:
            return HttpResponseRedirect('/user/stuMain')


def performance(request):
    if(request.session.get('utype', 'none') != 'Student'):
        return HttpResponseRedirect('login')
    else:
        if request.method == 'GET':
            return render(request, 'performance.html')
        elif request.method == 'POST':
            model = request.POST['model']
            ciloNames = request.session.get('ciloNames', 'none')
            totalPer = request.session.get('totalPer', 'none')
            outcomes = request.session.get('outcomes', 'none')
            print(ciloNames)
            print(totalPer)
            print(outcomes)
            for i in range(0, len(ciloNames)):
                ciloNames[i] = "CILO" + ciloNames[i]
            if model == 'bar_chart':
                c = (
                    Bar()
                    .add_xaxis(ciloNames)
                    .add_yaxis("Total", totalPer)
                    .add_yaxis("Obtain", outcomes)
                    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-Chart", subtitle="CILO Outcomes"))
                )
            if model == 'pie_chart':
                c = (
                    # 创建饼图
                    Pie()
                    # 为饼图增加标签和数据
                    .add("", list(zip(ciloNames, outcomes)))
                    # 为饼图增加主标题和副标题
                    .set_global_opts(title_opts=opts.TitleOpts(title="Pie Chart", subtitle="CILO Outcomes"))
                    # 为饼图增加数据标签
                    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n({d}%)"))
                )
            if model == 'line_chart':
                columns = ["Jan", "Feb", "Mar", "Apr", "May",
                           "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                # // 设置数据
                data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
                         135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
                data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
                         175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
                c = (
                    # 创建饼图
                    Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
                    # 增加主标题与副标题
                    .set_global_opts(title_opts=opts.TitleOpts(title="Line Chart", subtitle="CILO Outcomes"))
                    # X轴标签
                    .add_xaxis(columns)
                    # 增加折线图数据, symbol_size:圆点的大小，is_smooth:是否圆滑曲线,color:曲线的颜色
                    # 注意：当上面的init_opts设置了主题样式后，color就不起作用了
                    .add_yaxis("CILO1", data1, symbol_size=10, is_smooth=True, color="green")
                    .add_yaxis("CILO2", data2, symbol_size=10, is_smooth=True, color="blue")
                )
            return HttpResponse(c.render_embed())


def analysis(request):
    if(request.session.get('utype', 'none') == 'Student'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'POST':
            courseName = request.POST['courseName']
            semester = request.POST['semester']
            type = request.POST['type']
            print("Course Name:%s; Semester:%s, Type:%s" %
                  (courseName, semester, type))

            # check if input is empty
            if not courseName:
                messages.error(
                    request, 'Please input Course Name!!!')
                return HttpResponseRedirect('analysis')
            elif not type:
                messages.error(
                    request, 'Please input Course Type!!!')
                return HttpResponseRedirect('analysis')
            elif not semester:
                messages.error(
                    request, 'Please input Semester!!!')
                return HttpResponseRedirect('analysis')
            # get the number of courses according to  course name
            cnum = Course.objects.filter(CourseName=courseName).count()
            if (cnum == 0):
                messages.error(request, 'Please check course name!')
                return HttpResponseRedirect('analysis')
            try:
                # get the exact course according to course name and type
                course = Course.objects.get(
                    Q(CourseName=courseName) & Q(Type=type))
                courseID = course.CourseID
            except Exception as e:
                print('---Get error %s' % (e))
                messages.error(
                    request, 'Check course name or input type')
                return HttpResponseRedirect('analysis')

            assessments = course.assessment_set.filter(
                AcademicYear=int(semester))
            # judge if the input semester has the assessments according to input course name
            if assessments.count() == 0:
                messages.error(
                    request, 'The course has no assessment in this semester!')
                return HttpResponseRedirect('analysis')

            students = Student_Course.objects.filter(
                Q(course_id=courseID) & Q(Semester=semester))
            print(students)
            stuNum = students.count()
            # check if there is any student takes this course
            if stuNum == 0:
                messages.error(
                    request, 'There is no student taking this course!')
                return HttpResponseRedirect('analysis')

            cilos = course.cilo_set.filter(AcademicYear=int(semester))
            assessmentMethods = []  # To store all the assessment methods name
            percentages = []
            preCILOs = []
            avgMarks = []
            try:
                for assessment in assessments:
                    '''
                    get all marks, percentages, preCILOs of each assessment, and compute total marls
                    '''
                    assessmentID = assessment.AssessmentID
                    grades = GradeReport.objects.filter(
                        assessment_id=assessmentID)
                    totalMark = 0
                    for grade in grades:
                        totalMark += grade.Marks
                    avgMarks.append(totalMark/stuNum)
                    assessmentMethods.append(assessment.MethodName)
                    percentages.append(assessment.Percentage)
                    preCILOs.append(assessment.CILOIDs)
            except Exception as e:
                print('---Get assessments error %s' % (e))
                messages.error(
                    request, 'Assessments get error')
                return HttpResponseRedirect('analysis')

            ciloNames = []
            for cilo in cilos:
                # get all CILO names
                ciloName = cilo.CILOName
                ciloNames.append(ciloName)

            # call function to calculate performance
            totalPer, outcomes = calculatePerformance(
                preCILOs, percentages, avgMarks, ciloNames)

            # store the value into session
            request.session['ciloNames'] = ciloNames
            request.session['totalPer'] = list(totalPer)
            request.session['outcomes'] = list(outcomes)
            request.session['courseID'] = courseID
            request.session['inputSemester'] = semester
            print(semester)

            currentYear = datetime.datetime.now().year
            years = range(currentYear, 2004, -1)
            return render(request, 'analysisResult.html', locals())
        else:
            utype = request.session.get('utype', 'none')
            if utype == 'CourseDesigner':
                return HttpResponseRedirect('/user/cdMain')
            if utype == 'NonCourseDesigner':
                return HttpResponseRedirect('/user/ncdMain')


def analysisResult(request):
    if request.method == 'GET':
        return render(request, 'analysisResult.html')
    elif request.method == 'POST':
        # get values from POST
        model = request.POST['model']
        compareSemester = request.POST['compareSemester']

        # get values from session
        ciloNames = request.session.get('ciloNames', 'none')
        totalPer = request.session.get('totalPer', 'none')
        outcomes = request.session.get('outcomes', 'none')
        courseID = request.session.get('courseID', 'none')
        inputSemester = request.session.get('inputSemester', 'none')
        multipule = True

        # rename ciloName
        for i in range(0, len(ciloNames)):
            ciloNames[i] = "CILO" + ciloNames[i]

        # check if the semester input is empty
        if not compareSemester:
            compareSemester = inputSemester
            multipule = False

        # get course
        try:
            course = Course.objects.get(CourseID=courseID)
        except Exception as e:
            messages.error(
                request, 'Get course error!')
            return HttpResponseRedirect('/visGrade/analysis')

        students = Student_Course.objects.filter(
            Q(course_id=courseID) & Q(Semester=compareSemester))
        print(students)
        stuNum = students.count()
        # check if there is any student takes this course
        if stuNum == 0:
            messages.error(
                request, 'There is no student taking this course!')
            return HttpResponseRedirect('analysis')

        # get assessments of input semester and compare semester
        assessmentsCom = course.assessment_set.filter(
            AcademicYear=int(compareSemester))
        if assessmentsCom.count() == 0:
            messages.error(
                request, 'Please check compare semester!')
            return HttpResponseRedirect('/visGrade/analysis')
        print(assessmentsCom)

        # get cilos
        cilosCom = course.cilo_set.filter(AcademicYear=int(compareSemester))
        print(cilosCom)
        ciloNamesCom = []
        for cilo in cilosCom:
            # get all CILO names
            ciloName = cilo.CILOName
            ciloNamesCom.append(ciloName)

        percentages = []
        preCILOs = []
        avgMarks = []
        for assessment in assessmentsCom:
            '''
            get all marks, percentages, preCILOs of each assessment, and compute total marls
            '''
            assessmentID = assessment.AssessmentID
            grades = GradeReport.objects.filter(
                assessment_id=assessmentID)
            totalMark = 0
            for grade in grades:
                totalMark += grade.Marks
            avgMarks.append(totalMark/stuNum)
            percentages.append(assessment.Percentage)
            preCILOs.append(assessment.CILOIDs)

        # call function to calculate performance
        totalPerCom, outcomesCom = calculatePerformance(
            preCILOs, percentages, avgMarks, ciloNamesCom)
        totalPerCom = list(totalPerCom)
        outcomesCom = list(outcomesCom)
        print(totalPerCom)
        print(outcomesCom)

        # rename ciloName
        for i in range(0, len(ciloNamesCom)):
            ciloNamesCom[i] = "CILO" + ciloNamesCom[i]

        if model == 'bar_chart':
            if multipule == True:
                # 初始化grid对象
                c = Grid(init_opts=opts.InitOpts(
                    theme=ThemeType.ROMA, width='1350px'))

                # 柱状图
                # 创建柱状图
                bar1 = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
                # 增加主题和副标题
                bar1.set_global_opts(title_opts=opts.TitleOpts(title=inputSemester, subtitle="Analysis Outcomes", pos_left="7%"),
                                     legend_opts=opts.LegendOpts(pos_left="25%"))
                # 添加柱状图的数据
                bar1.add_xaxis(ciloNames)
                bar1.add_yaxis("Total", totalPer)
                bar1.add_yaxis("Average", outcomes)
                # 增加平均线
                # bar1.set_series_opts(markline_opts=opts.MarkLineOpts(
                #     data=[opts.MarkLineItem(name="平均值", type_="average")]))

                # 柱状图
                # 创建柱状图
                bar2 = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
                # 增加主题和副标题
                bar2.set_global_opts(title_opts=opts.TitleOpts(title=compareSemester, subtitle="Analysis Outcomes", pos_right="7%"),
                                     legend_opts=opts.LegendOpts(pos_right="25%"))
                # 添加柱状图的数据
                bar2.add_xaxis(ciloNamesCom)
                bar2.add_yaxis("Total", totalPerCom)
                bar2.add_yaxis("Average", outcomesCom)
                # 增加平均线
                # bar2.set_series_opts(markline_opts=opts.MarkLineOpts(
                #     data=[opts.MarkLineItem(name="平均值", type_="average")]))

                # 将两个图表分别添加到grid对象里面去
                # 对grid的pos参数而言，pos_left是显示在靠右的位置 pos_right同理
                c.add(bar1, grid_opts=opts.GridOpts(pos_right="55%"))
                c.add(bar2, grid_opts=opts.GridOpts(pos_left="55%"))

            else:
                c = (
                    Bar()
                    .add_xaxis(ciloNames)
                    .add_yaxis("Total", totalPer)
                    .add_yaxis("Average", outcomes)
                    .set_global_opts(title_opts=opts.TitleOpts(title=inputSemester, subtitle="Analysis Outcomes"))
                )
        if model == 'pie_chart':
            c = (
                # 创建饼图
                Pie()
                # 为饼图增加标签和数据
                .add("", list(zip(['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉'], [randint(100, 300) for _ in range(7)])))
                # 为饼图增加主标题和副标题
                .set_global_opts(title_opts=opts.TitleOpts(title="2019年销量统计", subtitle="单位: (万)"))
                # 为饼图增加数据标签
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}\n({d}%)"))
            )
        if model == 'line_chart':
            columns = ["Jan", "Feb", "Mar", "Apr", "May",
                       "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            # // 设置数据
            data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
                     135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
            data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
                     175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
            c = (
                # 创建饼图
                Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
                # 增加主标题与副标题
                .set_global_opts(title_opts=opts.TitleOpts(title="折线图", subtitle="一年的降水量与蒸发量"))
                # X轴标签
                .add_xaxis(columns)
                # 增加折线图数据, symbol_size:圆点的大小，is_smooth:是否圆滑曲线,color:曲线的颜色
                # 注意：当上面的init_opts设置了主题样式后，color就不起作用了
                .add_yaxis("降水量", data1, symbol_size=10, is_smooth=True, color="green")
                .add_yaxis("蒸发量", data2, symbol_size=10, is_smooth=True, color="blue")
            )
        return HttpResponse(c.render_embed())


def back(request):
    if(request.session.get('utype', 'none') == 'Student'):
        return HttpResponseRedirect('/user/login')
    else:
        utype = request.session.get('utype', 'none')
        if utype == 'CourseDesigner':
            return HttpResponseRedirect('/user/cdMain')
        if utype == 'NonCourseDesigner':
            return HttpResponseRedirect('/user/ncdMain')
