from django.shortcuts import render  
from myapp.form import EmployeeForm  
from django.template import loader
from django.http import HttpResponse  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})


def index(request):  
    template = loader.get_template('index2.html') # getting our template  
    return HttpResponse(template.render())       # rendering the template in HttpResponse  
