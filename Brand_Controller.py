from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def Brand_Interface(request):
  try:
    admin = request.session['ADMIN']
    return render(request, 'BrandInterface.html')
  except:
    return render(request, 'Login_Page.html')
@xframe_options_exempt
def Submit_Brand(request):
    try:
        DB, CMD = Pool.ConnectionPooliing()

        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandname = request.POST['brandname']
        contactperson = request.POST['contactperson']
        mobileno = request.POST['mobileno']
        status = request.POST['status'] 
        logo = request.FILES['logo']
        Q = "insert into brands(categoryid,subcategoryid,brandname,contactperson,mobileno,status,logo) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(
            categoryid,subcategoryid,brandname,contactperson,mobileno,status,logo.name)
        print("somil")
        F = open("C:/Users/Somil/medassist_ecom/assets/" + logo.name, 'wb')
        for chunk in logo.chunks():
            F.write(chunk)
        F.close()

        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'BrandInterface.html', {'message': 'Record Submitted Succesfully'})
    except Exception as e:
        print("Error:", e)
        return render(request, 'BrandInterface.html', {'message': 'Fail to Submit Record'})

@xframe_options_exempt
def Display_All_Brands(request):
  try:
    admin = request.session['ADMIN']
  except:
    return render(request, 'Login_Page.html')
  try:
        DB, CMD = Pool.ConnectionPooliing()
        Q = "select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cname,(select S.subcategoryname from subcategories S where B.subcategoryid=S.subcategoryid) as scname from brands B"
        CMD.execute(Q)
        records = CMD.fetchall()
        print('RECORDS:', records)
        DB.close()
        return render(request, 'DisplayAllBrands.html', {'records': records})
  except Exception as e:
        return render(request, 'DisplayAllBrands.html', {'records': None})

@xframe_options_exempt
def Edit_Brands(request):
  try:
    print("\nsomil yadav\n")
    DB,CMD=Pool.ConnectionPooliing()
    categoryid = request.GET['categoryid']
    subcategoryid = request.GET['subcategoryid']
    brandid=request.GET['brandid']
    brandname=request.GET['brandname']
    contactperson=request.GET['contactperson']
    mobileno=request.GET['mobileno']
    status=request.GET['status']
   
    Q="update brands set categoryid={0},subcategoryid={1},brandname='{2}',contactperson='{3}',mobileno={4},status='{5}' where  brandid={6}".format(categoryid,subcategoryid,brandname,contactperson,mobileno,status,brandid)
    print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Delete_Brand(request):
  try:
    DB,CMD=Pool.ConnectionPooliing()
    brandid = request.GET['brandid']
    Q="delete from brands  where  brandid={0}".format(brandid)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Edit_BrandIcon(request):
  try:
    DB,CMD=Pool.ConnectionPooliing()
    brandid = request.POST['brandid']
    logo = request.FILES['logo']
    Q="update brands set logo='{0}' where  brandid={1}".format(logo.name,brandid)
    print(Q)
    F = open("C:/Users/Somil/medassist_ecom/assets/" + logo.name, 'wb')
    for chunk in logo.chunks():
      F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Fetch_All_SubCategory_JSON(request):
    try:
      DB, CMD = Pool.ConnectionPooliing()
      categoryid=request.GET['categoryid']
      Q = "select * from subcategories where categoryid={0}".format(categoryid)
      CMD.execute(Q)
      records = CMD.fetchall()
      print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return render(request, 'DisplayAllSubCategories.html', {{'data':None}})

