from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt

def Login_Interface(request):
  try:
    admin = request.session['ADMIN']
    return render(request, 'Dashboard.html',{'records':admin})
  except:
    return render(request, 'Login_Page.html')

def Admin_Logout(request):
    del request.session['ADMIN']
    return render(request,"Login_Page.html")

def Login_Varification(request):
  try:
    DB,CMD=Pool.ConnectionPooliing()
    email=request.POST['email']
    pswrd=request.POST['password']
    Q="select * from adminlogin where email='{0}' ".format(email)
    CMD.execute(Q)
    records=CMD.fetchone()
    DB.close()
    print(records)
    if(records['password']==pswrd):
      request.session['ADMIN']=records
      return render(request, 'Dashboard.html',{'records':records})
    else:
      return render(request, 'Login_Page.html', {'message': 'invalid password'})
  except Exception as e:
      print("Error:",e)
      return render(request, 'Login_Page.html', {'message': 'Invalid Login'})

def Dashboard_Interface(request):
    return render(request,'Dashboard.html')