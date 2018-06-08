# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

# Create your views here.
from datetime import datetime
from  django.http import HttpResponse
from django.template import loader
import threading
from music.camera import play_video
from models import Students, Log
from music.forms import StudentForm

def index(request):
    dt = datetime.now()
    date = dt.strftime("%Y-%m-%d")
    time = dt.strftime("%H:%M:%S.%f")
    cd = {'out_error':False, 'success':False, 'in_error':False, 'rollno':False}
    if request.method == 'POST':
        s = Students.objects.filter(id=request.POST['refid'])
        # print s
        if len(s)==0:
            cd['rollno']=True
            print 1
        elif request.POST["1"] == "in":
            ls = Log.objects.filter(refid=s)
            # print s[0]
            if len(ls) == 0:
                l = Log(refid=s[0], date=date, in_time=time, out_time=None)
                l.save()
                cd['success'] = True
            else:
                l = ls.filter(out_time=None)
                if len(l) == 0:
                    l = Log(refid=s[0], date=date, in_time=time, out_time=None)
                    l.save()
                    cd['success'] = True
                else:
                    cd['in_error'] = True
        else:
            l = Log.objects.filter(refid=s[0]).filter(out_time=None)
            if len(l)==0:
                cd['out_error'] = True
            else:
                if l[0].out_time is None:
                    l[0].out_time = time
                    l[0].save()
                    cd['success'] = True
                else:
                    cd['out_error']=True
    template = loader.get_template("index.html")
    context=cd
    return HttpResponse(template.render(context, request))

def register(request):
    cd = {'error':False}
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.save()
            print cd
            return redirect('register_train',cd)
    else:
        form = StudentForm()

    return render(request, 'register.html', {
        'form': form
    })


def search(request):
    cd = {}
    cd['error'] = False
    if request.method == "POST":
        cd['id']=request.POST['search-id']
        s = Students.objects.filter(id=cd['id'])
        # print s
        if len(s)==0:
            cd['error'] = True
        else:
            cd['name'] = s[0].name
            cd['image'] = s[0].image
            l = list(Log.objects.values('date','in_time','out_time').filter(refid=cd['id']))
            ls = {}
            for i in l:
                i['date'] = i['date'].strftime("%d-%b-%Y")
                if not ls.has_key(i['date']):
                    ls[i['date']] = []
                intime = i['in_time'].strftime("%I:%M:%S %p")
                if i['out_time']!=None:
                    outtime = i['out_time'].strftime("%I:%M:%S %p")
                else:
                    outtime = "Not yet left"

                ls[i['date']].append([intime,outtime])

            cd['log'] = ls

    template = loader.get_template("search.html")
    context = cd
    return HttpResponse(template.render(context, request))


def postpone(function, args):
    t = threading.Thread(target = function, args=(args,))
    t.daemon = True
    t.start()


def video_feed(request,slug):
    postpone(play_video, slug)
    # return HttpResponse("training the data for id:"+str(slug)+
    #"<a href = index1 >"+"home</a>")
    template = loader.get_template("train.html")
    context = {'id':slug}
    return HttpResponse(template.render(context, request))


def home(request):
    print 'hello',request.method
    return redirect('index')
