from django.shortcuts import render
def delta(request):
    return render(request, 'project.html')
def my(request):
    return render(request, 'my.html')
def util(request):
    return render(request, 'util.html')

# Create your views here.
