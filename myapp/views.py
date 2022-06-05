from django.shortcuts import render

from django.http import HttpResponse
<<<<<<< HEAD
from .models import Order

def write_result(request):

    return HttpResponse("HI")

=======
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    course_list = Course.objects.all().order_by('-price')[:5]
    response = HttpResponse()
    heading1 = '<h2>' + 'List of topics: ' + '</h2>'
    response.write(heading1)
    for topic in top_list:
        para = '<p>'+ str(topic.id) + ': ' + str(topic) + '</p>'
        response.write(para)
    
    heading2 = '<h2>' + 'List of Courses: ' + '</h2>'
    response.write(heading2)
    for course in course_list:
        if(course.for_everyone == True):
            para = '<p>'+ str(course.id) + ': ' + str(course) +' -- ' + ' This Course is For Everyone!' +'</p>'
            response.write(para)
        else:
            para = '<p>'+ str(course.id) + ': ' + str(course) +' -- ' + ' This Course is Not For Everyone!' +'</p>'
            response.write(para)
    
    return response

def about(request):
    response = HttpResponse()
    heading1 = '<h2>' + 'This is an E-learning Website! Search our Topics to find all available Courses. ' + '</h2>'
    response.write(heading1)
    
    return response
>>>>>>> ac7428666852ee7ea856ece741f5b1c0632727c5

def  detail(request, top_no):
    topic=get_object_or_404(Topic, pk=top_no)
    #topic= Topic.objects.get(id=top_no)
    #get_object_or_404(topic, pk=1)
    course_list = Course.objects.filter(topic=Topic.objects.get(id=top_no))
    response = HttpResponse()
    heading1 = '<h2>' + 'Topic name: ' + str(topic) + '</h2>'
    heading2 = '<h2>' + 'Category: ' + str(topic.category) + '</h2>'
    response.write(heading1)
    response.write(heading2)
    
    for course in course_list:
        para = '<p>'+ str(course.id) + ': ' + str(course) +'</p>'
        response.write(para)
            
    return response