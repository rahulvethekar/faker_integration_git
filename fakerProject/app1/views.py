from django.shortcuts import render
from .models import Student
# Create your views here.
def StudentDataView(request):
    obj = Student.objects.all()
    context = {'data':obj}
    template_name = 'student.html'
    return render(request,template_name,context)