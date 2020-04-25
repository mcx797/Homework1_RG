from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import *
from django.db.models import Max
from django.utils import timezone 

contex = {}

def mi(a):
        return a

def hello(request):
        return render(request, 'hello.html')

def To_Register(request):
        return render(request, "register.html")

def Return_Login(request):
        return render(request, "hello.html")

def register(request):
        if 'usr_name' in request.GET and 'usr_password' in request.GET and 'usr_password_Again' in request.GET and'power' in request.GET and 'laboratory' in request.GET:
                if len(usr_t.objects.filter(usr_name=request.GET['usr_name'])) == 0:
                        if request.GET['usr_password'] != "" and  request.GET['usr_name'] != "":
                                if request.GET['power'] == "1" and request.GET['usr_password'] != "17373019":
                                        return HttpResponse("你无权注册")
                                if request.GET['usr_password_Again'] == request.GET['usr_password']:
                                        usr_t(usr_name=request.GET['usr_name'], usr_password=mi(request.GET['usr_password']),
                                                power=request.GET['power'],laboratory = request.GET['laboratory']).save()
                                        return render(request, 'success.html')
                                else:
                                        return HttpResponse("请确保两次输入密码一致")
                else:
                        return HttpResponse("已经存在该用户")
                
                return render(request, 'hello.html')
        else:
                return HttpResponse("有未填的值") 
        return HttpResponse("注册失败") 

def success(request):
        return render(request, 'hello.html')

def item_list(lab, power):
        item = []
        my_device = device.objects.all()
        for i in my_device:
                if power == 1 or i.laboratory == lab:
                        s_name = i.device_name
                        g_name = i.device_time
                        a = {}
                        a["goods_name"] = s_name
                        a["stick_name"] = g_name
                        a["stick_id"] = i.id
                        a["buy_name"] = i.buy_name
                        a["lab"] = i.laboratory
                        item.append(a)
        return item

def item_list_name(string1, lab, power):
        item = []
        my_device = device.objects.all()
        for i in my_device:
                if string1 in i.device_name:
                        if power == 1 or i.laboratory == lab:
                                s_name = i.device_name
                                g_name = i.device_time
                                a = {}
                                a["goods_name"] = s_name
                                a["stick_name"] = g_name
                                a["stick_id"] = i.id
                                a["buy_name"] = i.buy_name
                                a["lab"] = i.laboratory
                                item.append(a)
        return item 


def item_list_id(string1, lab, power):
        item = []
        my_device = device.objects.all()
        for i in my_device:
                if string1 == str(i.id):
                        if power == 1 or i.laboratory == lab:
                                s_name = i.device_name
                                g_name = i.device_time
                                a = {}
                                a["goods_name"] = s_name
                                a["stick_name"] = g_name
                                a["stick_id"] = i.id
                                a["buy_name"] = i.buy_name
                                a["lab"] = i.laboratory
                                item.append(a)
        return item 



def login(request):
        if 'usr_name' in request.GET and 'usr_password' in request.GET:
                try:
                        usr = usr_t.objects.get(usr_name =request.GET['usr_name'])
                        if usr.usr_password == request.GET['usr_password']:
                                contex['usr_name'] = request.GET['usr_name']
                                contex['n_news'] = 0
                                contex["lab"] = usr.laboratory
                                if usr.power == 0:
                                        contex['power'] = "普通用户"
                                else:
                                        contex['power'] = "管理员"
                                contex['item_list'] = item_list(usr.laboratory, usr.power)
                                return render(request, 'main.html', contex)
                        else:  
                                return HttpResponse("密码错误")
                except:
                        return HttpResponse("请先注册")
        else:
                return HttpResponse("有未填的值")


def Login_Out(request):
    return render(request,'hello.html',contex)

def i_project(request):
    return render(request, 'project.html', contex)

def project(request):
        global project_id
        global stick_id
        if len(device.objects.all()) == 0:
                idd = 1
        else:
                idd = device.objects.latest('id').id + 1
        if 'project_name' in request.GET and 'usr_name' in request.GET and 'laboratory' in request.GET:
                device(id = idd, device_name = request.GET['project_name'], buy_name = request.GET['usr_name'],device_time = timezone.now(),laboratory = request.GET['laboratory']).save()
        return render(request, 'main.html', contex)

def to_appointment(request):
        if "stick_id" in request.GET:
                print(request.GET['stick_id'])
                contex["ss_id"] = request.GET['stick_id']
                contex["appoint"] = ""
        return render(request, 'Appointment.html', contex)

def back(request):
        return render(request, "main.html", contex)

def search(request):
        if "contents" in request.GET and "identify" in request.GET:
                usr = usr_t.objects.get(usr_name = contex['usr_name'])
                if request.GET["identify"] == "name":
                        s = request.GET["contents"]
                        contex['item_list'] = item_list_name(s,usr.laboratory, usr.power)
                else:
                        s = request.GET["contents"]
                        contex['item_list'] = item_list_id(s, usr.laboratory, usr.power)
        return render(request, "main.html", contex)


def appoint1(request):
        if "button1" in request.GET:
                id_ap = contex["ss_id"]
                year1 = request.GET["YYYY"]
                month1 = request.GET["MM"]
                day1 = request.GET["DD"]
                time1 = request.GET["identify"]
                item = []
                timenum = []
                for i in range(14):
                        if len(appoint.objects.filter(year = year1, month = month1, day = day1, hour = i + 7, device_id = contex["ss_id"])) == 0:
                                timenum.append("0")
                        else:
                                timenum.append("1")
                for i in range(14):
                        aaa = {}
                        aaa["time"] = str(i + 7)
                        aaa["time1"] = str(i + 8)
                        #print(i)
                        #print(timenum[i])
                        aaa["Is"] = timenum[i]
                        item.append(aaa)
                contex["time"] = item
                contex["appoint"] = ""
                return render(request, 'Appointment.html', contex)
        if "button2" in request.GET:
                year1 = request.GET["YYYY"]
                month1 = request.GET["MM"]
                day1 = request.GET["DD"]
                time1 = request.GET["identify"]
                if len(appoint.objects.all()) == 0:
                        idd = 1
                else:
                        idd = appoint.objects.latest('id').id + 1
                if len(appoint.objects.filter(year = year1, month = month1, day = day1, hour = time1, device_id = contex["ss_id"])) == 0:
                        contex["appoint"] = "预约成功"
                        appoint(id = idd, usr_name = contex["usr_name"], year = year1, month = month1, day = day1, hour = time1, device_id = contex["ss_id"]).save()
                else:
                        contex["appoint"] = "预约失败"
                return render(request, 'Appointment.html', contex)