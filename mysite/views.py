from django.shortcuts import render

from employee.models import Employee

from blog.models import Blog

def home(request):
    employee = Employee.objects.all()
    context = {'emp' : employee}
    return render(request,'home.html',context)

def about(request):
    return render(request,'about.html')

def blog(request):
    blog = Blog.objects.all()
    context = {'bl' : blog}
    return render(request,'blog.html',context)
