from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ageCal(request):
    if request.method=="POST":
        d1 = int(request.POST.get('dd1',''))
        m1 = int(request.POST.get('mm1',''))
        y1 = int(request.POST.get('yy1',''))

        d2 = int(request.POST.get('dd2',''))
        m2 = int(request.POST.get('mm2',''))
        y2 = int(request.POST.get('yy2',''))

        if((d1>31 or d1<1) or (d2>31 or d2<1) or (m1<1 or m1>12) or (m1<1 or m1>12) or (y1<0 and y2<0)):
            # print("You Enter wroung somthing Try Again ...")
            a = f"You Enter wroung somthing Try Again"
            return render(request,'testapp/success.html',a)
        else:
            r3 = y2-y1
        if (d2>=d1):
            r1 = d2-d1
        else:
            m2 = m2-1
            d2 = d2+30
            r1 = d2-d1
        if (m2>=m1):
            r2 = m2-m1
        else:
            r3 = r3-1
            m2 = m2+12
            r2 = m2-m1
        # print(f"You age is {r1} day {r2} month {r3} year ")
        # my_dict = {'days':r1,'month':r2,'year':r3}
        return render(request,'testapp/success.html',{'days':r1,'month':r2,'year':r3})

    return render(request,'testapp/index.html')

# def ageCal_view(request):
#     return render(request,'testapp/success.html')