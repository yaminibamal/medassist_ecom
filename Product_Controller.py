from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def Product_Interface(request):
  try:
    admin = request.session['ADMIN']
    return render(request, 'ProductInterface.html')
  except:
    return render(request, 'Login_Page.html')

@xframe_options_exempt
def Submit_Product(request):
    try:
        DB, CMD = Pool.ConnectionPooliing()
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandid = request.POST['brandid']
        productname = request.POST['productname']
        price = request.POST['price']
        offerprice = request.POST['offerprice']
        packingtype = request.POST['packingtype']
        qty = request.POST['qty']
        status = request.POST['status']
        rating = request.POST['rating']
        salestatus = request.POST['salestatus']        
        productimage = request.FILES['productimage']
        Q = "insert into products(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,qty,status,rating,salestatus,productimage) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(
            categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,qty,status,rating,salestatus,productimage.name)
        F = open("C:/Users/Somil/medassist_ecom/assets/" + productimage.name, 'wb')
        for chunk in productimage.chunks():
            F.write(chunk)
            F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'ProductInterface.html', {'message': 'Record Submitted Succesfully'})
    except Exception as e:
        print("Error:", e)
        return render(request, 'ProductInterface.html', {'message': 'Fail to Submit Record'})

@xframe_options_exempt
def Display_All_Products(request):
  try:
    admin = request.session['ADMIN']
  except:
    return render(request, 'Login_Page.html')
  try:
        DB, CMD = Pool.ConnectionPooliing()
        Q = "select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid) as cname,(select S.subcategoryname from subcategories S where P.subcategoryid=S.subcategoryid) as scname,(select B.brandname from brands B where P.brandid=B.brandid) as bname from products P"
        CMD.execute(Q)
        records = CMD.fetchall()
        print('RECORDS:', records)
        DB.close()
        return render(request, 'DisplayAllProducts.html', {'records': records})
  except Exception as e:
        return render(request, 'DisplayAllProducts.html', {'records': None})

@xframe_options_exempt
def Edit_Products(request):
  try:
    DB,CMD=Pool.ConnectionPooliing()
    categoryid = request.GET['categoryid']
    subcategoryid = request.GET['subcategoryid']
    brandid=request.GET['brandid']
    productid=request.GET['productid']
    productname=request.GET['productname']
    price=request.GET['price']
    offerprice=request.GET['offerprice']
    packingtype=request.GET['packingtype']
    qty=request.GET['qty']
    status=request.GET['status']
    salestatus=request.GET['salestatus']
    rating=request.GET['rating']

    Q="update products set categoryid={0},subcategoryid={1},brandid={2},productname='{3}',price={4},offerprice={5},packingtype='{6}',qty={7},status='{8}',salestatus='{9}',rating={10} where  productid={11}".format(categoryid,subcategoryid,brandid,productname,price,offerprice,packingtype,qty,status,salestatus,rating,productid)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Delete_Product(request):
  try:
    DB,CMD=Pool.ConnectionPooliing()
    productid = request.GET['productid']
    Q="delete from products  where  productid={0}".format(productid)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Edit_ProductIcon(request):
  try:
    DB,CMD=Pool.ConnectionPooliing()

    productid = request.POST['productid']
    productimage = request.FILES['producticon']
    Q="update products set productimage='{0}' where  productid={1}".format(productimage.name,productid)
    print(Q)
    F = open("C:/Users/Somil/medassist_ecom/assets/" + productimage.name, 'wb')
    for chunk in productimage.chunks():
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
def Fetch_All_Brands_JSON(request):
    try:
      DB, CMD = Pool.ConnectionPooliing()
      subcategoryid=request.GET['subcategoryid']
      Q = "select * from brands where subcategoryid={0}".format(subcategoryid)
      print("\n\n",Q)
      CMD.execute(Q)
      records = CMD.fetchall()
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return render(request, 'DisplayAllBrands.html', {{'data':None}})

