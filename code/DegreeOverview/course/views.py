from django.shortcuts import render, redirect
from django.db.models import Q
from django.http.response import HttpResponse, HttpResponseRedirect
from pyecharts.globals import CurrentConfig

from .models import *
import xlrd
from django.contrib import messages
from django.db import transaction
import logging
from pyecharts import options as opts
from pyecharts.charts import Tree
from pyecharts.charts import Graph
import datetime
from pyecharts import options as opts
from jinja2 import Environment, FileSystemLoader

# Create your views here.

# Get an instance of a logger
logger = logging.getLogger('django')


# def Visualize(request):
#     return render(request, 'performance.html')


def Search(request):
    if (request.session.get('utype', 'none') == 'CourseDesigner'
            or request.session.get('utype', 'none') == 'NonCourseDesigner'
            or request.session.get('utype', 'none') == 'Student'):
        if request.method == 'GET':
            query_dict = request.GET.dict()
            keyword = query_dict.get("keyword")
            search_word = query_dict.get('search_word')

            # store the keyword and search_word for latter turn back from course info to search result
            request.session['keyword'] = keyword
            request.session['search_word'] = search_word

            if keyword.upper() == 'COURSE':
                models = Course.objects.filter(Q(CourseName=search_word) | Q(
                    Type=search_word) | Q(Program=search_word) | Q(Code=search_word))

                context = {
                    'model': models,
                }
                return render(request, 'searchByCourseResult.html', context)
            elif keyword.upper() == 'CILO':
                currentYear = datetime.datetime.now().year
                courseid = Course.objects.get(CourseName=search_word)
                allcilo = CILO.objects.all()
                model1 = CILO.objects.filter(
                    Q(course_id=courseid), Q(AcademicYear=currentYear))

                model2 = []
                # get all the pre cilos
                for cilo in model1:
                    if (cilo.PreCILO != ""):
                        # print(cilo)
                        temp = cilo.PreCILO
                        res = temp.replace(
                            "[", "").replace("]", "").replace("'", "")
                        precilos = res.split(", ")
                        # print(precilos)
                        for i in precilos:
                            preciloinfo = i.split("-")
                            precourse = Course.objects.get(
                                Q(CourseName=preciloinfo[0]), Q(Type=preciloinfo[1]))
                            precilo = CILO.objects.get(Q(course_id=precourse.CourseID), Q(
                                CILOName=preciloinfo[2]), Q(AcademicYear=currentYear))
                            precilo.CILOName = precourse.CourseName + " CILO" + precilo.CILOName
                            check = True
                            for item in model2:
                                if(item.CILOID == precilo.CILOID):
                                    check = False
                            if(check):
                                model2.append(precilo)
                model3 = []
                # get all the past cilos
                for cilo in model1:
                    for tempcilo in allcilo:
                        if (tempcilo.PreCILO != ""):
                            # print(cilo)
                            temp = tempcilo.PreCILO
                            res = temp.replace(
                                "[", "").replace("]", "").replace("'", "")
                            precilos = res.split(", ")
                            # print(precilos)
                            for i in precilos:
                                preciloinfo = i.split("-")
                                coursename = Course.objects.get(
                                    CourseID=cilo.course_id).CourseName
                                coursetype = Course.objects.get(
                                    CourseID=cilo.course_id).Type
                                if(coursename == preciloinfo[0] and coursetype == preciloinfo[1] and cilo.CILOName == preciloinfo[2]):
                                    check = True
                                    for item in model3:
                                        if (item.CILOID == tempcilo.CILOID):
                                            check = False
                                    if (check):
                                        model3.append(tempcilo)
                context = {
                    'model1': model1,
                    'model2': model2,
                    'model3': model3,
                    'coursename': search_word
                }
                return render(request, 'searchByCiloResult.html', context)
            elif keyword.upper() == 'KEYWORD':
                print(search_word)
                course = Course.objects.filter(Q(CourseName=search_word) | Q(
                    Type=search_word) | Q(Program=search_word) | Q(Code=search_word))
                allcourse = Course.objects.all()

                flag = True
                for item in allcourse:
                    if(item.CourseName == search_word):
                        flag = False
                        cilo = CILO.objects.filter(Q(course_id=item.CourseID))

                if(flag):
                    cilo = []

                context = {
                    'cilo': cilo,
                    'course': course
                }
                return render(request, 'searchByKeywordResult.html', context)
    else:
        return HttpResponseRedirect('/user/login')

# turn back to user main page


def TurnBackToMain(request):
    if (request.session.get('utype', 'none') == 'CourseDesigner'):
        return HttpResponseRedirect('/user/cdMain')
    elif (request.session.get('utype', 'none') == 'NonCourseDesigner'):
        return HttpResponseRedirect('/user/ncdMain')
    elif (request.session.get('utype', 'none') == 'Student'):
        return HttpResponseRedirect('/user/stuMain')

#  turn back to course info page


def TurnToCourseInfo(request, id):
    request.session['operation'] = "EditCourse"
    print(request.session.get('operation', 'none'))
    if (request.session.get('utype', 'none') == 'CourseDesigner'):
        http = '/course/cdCourseInfo/%d/' % id
        return HttpResponseRedirect(http)
    elif (request.session.get('utype', 'none') == 'NonCourseDesigner'):
        http = '/course/ncdCourseInfo/%d/' % id
        return HttpResponseRedirect(http)
    elif (request.session.get('utype', 'none') == 'Student'):
        http = '/course/stuCourseInfo/%d/' % id
        return HttpResponseRedirect(http)


def TurnBackToSearchHis(request):
    html = '/course/search/?search_word=%s&keyword=%s' % (request.session.get(
        'search_word', 'none'), request.session.get('keyword', 'none'))
    return HttpResponseRedirect(html)


def cdCourseInfo(request, id):
    print(request.session.get('utype', 'none'))
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            try:
                currentYear = datetime.datetime.now().year
                obj = Course.objects.get(CourseID=id)
                cilo = CILO.objects.filter(course_id=id).order_by('CILOName')
                assessment = Assessment.objects.filter(Q(course_id=id), Q(
                    AcademicYear=currentYear)).order_by('Percentage')
            except Course.DoesNotExist:
                return HttpResponse("Data wrong!")

            # search and return all after course
            flag = False
            for item in cilo:
                if(item.PreCILO != ""):
                    flag = True

            allprecourses = []
            if(flag):
                for item in cilo:
                    temp = item.PreCILO
                    res = temp.replace(
                        "[", "").replace("]", "").replace("'", "")
                    precilos = res.split(", ")
                    print(precilos)
                    for i in precilos:
                        preciloinfo = i.split("-")
                        precourse = Course.objects.get(
                            Q(CourseName=preciloinfo[0]), Q(Type=preciloinfo[1]))
                        allprecourses.append(precourse)
                allprecourses = list(set(allprecourses))

            # search and return all after course
            allaftercilos = []
            for item in cilo:
                cilocontent = "%s-%s-%s" % (obj.CourseName,
                                            obj.Type, item.CILOName)
                # print(cilocontent)
                aftercilos = CILO.objects.filter(PreCILO__contains=cilocontent)
                # print(aftercilos)
                allaftercilos.append(aftercilos)

            allaftercourse = []
            for item in allaftercilos:
                for i in item:
                    course = Course.objects.get(CourseID=i.course_id)
                    allaftercourse.append(course)
            allaftercourse = list(set(allaftercourse))
            # print(allaftercourse)

            # search and return the after course

            # aftercourse =Course.objects.filter()
            model = {
                'id': id,
                'name': obj.CourseName,
                'code': obj.Code,
                'type': obj.Type,
                'programme': obj.Program,
            }
            context = {
                'model': model,
                'cilo': cilo,
                'assessment': assessment,
                'allaftercourse': allaftercourse,
                'allprecourses': allprecourses
            }
            return render(request, 'cdCourseInfo.html', context)


def ncdCourseInfo(request, id):
    if (request.session.get('utype', 'none') != 'NonCourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            try:
                currentYear = datetime.datetime.now().year
                obj = Course.objects.get(CourseID=id)
                cilo = CILO.objects.filter(course_id=id).order_by('CILOName')
                assessment = Assessment.objects.filter(Q(course_id=id), Q(AcademicYear=currentYear)).order_by(
                    'Percentage')
            except Course.DoesNotExist:
                return HttpResponse("Data wrong!")

            # search and return all after course
            flag = False
            for item in cilo:
                if (item.PreCILO != ""):
                    flag = True

            allprecourses = []
            if (flag):
                for item in cilo:
                    temp = item.PreCILO
                    res = temp.replace(
                        "[", "").replace("]", "").replace("'", "")
                    precilos = res.split(", ")
                    print(precilos)
                    for i in precilos:
                        preciloinfo = i.split("-")
                        precourse = Course.objects.get(
                            Q(CourseName=preciloinfo[0]), Q(Type=preciloinfo[1]))
                        allprecourses.append(precourse)
                allprecourses = list(set(allprecourses))

            # search and return all after course
            allaftercilos = []
            for item in cilo:
                cilocontent = "%s-%s-%s" % (obj.CourseName,
                                            obj.Type, item.CILOName)
                # print(cilocontent)
                aftercilos = CILO.objects.filter(PreCILO__contains=cilocontent)
                # print(aftercilos)
                allaftercilos.append(aftercilos)

            allaftercourse = []
            for item in allaftercilos:
                for i in item:
                    course = Course.objects.get(CourseID=i.course_id)
                    allaftercourse.append(course)
            allaftercourse = list(set(allaftercourse))
            # print(allaftercourse)

            # search and return the after course

            # aftercourse =Course.objects.filter()
            model = {
                'id': id,
                'name': obj.CourseName,
                'code': obj.Code,
                'type': obj.Type,
                'programme': obj.Program,
            }
            context = {
                'model': model,
                'cilo': cilo,
                'assessment': assessment,
                'allaftercourse': allaftercourse,
                'allprecourses': allprecourses
            }
            return render(request, 'ncdCourseInfo.html', context)


def stuCourseInfo(request, id):
    print(request.session.get('utype', 'none'))
    if (request.session.get('utype', 'none') != 'Student'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            try:
                currentYear = datetime.datetime.now().year
                obj = Course.objects.get(CourseID=id)
                cilo = CILO.objects.filter(course_id=id).order_by('CILOName')
                assessment = Assessment.objects.filter(Q(course_id=id), Q(AcademicYear=currentYear)).order_by(
                    'Percentage')
            except Course.DoesNotExist:
                return HttpResponse("Data wrong!")

            # search and return all after course
            flag = False
            for item in cilo:
                if (item.PreCILO != ""):
                    flag = True

            allprecourses = []
            if (flag):
                for item in cilo:
                    temp = item.PreCILO
                    res = temp.replace(
                        "[", "").replace("]", "").replace("'", "")
                    precilos = res.split(", ")
                    print(precilos)
                    for i in precilos:
                        preciloinfo = i.split("-")
                        precourse = Course.objects.get(
                            Q(CourseName=preciloinfo[0]), Q(Type=preciloinfo[1]))
                        allprecourses.append(precourse)
                allprecourses = list(set(allprecourses))

            # search and return all after course
            allaftercilos = []
            for item in cilo:
                cilocontent = "%s-%s-%s" % (obj.CourseName,
                                            obj.Type, item.CILOName)
                # print(cilocontent)
                aftercilos = CILO.objects.filter(PreCILO__contains=cilocontent)
                # print(aftercilos)
                allaftercilos.append(aftercilos)

            allaftercourse = []
            for item in allaftercilos:
                for i in item:
                    course = Course.objects.get(CourseID=i.course_id)
                    allaftercourse.append(course)
            allaftercourse = list(set(allaftercourse))
            # print(allaftercourse)

            # search and return the after course

            # aftercourse =Course.objects.filter()
            model = {
                'id': id,
                'name': obj.CourseName,
                'code': obj.Code,
                'type': obj.Type,
                'programme': obj.Program,
            }
            context = {
                'model': model,
                'cilo': cilo,
                'assessment': assessment,
                'allaftercourse': allaftercourse,
                'allprecourses': allprecourses
            }
            return render(request, 'stuCourseInfo.html', context)

# Course Operation


def addCourse(request):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'POST':
            username = request.session.get('username', 'none')
            request.session['operation'] = "CreateCourse"
            print(request.session.get('operation', 'none'))
            query_dict = request.POST.dict()
            name = query_dict.get('name')
            code = query_dict.get('code')
            type = query_dict.get('type')
            programme = query_dict.get('programme')
            if (name == "" or code == "" or type == "" or programme == ""):
                messages.error(request, 'Here are some information missing')
                return HttpResponseRedirect('/course/addcourse/')

            id = Course.objects.filter(
                Q(CourseName=name), Q(Code=code), Q(Type=type))
            if(id.exists() == True):
                messages.error(request, 'The course already exist')
                return HttpResponseRedirect('/course/addcourse/')
            else:
                Course.objects.create(
                    CourseName=name,
                    Code=code,
                    Type=type,
                    Program=programme,
                )
            id = Course.objects.get(Q(CourseName=name), Q(Type=type)).CourseID
            html = '/course/addciloassessment/%d/' % id
            logger.info('%s add course' % username)
            return redirect(html)
        elif request.method == 'GET':
            return render(request, 'createCourse.html')


def addCiloAssessment(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == "GET":
            try:
                currentYear = datetime.datetime.now().year
                obj = Course.objects.get(CourseID=id)
                cilo = CILO.objects.filter(course_id=id).order_by('CILOName')
                assessment = Assessment.objects.filter(Q(course_id=id), Q(AcademicYear=currentYear)).order_by(
                    'Percentage')
            except Course.DoesNotExist:
                return HttpResponse("Data wrong!")

            # allPreCILOInfo = []
            # for item in cilo:
            #     preciloids = item.PreCILO.split("-")
            #     PreCILOInfo = []
            #     for ciloid in preciloids:
            #         CILOInfo = CILO.objects.get(CILOID=ciloid)
            #         CourseInfo = Course.objects.get(CourseID=CILOInfo.course_id)
            #         info = "%s-%s-%s"%(CourseInfo.CourseName, CourseInfo.Type, CILOInfo.CILOName)
            #         PreCILOInfo.append(info)
            #     allPreCILOInfo.append(PreCILOInfo)

            # check if add pre cilo button appear
            for item in cilo:
                temp = item.PreCILO
                res = temp.replace("[", "").replace("]", "").replace("'", "")
                # print(res)
                item.PreCILO = res

            # print(cilo)
            model = {
                'id': id,
                'name': obj.CourseName,
                'code': obj.Code,
                'type': obj.Type,
                'programme': obj.Program,
            }
            context = {
                'model': model,
                'CourseID': id,
                'cilo': cilo,
                'assessment': assessment,
            }
            return render(request, 'createCILOAssessment.html', context)


def finishCreate(request, id):
    cilos = CILO.objects.filter(course_id=id)
    assessments = Assessment.objects.filter(course_id=id)
    if(cilos.exists() and assessments.exists()):
        messages.error(request, 'Create sucessfully!')
        html = "/user/cdMain"
        return HttpResponseRedirect(html)
    else:
        messages.error(
            request, 'Create unsucessfully! CILO or assessment are not import!')
        html = "/course/addciloassessment/%d/" % id
        return HttpResponseRedirect(html)


def EditCourse(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            try:
                obj = Course.objects.get(CourseID=id)
            except Course.DoesNotExist:
                return HttpResponse("Data wrong!")
            model = {
                'id': id,
                'name': obj.CourseName,
                'code': obj.Code,
                'type': obj.Type,
                'programme': obj.Program,
            }
            context = {
                'model': model
            }
            return render(request, 'editCourse.html', context)


def UpdateCourse(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'POST':
            try:
                obj = Course.objects.get(CourseID=id)
            except Course.DoesNotExist:
                return HttpResponse("Data wrong!")
            # get the input
            query_dict = request.POST.dict()
            name = query_dict.get('name', None)
            type = query_dict.get('type', None)
            code = query_dict.get('code', None)
            programme = query_dict.get('programme', None)
            # check whether input is null
            if name == '':
                name = obj.CourseName
            if type == '':
                type = obj.Type
            if code == '':
                code = obj.Code
            if programme == '':
                programme = obj.Program
            # set the updated data and save
            obj.CourseName = name
            obj.Type = type
            obj.Code = code
            obj.Program = programme
            obj.save()
            html = '/course/courseInfo/%d/' % id
            return redirect(html)


def TurnFromEdit(request, id):
    print(request.session.get('operation', 'none'))
    if (request.session.get('operation', 'none') == 'CreateCourse'):
        html = '/course/addciloassessment/%d/' % id
    elif (request.session.get('operation', 'none') == 'EditCourse'):
        html = '/course/courseInfo/%d/' % id
    return HttpResponseRedirect(html)

# CILO Operation


def AddCILO(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            allCILO = CILO.objects.exclude(course_id=id).order_by(
                "course_id").order_by("CILOName")
            allCourse = Course.objects.exclude(
                CourseID=id).order_by("CourseID")
            context = {
                'CourseID': id,
                'CILO': allCILO,
                'Course': allCourse
            }
            return render(request, 'addCILO.html', context)
        elif request.method == 'POST':

            # get the cilo name and discription
            query_dict = request.POST.dict()
            cilo_name = query_dict.get("name", None)
            cilo_discription = query_dict.get("discription", None)

            # store all the pre cilo ids in preCILO attribute
            # store the discription of pre cilos
            precilos = request.POST.getlist("precilo")
            # precilocontent = "" # store the id of pre cilos
            # for precilo in precilos:
            #     content = precilo.split("-")
            #     courseid = Course.objects.get(Q(CourseName=content[0]), Q(Type=content[1])).CourseID
            #     ciloid = CILO.objects.get(Q(course_id=courseid), Q(CILOName=content[2])).CILOID
            #     if (precilo == precilos[0]):
            #         precilocontent += "%s" % ciloid
            #     else:
            #         precilocontent += "-%s" % ciloid

            currentYear = datetime.datetime.now().year
            CILOs = CILO.objects.filter(course_id=id)
            # check if the cilo is alreagy 3
            if(CILOs.count() == 3):
                messages.error(
                    request, 'There are already enough cilos!')
                html = "/course/editcilo/%d/" % id
                return HttpResponseRedirect(html)

            # check if the input is null
            elif (cilo_name == "" or cilo_discription == ""):
                messages.error(
                    request, 'Cilo name or discription should not be empty!')
                html = "/course/editcilo/%d/" % id
                return HttpResponseRedirect(html)

            # check if the cilo name is already exist
            elif (CILOs.filter(CILOName=cilo_name).exists()):
                messages.error(
                    request, 'This cilo has already exist!')
                html = "/course/addcilo/%d/" % id
                return HttpResponseRedirect(html)
            elif(len(precilos) == 0):
                CILO.objects.create(
                    CILOName=cilo_name,
                    Description=cilo_discription,
                    course_id=id,
                    AcademicYear=currentYear
                )
            else:
                CILO.objects.create(
                    CILOName=cilo_name,
                    Description=cilo_discription,
                    PreCILO=precilos,
                    course_id=id,
                    AcademicYear=currentYear
                )

            html = '/course/editcilo/%d/' % id
            return HttpResponseRedirect(html)


def DeleteCilo(request, ciloid, courseid):
    CILO.objects.filter(CILOID=ciloid).delete()
    html = '/course/editcilo/%d/' % courseid
    return redirect(html)


def EditCilo(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            try:
                cilo_model = CILO.objects.filter(
                    course_id=id).order_by('CILOName')
            except CILO.DoesNotExist:
                return HttpResponse('Data does not exist!')

            # get all the course and cilo information
            course_models = Course.objects.exclude(CourseID=id)
            course_name = []
            for course_model in course_models:
                course_name.append(course_model.CourseName)

            ciloid_models = CILO.objects.exclude(course_id=id)
            cilo_id = []
            for ciloid_model in ciloid_models:
                cilo_id.append(ciloid_model.CILOID)

            # indicate the operation type
            operation = request.session.get('operation', 'none')

            # all courses and cilos
            allCILO = CILO.objects.exclude(course_id=id).order_by(
                "course_id").order_by("CILOName")
            allCourse = Course.objects.exclude(
                CourseID=id).order_by("CourseID")

            context = {
                'model': cilo_model,
                'course_name': course_name,
                'clio_id': cilo_id,
                'CourseID': id,
                'operation': operation,
                'CILO': allCILO,
                'Course': allCourse
            }

            return render(request, 'editCILO.html', context)
        elif request.method == 'POST':
            try:
                cilo_model = CILO.objects.filter(course_id=id)
            except CILO.DoesNotExist:
                return HttpResponse('Data does not exist!')
            for i in range(cilo_model.count()):
                index = i + 1
                ciloid = 'ciloid%d' % index
                name = 'name%d' % index
                discription = 'discription%d' % index
                precilos = 'precilo%d' % index
                Ciloid = request.POST.get(ciloid, None)
                Name = request.POST.get(name, None)
                Discription = request.POST.get(discription, None)
                Precilos = request.POST.getlist(precilos, None)

                if (Name == "" or Discription == ""):
                    return HttpResponse('Please enter a CILO name and description!')

                currentYear = datetime.datetime.now().year
                cilo_content = CILO.objects.get(Q(course_id=id), Q(
                    CILOID=Ciloid), Q(AcademicYear=currentYear))

                cilo_content.CILOName = Name
                cilo_content.Description = Discription

                if(len(Precilos) != 0):
                    cilo_content.PreCILO = Precilos

                cilo_content.save()
            if(request.session.get('operation', 'none') == 'CreateCourse'):
                html = '/course/addciloassessment/%d/' % id
            elif(request.session.get('operation', 'none') == 'EditCourse'):
                html = '/course/courseInfo/%d/' % id
            return HttpResponseRedirect(html)


def importCILO(request, id):
    if(request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('user/login')
    else:
        if request.method == 'GET':
            logger.info('This is a info. The request method is GET')
            context = {
                'CourseID': id
            }
            return render(request, 'importCILO.html', context)
        elif request.method == 'POST':
            username = request.session.get('username', 'none')
            file = request.FILES.get('cilofile')
            if file == None:
                messages.error(request, 'Please upload a file!')
                html = "/course/importCILO/%d/" % id
                return HttpResponseRedirect(html)
            else:
                type_excel = file.name.split('.')[1]  # get the type of file
                # print(type_excel)
            if (type_excel == 'xls' or type_excel == 'xlsx'):
                # open the new workbook of excel file
                wb = xlrd.open_workbook(
                    filename=None, file_contents=file.read())
                # logger.info('------------------------')
                sheetNum = len(wb.sheet_names())  # the number of sheets
                for i in range(1, sheetNum):
                    # judge if other sheets contain any data, if so, show the error
                    nrows = wb.sheet_by_index(i).nrows
                    if(nrows > 0):
                        messages.error(
                            request, 'All the data must be contained in first sheet!')
                        html = "/course/importCILO/%d/" % id
                        return HttpResponseRedirect(html)
                # choose the first sheet as table
                table = wb.sheets()[0]
                nrows = table.nrows  # the number of rows
                # initialize a new course just created
                course = Course.objects.get(CourseID=id)
                # obtain all the cilos according to this course
                cilos = course.cilo_set.all()
                # calculate the number of cilos
                ciloNum = cilos.count()
                # 加一个判断：判断rows是否等于0 或者 大于 3， 如果是则进行下一步
                # 先声明一个course object
                sum = nrows + ciloNum  # total number of cilos after import
                if (nrows >= 5 or sum >= 5):
                    messages.error(request, 'Too many CILOs')
                    html = "/course/importCILO/%d/" % id
                    return HttpResponseRedirect(html)
                elif nrows == 1:
                    messages.error(request, 'No data to import')
                    html = "/course/importCILO/%d/" % id
                    return HttpResponseRedirect(html)
                try:
                    with transaction.atomic():
                        headers = table.row_values(0)
                        headerSet = ['CILO Name',
                                     'CILO Description', 'Previous CILO']
                        if len(headers) != len(headerSet):
                            messages.error(
                                request, 'The number of headers is wrong!')
                            html = "/course/importCILO/%d/" % id
                            return HttpResponseRedirect(html)
                        currentYear = datetime.datetime.now().year
                        for i in range(0, len(headerSet)):
                            # judge whether the hearder of file is correct
                            if headers[i] != headerSet[i]:
                                messages.error(
                                    request, 'The header format is wrong!')
                                html = "/course/importCILO/%d/" % id
                                return HttpResponseRedirect(html)
                        # check whether the header is correct
                        for i in range(1, nrows):
                            # 按行插值
                            for j in range(0, 3):
                                print('---------------------')
                                print(table.cell(i, j))
                                print(table.cell(i, j).ctype)
                                # c_cell = table.cell(i, j)
                                c_type = table.cell(i, j).ctype
                                if j == 0:
                                    if c_type == 2:
                                        CILOName = int(table.cell_value(i, j))
                                    else:
                                        messages.error(
                                            request, 'Data of CILO Name is wrong')
                                        html = "/course/importCILO/%d/" % id
                                        return HttpResponseRedirect(html)
                                if j == 1:
                                    if c_type == 1 or c_type == 0:
                                        Description = table.cell_value(i, j)
                                    else:
                                        messages.error(
                                            request, 'Data of CILO Description is wrong')
                                        html = "/course/importCILO/%d/" % id
                                        return HttpResponseRedirect(html)
                                if j == 2:
                                    if c_type == 1 or c_type == 0:
                                        PreCILO = table.cell_value(i, j)
                                    else:
                                        messages.error(
                                            request, 'Data of Previous CILO is wrong')
                                        html = "/course/importCILO/%d/" % id
                                        return HttpResponseRedirect(html)
                            CILO.objects.create(CILOName=CILOName, Description=Description,
                                                PreCILO=PreCILO, AcademicYear=currentYear, course=course)
                except Exception as e:
                    messages.error(request, 'Error occurs')
                    print('---error---%s' % (e))
                    html = "/course/importCILO/%d/" % id
                    return HttpResponseRedirect(html)
                messages.success(request, 'The file upload successfully')
                logger.info('%s import the CILO' % username)
                html = "/course/addciloassessment/%d/" % id
                return HttpResponseRedirect(html)
            messages.error(request, 'The upload file is not .xlsx or .xls')
            html = "/course/importCILO/%d/" % id
            return HttpResponseRedirect(html)

# Assessment Operation


def AddAssessment(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            CILOs = CILO.objects.filter(course_id=id)
            context = {
                'CourseID': id,
                'CILO': CILOs
            }
            return render(request, 'addAssessment.html', context)
        elif request.method == 'POST':
            CILOs = CILO.objects.filter(course_id=id)
            query_dict = request.POST.dict()
            methodname = query_dict.get("methodname", None)
            percentage = query_dict.get("percentage", None)
            cilos = request.POST.getlist("cilos")
            currentYear = datetime.datetime.now().year

            # check the if the input is null
            if (methodname == "" or percentage == "" or len(cilos) == 0):
                messages.error(
                    request, 'Please enter a Assessment method and percentage and related cilos!')
                html = "/course/addassessment/%d/" % id
                return HttpResponseRedirect(html)

            ciloscontent = ""
            for cilo in cilos:
                print(cilo)
                if (cilo == cilos[0]):
                    ciloscontent += "%s" % cilo
                else:
                    ciloscontent += "-%s" % cilo
            print(ciloscontent)

            assessment = Assessment.objects.filter(Q(course_id=id), Q(
                AcademicYear=currentYear), Q(MethodName=methodname))
            if(assessment.exists()):
                messages.error(request, 'This assessment already exists!')
                context = {
                    "name": methodname,
                    "percentage": percentage,
                    'CILO': CILOs,
                    "CourseID": id,
                }
                return render(request, 'addAssessment.html', context)

            Assessment.objects.create(
                MethodName=methodname,
                Percentage=percentage,
                CILOIDs=ciloscontent,
                course_id=id,
                AcademicYear=currentYear
            )

            html = '/course/editassessment/%d/' % id
            return HttpResponseRedirect(html)


def DeleteAssessment(request, assessmentid, courseid):
    Assessment.objects.filter(AssessmentID=assessmentid).delete()
    html = '/course/editassessment/%d/' % courseid
    return redirect(html)


def EditAssessment(request, id):
    if (request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            try:
                currentYear = datetime.datetime.now().year
                CILOs = CILO.objects.filter(course_id=id)
                assessment = Assessment.objects.filter(Q(course_id=id), Q(
                    AcademicYear=currentYear)).order_by('Percentage')
            except Assessment.DoesNotExist:
                return HttpResponse('Data does not exist!')
            operation = request.session.get('operation', 'none')
            context = {
                'CourseID': id,
                'assessment': assessment,
                'operation': operation,
                'CILO': CILOs
            }
            return render(request, 'editAssessment.html', context)
        elif request.method == 'POST':
            try:
                currentYear = datetime.datetime.now().year
                assessment_model = Assessment.objects.filter(
                    Q(course_id=id), Q(AcademicYear=currentYear))
            except CILO.DoesNotExist:
                return HttpResponse('Data not exist!')

            TotalPercentage = 0
            for i in range(assessment_model.count()):
                index = i + 1
                percentage = 'percentage%d' % index
                Percentage = request.POST.get(percentage, None)
                TotalPercentage = TotalPercentage + float(Percentage)

            if(TotalPercentage != 100):
                messages.error(
                    request, 'The total percentage of methods should equal to 100!')
                html = "/course/editassessment/%d/" % id
                return HttpResponseRedirect(html)
            else:
                for i in range(assessment_model.count()):
                    index = i + 1
                    assessmentid = 'assessmentid%d' % index
                    method = 'method%d' % index
                    percentage = 'percentage%d' % index
                    cilos = 'cilos%d' % index

                    Assessmentid = request.POST.get(assessmentid, None)
                    Method = request.POST.get(method, None)
                    Percentage = request.POST.get(percentage, None)
                    cilos = request.POST.getlist(cilos)

                    # check the if the input is null
                    if (Method == "" or Percentage == "" or len(cilos) == 0):
                        messages.error(
                            request, 'Please enter a Assessment method and percentage and related cilos!')
                        html = "/course/editassessment/%d/" % id
                        return HttpResponseRedirect(html)

                    ciloscontent = ""
                    for cilo in cilos:
                        print(cilo)
                        if (cilo == cilos[0]):
                            ciloscontent += "%s" % cilo
                        else:
                            ciloscontent += "-%s" % cilo

                    assessment_content = Assessment.objects.get(
                        Q(course_id=id), Q(AssessmentID=Assessmentid))
                    assessment_content.MethodName = Method
                    assessment_content.Percentage = Percentage
                    assessment_content.CILOIDs = ciloscontent
                    assessment_content.save()

            if (request.session.get('operation', 'none') == 'CreateCourse'):
                html = '/course/addciloassessment/%d/' % id
            elif (request.session.get('operation', 'none') == 'EditCourse'):
                html = '/course/courseInfo/%d/' % id
            return HttpResponseRedirect(html)


def importAssessment(request, id):
    if(request.session.get('utype', 'none') != 'CourseDesigner'):
        return HttpResponseRedirect('user/login')
    else:
        if request.method == 'GET':
            logger.info('This is a info.')
            context = {
                'CourseID': id
            }
            return render(request, 'importAssessment.html', context)
        elif request.method == 'POST':
            username = request.session.get('username', 'none')
            file = request.FILES.get('assessmentFile')
            if file == None:
                messages.error(request, 'Please upload a file!')
                html = "/course/importAssessment/%d/" % id
                return HttpResponseRedirect(html)
            else:
                type_excel = file.name.split('.')[1]  # get the type of file
                # print(type_excel)
            if (type_excel == 'xls' or type_excel == 'xlsx'):
                # open the new workbook of excel file
                wb = xlrd.open_workbook(
                    filename=None, file_contents=file.read())
                # logger.info('------------------------')
                sheetNum = len(wb.sheet_names())  # the number of sheets
                for i in range(1, sheetNum):
                    # judge if other sheets contain any data, if so, show the error
                    nrows = wb.sheet_by_index(i).nrows
                    if(nrows > 0):
                        messages.error(
                            request, 'All the data must be contained in first sheet!')
                        html = "/course/importAssessment/%d/" % id
                        return HttpResponseRedirect(html)
                # choose the first sheet as table
                table = wb.sheets()[0]
                nrows = table.nrows  # the number of rows
                # initialize a new course just created
                course = Course.objects.get(CourseID=id)
                # obtain all the assessments according to this course
                cilos = course.cilo_set.all()
                # the number of cilos can not be zero
                ciloNames_list = []
                if cilos.count() == 0:
                    messages.error(
                        request, 'There is no cilo exist!')
                    html = "/course/importAssessment/%d/" % id
                    return HttpResponseRedirect(html)
                else:
                    for cilo in cilos:
                        ciloName = cilo.CILOName
                        ciloNames_list.append(ciloName)
                assessments = course.assessment_set.all()
                total = 0  # check if the total percentage is 100
                if assessments.count() > 0:
                    for assessment in assessments:
                        total += assessment.Percentage
                if nrows <= 1:
                    messages.error(request, 'No data to import')
                    html = "/course/importAssessment/%d/" % id
                    return HttpResponseRedirect(html)
                try:
                    with transaction.atomic():
                        headers = table.row_values(0)
                        headerSet = ['Method Name',
                                     'Percentage', 'CILOIDs']
                        if len(headers) != len(headerSet):
                            messages.error(
                                request, 'The number of headers is wrong!')
                            html = "/course/importAssessment/%d/" % id
                            return HttpResponseRedirect(html)
                        currentYear = datetime.datetime.now().year
                        for i in range(0, len(headerSet)):
                            # judge whether the hearder of file is correct
                            if headers[i] != headerSet[i]:
                                messages.error(
                                    request, 'The header format is wrong!')
                                html = "/course/importAssessment/%d/" % id
                                return HttpResponseRedirect(html)
                        # check whether the header is correct
                        for i in range(1, nrows):
                            # 按行插值
                            for j in range(0, 3):
                                # get the ctype
                                c_type = table.cell(i, j).ctype
                                if j == 0:
                                    if c_type == 1 or c_type == 0:
                                        MethodName = table.cell_value(i, j)
                                    else:
                                        messages.error(
                                            request, 'Data of Method Name is wrong')
                                        html = "/course/importAssessment/%d/" % id
                                        return HttpResponseRedirect(html)
                                if j == 1:
                                    if c_type == 2:
                                        Percentage = table.cell_value(i, j)
                                        total += Percentage
                                        if total > 100:
                                            messages.error(
                                                request, 'The total percentage of methods should less than 100!')
                                            html = "/course/importAssessment/%d/" % id
                                            return HttpResponseRedirect(html)
                                    else:
                                        messages.error(
                                            request, 'Data of Percentage is wrong')
                                        html = "/course/importAssessment/%d/" % id
                                        return HttpResponseRedirect(html)
                                if j == 2:
                                    if c_type == 1:
                                        temp = table.cell_value(i, j)
                                        ciloList = temp.split("-")
                                        print(ciloList)
                                        if set(ciloNames_list) >= set(ciloList):
                                            CILOIDs = table.cell_value(i, j)
                                        else:
                                            messages.error(
                                                request, 'The CILOs must be consisted by the cilos which exits in the course! ')
                                            html = "/course/importAssessment/%d/" % id
                                            return HttpResponseRedirect(html)
                                    else:
                                        messages.error(
                                            request, 'Data Type of CILOIDs is wrong')
                                        html = "/course/importAssessment/%d/" % id
                                        return HttpResponseRedirect(html)
                            Assessment.objects.create(MethodName=MethodName, Percentage=Percentage,
                                                      CILOIDs=CILOIDs, AcademicYear=currentYear, course=course)
                except Exception as e:
                    messages.error(request, 'Error occurs')
                    print('---error---%s' % (e))
                    html = "/course/importAssessment/%d/" % id
                    return HttpResponseRedirect(html)
                messages.success(request, 'The file upload successfully')
                logger.info('%s import the Assessment' % username)
                html = "/course/addciloassessment/%d/" % id
                return HttpResponseRedirect(html)
            messages.error(request, 'The upload file is not .xlsx or .xls')
            html = "/course/importAssessment/%d/" % id
            return HttpResponseRedirect(html)


def visualize(request):
    if (request.session.get('utype', 'none') == 'none'):
        return HttpResponseRedirect('/user/login')
    else:
        if request.method == 'GET':
            utype = request.session.get('utype', 'none')
            if utype == 'CourseDesigner':
                return HttpResponseRedirect('/user/cdMain')
            elif utype == 'NonCourseDesigner':
                return HttpResponseRedirect('/user/ncdMain')
            else:
                return HttpResponseRedirect('/user/stuMain')
        elif request.method == 'POST':
            programme = request.POST.get('programme', 'none')
            logger.info('-------------------------------')
            print(programme)
            if not programme:
                messages.error(
                    request, 'Please input programme!')
                return HttpResponseRedirect('/course/visualize/')
            # try:
            #     courses = Course.objects.values(program=programme)
            # except Exception as e:
            #     messages.error(request, 'There is no course')
            #     return HttpResponseRedirect('user/stuMain')
            else:
                courses = Course.objects.filter(Program=programme)
                nodes = []
                links = []
                for course in courses:
                    # save all the courses as nodes
                    course_dic = {}
                    course_dic['name'] = course.CourseName + '_' + course.Type
                    course_dic['symbolSize'] = 50
                    nodes.append(course_dic)

                    CilosInOneCourse = CILO.objects.filter(
                        course_id=course.CourseID)

                    for cilo in CilosInOneCourse:
                        if (cilo.PreCILO != ""):
                            # print(cilo)
                            temp = cilo.PreCILO
                            res = temp.replace(
                                "[", "").replace("]", "").replace("'", "")
                            precilos = res.split(", ")
                            # print(precilos)
                            for i in precilos:
                                preciloinfo = i.split("-")
                                precourse = Course.objects.get(
                                    Q(CourseName=preciloinfo[0]), Q(Type=preciloinfo[1]))
                                relation_dic = {}
                                relation_dic['source'] = precourse.CourseName + \
                                    '_' + precourse.Type
                                relation_dic['target'] = course.CourseName + \
                                    '_' + course.Type
                                links.append(relation_dic)
                # print(nodes)
                # print(links)
                c = (
                    Graph()
                    .add("", nodes, links, repulsion=8000)
                    .set_global_opts(title_opts=opts.TitleOpts(title="Visualize Dependence", subtitle=programme))
                )
                return HttpResponse(c.render_embed())
