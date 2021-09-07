from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    tags_list = ['น้ำตก','ธรรมชาติ','เขา']
    date_list = {
        'name':'บทความการเที่ยงเที่ยว','author':'Kong',
        'tags':tags_list,
        'rating':2
        }
    return render(request,'index.html',date_list)

def page1(request):
    return render(request, 'page1.html')