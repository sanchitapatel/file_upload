from django.shortcuts import render
from app.forms import StudentForm
from app.models import Student

# Create your views here.
def home(request):
    form = StudentForm()
    msg = "Student Registration Page"
    if request.method=='POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg = "Registration succsessfully"
        else:
            msg = "Please enter proper data"

    return render(request,'home.html',{'form':form,'msg':msg})

def show(request):
    data1 = Student.objects.all()
    data = data1.values()
    return render(request,'show.html',{'data':data})