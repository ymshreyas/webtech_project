from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import DatabaseError
from django.http import HttpResponseRedirect
from webtech_app.models import user_info,plot_info
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from webtech_app import moving_avg,futures,MACD,Bollinger_bands
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import datetime
# Create your views here.
    
def child1_view(request):
    return render(request,'webtech_app/Bollinger.html')

def child2_view(request):
    return render(request,'webtech_app/MA.html')

def child3_view(request):
    return render(request,'webtech_app/MACD.html')

def child4_view(request):
    return render(request,'webtech_app/MACD2.html')

def landing(request):
    return render(request,'webtech_app/landing.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        exists = user_info.objects.filter(email=email,password=password)
        user = authenticate(username=email,password=password)
        if(user is not None and exists):
            login(request,user)
            return redirect('first')
        else:
            messages.success(request,'Invalid email or password, try again')
            return redirect('user_login')
    else:
        return render(request,'webtech_app/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing'))

def signup(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            retype_password = request.POST['retype_password']
            encrypted_password = make_password(password)
            if(password==retype_password):
                obj = user_info(email=email,password=password) 
                user = User(username=email,password=encrypted_password)
                obj.save()
                user.save()
                messages.success(request,"Resgistration Successful, you may close this tab now")
                return redirect('signup')
            else:
                messages.success(request,"Passwords do not match, try again")
                return redirect('signup')
        else:
            return render(request,'webtech_app/sign_up.html')
    except DatabaseError:
        messages.success(request,'Email already taken')
        return redirect('signup')
   

def generate(request):
    try:
        if request.method == 'POST':
            user_name = request.user.username
            analysis_type = request.POST['analysis_type']
            period1 = request.POST['Period1']
            period2 = request.POST['Period2']
            period3 = request.POST['Period3']
            period1 = int(period1)
            period2 = int(period2)
            period3 = int(period3)
            if(period1<0 or period2<0 or period3<0):
                messages.success(request,"Invalid input type, fill in the correct periods")
                return redirect('generate')
            select1 = request.POST['select1']
            select2 = request.POST['select2']
            select3 = request.POST['select3']
            start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()
            if start_date > timezone.now().date() or end_date > timezone.now().date():
                messages.success(request, "Start date or end date cannot be in the future")
                return redirect('generate')
            if end_date < start_date:
                messages.success(request, "End date cannot be before start date")
                return redirect('generate')
            select = select1+" "+select2
            str_start_date = str(start_date)
            str_end_date = str(end_date)
            if(analysis_type == 'MACD'):
                MACD.run((select, select3, [period1,period2,period3], str_start_date, str_end_date))
            elif analysis_type == 'MOV_AVG':
                moving_avg.run((select, select3, [period1,period2,period3], str_start_date, str_end_date))
            elif analysis_type == 'BOLLINGER':
                l = [period1,period2,period3]
                for x in l:
                    if x!=0:
                        period = x
                        break
                Bollinger_bands.run((select, select3, period, str_start_date, str_end_date))
            obj = plot_info(user_name=user_name,period1=period1,period2=period2,period3=period3,select1=select1,select2=select2,select3=select3,start_date=start_date,end_date=end_date,analysis_type=analysis_type)
            obj.save()
            return redirect('generate')
        else:
            return render(request,'webtech_app/select.html')
    except ZeroDivisionError or UnboundLocalError or ValueError:
        messages.success(request,"Fill in all the period fields with non zero positive numbers(for MACD)")
        return redirect('generate')
    
def first(request):
    user_name = request.user.username
    plot = plot_info.objects.filter(user_name=user_name)
    if(len(plot)==0):
        return render(request,'webtech_app/first_page.html',{'plot':0})
    else:
        return render(request,'webtech_app/first_page.html',{'plot':plot})
    