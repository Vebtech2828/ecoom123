from django.shortcuts import render
from django.http import HttpResponse
from paytm1.models import Employee
# Create your views here.

def study11(request):
    return HttpResponse ("<h1> Hello Vaibhav How are You !!</h1>")

def home_view(request):
    return render(request,'paytm1/home.html')

def Paytm_News_view(request):
    news1 = 'Paytm Aquires new Ecom TCS : Vijay Maliya'
    news2 = 'Lots of vacamncy are available in Paytm'
    news3 = 'Paytm Aquires Google'
    news4 = 'Paytm is not paytms : Vijay Maliya'
    news5 = 'Salman is going to marry soon : Vijay Maliya'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'paytm1/pnews.html',my_dict)

def Employee_info_view(request):
    employees =Employee.objects.all()
    return render(request,'paytm1/results.html',{'employees': employees})