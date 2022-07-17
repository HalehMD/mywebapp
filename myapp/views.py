from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Order

from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404
from .forms import InterestForm, OrderForm
#from myapp import forms
from django.shortcuts import render

def write_result(request):

    return HttpResponse("HI")

# Create your views here.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    course_list = Course.objects.all().order_by('-price')[:5]
    return render(request, 'myapp/index.html', {'top_list': top_list, 'course_list': course_list})


def about(request):
    return render(request, 'myapp/about.html')

def  detail(request, top_no):
    #topic=get_object_or_404(Topic, pk=top_no)
    topic= Topic.objects.get(id=top_no)
    #get_object_or_404(topic, pk=1)
    course_list = Course.objects.filter(topic=Topic.objects.get(id=top_no)) 
    #course_list = topic.Course.all()   
    return render(request, 'myapp/detail.html', {'topic': topic, 'course_list': course_list})


def courses(request):
    courlist = Course.objects.all().order_by('id')
    return render(request, 'myapp/courses.html', {'courlist': courlist})

def  place_order(request):
    msg = ''
    courlist = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            level= form.cleaned_data['levels']
            courname = form.cleaned_data['course']
            #if order.levels <= order.course.stages:
            if order.levels <= order.course.stages:
                print(courname)
                print(level)
                order.save()
                distcourse=Course.objects.get(name=courname)
                if distcourse.price > 150:
                    distcourse.discount()
                msg = 'Your course has been ordered successfully.'
            else:
                msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myapp/order_response.html', {'msg': msg}) 
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form':form, 'msg':msg, 'courlist':courlist})

def  coursedetail(request, cour_id):
    course = get_object_or_404(Course, id=cour_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.cleaned_data['interested']
            #levels = form.cleaned_data['levels']
            print(interest)
            print(course)
            if interest:
                course.interested += 1
                course.save()
            return HttpResponseRedirect(reverse('myapp:index'))
        else:
            print("chek")    
    else:
        print('------------------GET')
        form = InterestForm()
    #courdetails = get_object_or_404(Course, id=cour_id)
    return render(request, 'myapp/coursedetail.html', {'InterestForm':form, 'courdetails':course})