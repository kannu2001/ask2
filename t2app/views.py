from django.shortcuts import render
from t2app.models import course
from django.db.models import Q
# from .models import Box

# def filter_boxes(request):
#     location_filter = request.GET.get('location', 'all_locations')
    
#     if location_filter == 'all_locations':
#         boxes = Box.objects.all()
#     else:
#         boxes = Box.objects.filter(location=location_filter)

#     return render(request, 'index.htm


def search(request):
    context={}
    query=request.GET['query']
    #print(query)
    pname=course.objects.filter(name__icontains=query)
    pdetail=course.objects.filter(cdetail__icontains=query)
    pcat=course.objects.filter(cat__icontains=query)
    allproducts=pname.union(pdetail,pcat)
    if allproducts.count()==0:
        context['errmsg']='Products Not Found'
    context['data']=allproducts
    return render(request,'base.html',context)

def all(request):
    p=course.objects.filter(is_active=True)
    context={}
    context['data']=p
    return render(request,'base.html',context)

def catfilter(request,cv):
    print(cv)
    q1=Q(cat=cv)
    q2=Q(is_active=True)

    p=course.objects.filter(q1 & q2)

    context={}
    context['data']=p
    return render(request,'base.html',context)

def locfilter(request,vc):
    print(vc)
    q1=Q(lc=vc)
    q2=Q(is_active=True)

    p=course.objects.filter(q1 & q2)

    context={}
    context['data']=p
    return render(request,'base.html',context)

