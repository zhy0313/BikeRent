from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django import forms 
from django.contrib.auth import authenticate
# Create your views here.
from models import Person,Order,Bike

import time
import datetime


class PersonSignUpForm(forms.Form):
    PersonName = forms.CharField()
    PersonPassWord = forms.CharField()
    PersonGender = forms.CharField()
    PersonPhone = forms.CharField()
class PersonSignInFrom(forms.Form):
    PersonName = forms.CharField()
    PersonPassWord = forms.CharField()
class OrderFrom(forms.Form):
    BikeType = forms.CharField()
class ReturnFrom(forms.Form):
    BikeType = forms.CharField()

def index(rep):
    return render_to_response('index.html')
def signup(req):
    if req.method == 'POST':
        P_Form = PersonSignUpForm(req.POST)
        if P_Form.is_valid():
            person = Person()
            person.PersonName = P_Form.cleaned_data['PersonName']
            person.PersonPassWord = P_Form.cleaned_data['PersonPassWord']
            person.PersonGender = P_Form.cleaned_data['PersonGender']
            person.PersonPhone = P_Form.cleaned_data['PersonPhone']
            person.PersonStatus = 1
            person.AccountPayable = 0.0
            person.IsAdmin = 0
            if Person.objects.filter(PersonName = person.PersonName):
                return HttpResponse('User is EXIST')
            else:
                person.save()
                return HttpResponseRedirect('/Bike/')
    else:
        P_Form = PersonSignUpForm()
    return render_to_response('signup.html',{'Form':P_Form})

def signin(req):
    if req.method == 'POST':
        P_Form = PersonSignInFrom(req.POST)
        if P_Form.is_valid():
            
            Name = P_Form.cleaned_data['PersonName']
            PassWord = P_Form.cleaned_data['PersonPassWord']
            person = Person.objects.filter(PersonName = Name,PersonPassWord = PassWord)
            if person:
                req.session['PersonName'] = Name
                return HttpResponseRedirect('/Bike/person/')
            else:
                return HttpResponse('Error Please check Name or Password')
    else:
        P_Form = PersonSignInFrom()
    return render_to_response('signin.html',{'Form':P_Form})
def signout(req):
    del req.session['PersonName']
    return render_to_response('signout.html')

def person(req):
    Name = req.session.get('PersonName','EveryBody')
    if Name:
        person = Person.objects.get(PersonName = Name)
        
        
        list_order = Order.objects.filter(OrderPersonID = person).order_by('-OrderStartTime')
        list_order_temp = []
        list_StartTime = []
        list_EndTime = []
        for n in range(len(list_order)):
            name = list_order[n].OrderPersonID.PersonName
            bike = list_order[n].OrderBikeID.BikeType
            pay = list_order[n].OrderAccountPayable
            
            StartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(list_order[n].OrderStartTime)))
            list_StartTime.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(list_order[n].OrderStartTime))))
            if float(list_order[n].OrderEndTime) != 0:
                endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(list_order[n].OrderEndTime)))
            else:
                endTime = 0
            
            order_temp = {'Name':name,'Bike':bike,'StartTime':StartTime,'EndTime':endTime,'Payable':pay}
            list_order_temp.append(order_temp)
        
        
        return render_to_response('person.html',{'Person':person,'list_order_temp':list_order_temp,'List_order':list_order,'list_StartTime':list_StartTime,'list_EndTime':list_EndTime})
    else:
        return HttpResponse('Error, please SignIn again')

def rentbike(req):
    Name = req.session.get('PersonName')
    if Name:
        person = Person.objects.get(PersonName = Name)
        if person.IsAdmin == 1:
            return HttpResponse('Exist Order,Please Return Bike')
        else:
            list_bike = Bike.objects.filter(BikeStatus = 0)
            if req.method == 'POST':
                O_Form = OrderFrom(req.POST)                           
                if O_Form.is_valid():
                    biketype = O_Form.cleaned_data['BikeType']
                    bike = Bike.objects.get(BikeType = biketype)
                    
                    order = Order()
                    order.OrderPersonID = person
                    order.OrderBikeID = bike
                    order.OrderStartTime = time.time()
                    order.OrderEndTime = 0
                    order.OrderAccountPayable = 0
                    order.save()
                    
                    person.IsAdmin = 1
                    bike.BikeStatus = 1
                    person.save()
                    bike.save()
                    return HttpResponseRedirect('/Bike/person/')

                else:
                    return HttpResponse('Bike choice Error,Again')
            else:
                O_Form = OrderFrom()
            return render_to_response('rentbike.html',{'Form':O_Form,'List_Bike':list_bike,'Name':person.PersonName})

def returnbike(req):
    Name = req.session.get('PersonName')
    if Name:
        person = Person.objects.get(PersonName = Name)
        if person.IsAdmin == 0:
            return HttpResponse('No Exist Order,Please Rent Bike')
        else:
            ReturnOrder = Order.objects.get(OrderPersonID = person,OrderEndTime = 0)
            StartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(ReturnOrder.OrderStartTime)))
            if req.method == 'POST':
                O_Form = ReturnFrom(req.POST)                           
                if O_Form.is_valid():
                    biketype = O_Form.cleaned_data['BikeType']
                    bike = Bike.objects.get(BikeType = biketype)
                    
                    ReturnOrder.OrderEndTime = time.time()
                    startTime = ReturnOrder.OrderStartTime
                    endtime = ReturnOrder.OrderEndTime
                    if int(int(float(endtime) - float(startTime))/3600) > 24:
                        ReturnOrder.OrderAccountPayable = (int(int(float(endtime) - float(startTime))/3600)+1) * bike.BikeUnitPrice + 100
                    else:
                        ReturnOrder.OrderAccountPayable = (int(int(float(endtime) - float(startTime))/3600)+1) * bike.BikeUnitPrice
                    ReturnOrder.save()
                    
                    person = ReturnOrder.OrderPersonID
                    person.IsAdmin = 0
                    orderbike = ReturnOrder.OrderBikeID
                    orderbike.BikeStatus = 0
                    person.save()
                    orderbike.save()
                    return HttpResponseRedirect('/Bike/person/')

                else:
                    return HttpResponse('Bike choice Error,Again')
            else:
                O_Form = OrderFrom()
            return render_to_response('returnbike.html',{'Form':O_Form,'RetrunOrder':ReturnOrder,'StartTime':StartTime})
                   
                    
            
            
        
        
        
    
    
    