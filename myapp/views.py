from django.shortcuts import render

from django.http import HttpResponse
from .models import Order

from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404

from django.shortcuts import render

def write_result(request):

    return HttpResponse("HI")

# Create your views here.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    course_list = Course.objects.all().order_by('-price')[:5]
    return render(request, 'myapp/index0.html', {'top_list': top_list, 'course_list': course_list})


def about(request):
    return render(request, 'myapp/about0.html')

def  detail(request, top_no):
    #topic=get_object_or_404(Topic, pk=top_no)
    topic= Topic.objects.get(id=top_no)
    #get_object_or_404(topic, pk=1)
    course_list = Course.objects.filter(topic=Topic.objects.get(id=top_no))            
    return render(request, 'myapp/detail0.html', {'topic': topic, 'course_list': course_list})
