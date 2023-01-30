from django.shortcuts import render,redirect
from .models import *
# Create your views here.



   
def regsuplier(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passw = request.POST.get("pword")
        suplier = request.POST.get('supplier')
        print(username,passw,suplier)
        us = user.objects.create(username = username,password = passw, is_supplier = suplier)
    return render(request,'regs.html')

def regclient(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get("pword")
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        client_id = request.POST.get('cus_id')
        loanid = request.POST.get('loanid')
        print(username,password,fname,lname,email,client_id,loanid)
        us = user.objects.create(username = username,password = password, is_client = 1,first_name = fname,last_name = lname,email = email)
        us.save()
        us_c = client.objects.create(name = us, client_id = client_id,loan_id = loanid)
        us_c.save()
        return redirect('logc')

    return render(request,'regc.html')


from .models import user as u
from django.contrib.auth import authenticate,login
def logc(request):
    if 'login' in request.POST:
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(username=uname, password=pword)

        if user is not None:
            login(request,user)
            print("loged")
            if user.is_supplier:
                print("supplier")
                userid = user.id
                request.session['userid'] = userid
                request.session['is_is'] = "supplier"
                return redirect('home')
            elif user.is_client:
                print("client")
                userid = user.id
                request.session['userid'] = userid
                request.session['is_is'] = "client"
                return redirect('home')
            elif user.is_bank:
                print('bank')
                userid = user.id
                request.session['userid'] = userid
                request.session['is_is'] = "bank"
                return redirect('home')
        elif user is None:
            try:
                a = u.objects.get(username = uname)
                if a.password == pword:
                    login(request,a)
                    if a.is_bank:
                        userid = a.id
                        request.session['userid'] = userid
                        request.session['is_is'] = "bank"
                        return redirect('home')

                    elif a.is_supplier:
                        print("sup")
                        userid = a.id
                        request.session['userid'] = userid
                        request.session['is_is'] = "supplier"
                        return redirect('home')
                    else:
                        userid = a.id
                        request.session['userid'] = userid
                        request.session['is_is'] = "client"
                        return redirect('home')
                        
                else:
                    print('password not match')

            except Exception as e:
                print(e)
                print('UNKNOWN ERROR')
                
        else:
            print('NO user found')
        
    a = u.objects.all()        
    return render(request,'logc.html',{'datas':a})      


def enter(request):

    return render(request,'enter.html')

def home(request):
    isis = request.session['is_is']
    print(isis)




    if isis == 'client':
        userid = request.session['userid']
    

        if userid is not None:

            user_object = u.objects.get(id = userid)
            user_client = client.objects.get(name = user_object)
            ci = user_client.client_id
            ap_data = approved_invoice.objects.filter(cus_id =ci)
            print(ap_data)

            if 'Casloan' in request.POST:
                return render(request,'home.html',{"user":user_object,"userc":user_client,"app_in":ap_data,'isis':isis,"edit" :True})
            return render(request,'home.html',{"user":user_object,"userc":user_client,"app_in":ap_data,'isis':isis})
    
    elif isis == 'bank':
        if userid is not None:
            user_object = user.objects.get(id = userid)
            user_supplier = suplier.objects.get(name = user_object)
            ap_data = approved_invoice.objects.all()
            req_data = request_invioce.objects.all()
        return render(request,'home.html',{'isis':isis,"user":user_object,'users':user_supplier,'re_data':req_data})
    
   

    elif isis == 'supplier':
        userid = request.session['userid']
        user = u.objects.get(id = userid)
        if 'submitre' in request.POST:
            cname = request.POST.get('clientname')
            amount = request.POST.get('amount')
            approved_by = request.POST.get('ap_by')
            customer_id =  request.POST.get('cusid')
            supplier_id = request.POST.get('supid')
            print(cname,amount,approved_by,customer_id,supplier_id)
            print(cname)
            
            
            
            approve = approved_invoice.objects.create(amount = amount,cus_id = customer_id, client_id = 1223,sup_id = supplier_id,approved_by = user.username)
            approve.save()
            print("saved")
        elif "subde" in request.POST:
            print("deny")

        
    










        userid = request.session['userid']
        print(userid)
        if userid is not None:
            user_object = u.objects.get(id = userid)
            print(user_object)
            user_supplier = suplier.objects.get(name = user_object)
            ap_data = approved_invoice.objects.all()
            req_data = request_invioce.objects.all()
            print(req_data)
        return render(request,'home.html',{'isis':isis,"user":user_object,'users':user_supplier,'re_data':req_data})  
        
    
    else:    
        return render(request,'home.html',{'isis':'GUEST'})