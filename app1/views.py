import re
from django.shortcuts import render, redirect
from  django.http import HttpResponse, Http404,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import user , stocks
import bcrypt
from nsetools import Nse; nse_exchange = Nse()
from bsedata.bse import BSE; bse_exchange = BSE()
# Create your views here.

def logout(request):
    # if (request.method == 'POST'):
    #     if (request.POST.get('logout')):
    #         del request.session['user_logged']
    #         return redirect('/app1/user/')

    # else:
    try:
        # print("\n\n", request.POST.get('logout'),"\n\n")
        del request.session['user_logged']
        return redirect('/app1/user/')
    except:
        return redirect('/app1/user/')


    
def User(request):
    if (request.method == 'POST'):
        # if (request.POST.get('logout')):
        #     del request.session['user_logged']
        try:
            request.POST['sign_up']
            # print ("\nprint working \n",(request.POST['sign_up']))
            details = request.POST
            user_email = str(details.get('user_email'))
            user_pass = details.get('user_pass');
            try:
                user.objects.get(user_email=user_email)
                flag = 1
            except:
                hashed = bcrypt.hashpw(bytes(user_pass, 'utf-8'), bcrypt.gensalt(14))
        # print(f"\n\nHASHED PASS EDIT : {hashed.decode()}\nNO EDIT : {hashed}\n\n")
                send_data = user.objects.create(user_email=user_email, user_pass=hashed.decode())
                return HttpResponse(f'user_email : {user_email}\n user_pass : {user_pass}')
            if (flag):
                return HttpResponse(f'user already exists')
        except:
            user_email = str(request.POST['user_email'])
            user_pass = request.POST.get('user_pass'); 
            try:
                user.objects.get(user_email=user_email)
                flag = 1
            except:
                return HttpResponse("user does not exists")
            if (flag):
                # print(f"{user.objects.get(user_email=user_email).user_pass}")
                if (bcrypt.checkpw(bytes(user_pass, 'utf-8'), bytes(user.objects.get(user_email=user_email).user_pass, 'utf-8'))):
                    request.session['user_logged'] = user_email
                    return redirect('/app1/stocks/')
                else:
                    return HttpResponse("wrong pass")
    else:
        if ('user_logged' in request.session):
            return redirect('/app1/stocks/')
        else:    
            return render(request, 'app1/user.html')

        



    
def stock(request):
    if ('user_logged' in request.session):
        # return HttpResponse(f"session exists user_email : {request.session['user_logged']}")
        user_logged = stocks.objects.filter(user_email = request.session['user_logged']).all()
        for y in user_logged:
            try:
                # y.code = int(y.code)
                y.yesterday_price = nse_exchange.get_quote(y.code)['previousClose']
                y.today_price = nse_exchange.get_quote(y.code)['lastPrice']
                y.save()
            except:
                y.yesterday_price = bse_exchange.getQuote(y.code)['previousClose']
                y.today_price = bse_exchange.getQuote(y.code)['currentValue']
                y.save()

        # print('\n\n',user_logged.today_price,'\n\n') 
       
        context = {'data' : user_logged, 'message' : f"Welcome {request.session['user_logged']}"}
        # print("\n\n",nse_exchange.get_quote(context['data'].code),"\n\n")
        return render(request, 'app1/stocks.html', context=context)

    else:
        return redirect('/app1/user/')


def addStock(request):
    if (request.method == 'POST' and 'user_logged' in request.session):
        obj0 = user.objects.filter(user_email = request.session['user_logged']).all()[0]
        try:
            bse_code = request.POST['scrip_name']
            details = bse_exchange.getQuote(bse_code)
            obj = stocks(qty=request.POST['qty'],user_email = obj0, exchange = "BSE", code=bse_code, purchase_price 
            = request.POST['purchase_price'], stock = details['companyName'], today_price = details['currentValue'], yesterday_price=
            details['previousClose'])
            obj.save()
            return redirect ('/app1/stocks')
        except:
            try:
                nse_code = request.POST['scrip_name']
                details = nse_exchange.get_quote(nse_code)
                obj = stocks(qty=request.POST['qty'],user_email = obj0, exchange = "NSE", code=nse_code, purchase_price 
                = request.POST['purchase_price'], stock = details['companyName'], today_price = details['lastPrice'], yesterday_price=
                details['previousClose'])
                obj.save()
                return redirect ('/app1/stocks')
            except:
                context = {'message' : "please enter valid info without spaces."}
                return render(request, 'app1/stocks.html', context=context)




    else:
        if('user_logged' in request.session):
            return render(request,'app1/stockadd.html')
        else:
            return redirect('/app1/user/')

