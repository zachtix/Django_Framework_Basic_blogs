from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    # return HttpResponse('<h1>Hello World</h1>')
    tags = ['น้ำตก','ธรรมชาติ','เขา']
    date_list = {'name':'บทความการเที่ยงเที่ยว','author':'Kong','tags':tags}
    return render(request,'index.html',date_list)
