from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
import json
from urllib.parse import unquote

def Signin(request):
    return render(request, "User_Registration.html")

def AddToCart(request):
    try:
        product = request.GET['product']
        qty = request.GET['qty']
        product = product.replace("'", "\"")
        product = json.loads(product)
        product['qty'] = qty
        # create cart container using Session
        try:
            CART_CONTAINER = request.session['CART_CONTAINER']
            CART_CONTAINER[str(product['productid'])] = product
            request.session['CART_CONTAINER'] = CART_CONTAINER
        except:
            CART_CONTAINER = {}
            CART_CONTAINER[str(product['productid'])] = product
            request.session['CART_CONTAINER'] = CART_CONTAINER
        CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
        return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        return JsonResponse({'data': []}, safe=False)

def FetchCart(request):
    try:
        try:
            CART_CONTAINER = request.session['CART_CONTAINER']
        except:
            CART_CONTAINER = {}
        CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
        return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        return JsonResponse({'data': []}, safe=False)


def RemoveFromCart(request):
    try:
        productid = request.GET['productid']
        CART_CONTAINER = request.session['CART_CONTAINER']
        del CART_CONTAINER[productid]
        request.session['CART_CONTAINER'] = CART_CONTAINER
        CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
        return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        return JsonResponse({'data': []}, safe=False)

def Index(request):
    return render(request, "index.html")

def Buy_Product(request):
    product = unquote(request.GET['product'])
    product = json.loads(product)
    return render(request, "Buy_product.html", {'product': product})

def Fetch_All_Products(request):
    try:
        db, cmd = Pool.ConnectionPooliing()
        query = "select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid) as cname,(select s.subcategoryname from subcategories s where p.subcategoryid=s.subcategoryid) as scname,(select b.brandname from brands b where p.brandid=b.brandid) as bname from products p"
        cmd.execute(query)
        products = cmd.fetchall()
        db.close()
        return JsonResponse({'data': products}, safe=False)
    except Exception as e:
        return JsonResponse({'data': []}, safe=False)

def Fetch_All_Category_JSON(request):
    try:
        DB, CMD = Pool.ConnectionPooliing()
        Q = "select * from categories"
        CMD.execute(Q)
        records = CMD.fetchall()
        DB.close()
        return JsonResponse({'data': records}, safe=False)
    except Exception as e:
        return JsonResponse({'data': []}, safe=False)

def Fetch_All_SubCategory_JSON(request):
    try:
        DB, CMD = Pool.ConnectionPooliing()
        Q = "select * from subcategories"
        CMD.execute(Q)
        records = CMD.fetchall()
        DB.close()
        return JsonResponse({'data': records}, safe=False)
    except Exception as e:
        return JsonResponse({'data': []}, safe=False)

def  CheckUserMobileno(request):
    mobileno=request.GET['mobileno']
    try:
      DB, CMD = Pool.ConnectionPooliing()
      Q = "select * from  users where mobileno='{0}'".format(mobileno)
      CMD.execute(Q)
      record = CMD.fetchone()
      print('User:', record)
      if(record):
          return JsonResponse({'data': record,'status':True}, safe=False)
      else:
          return JsonResponse({'data':[], 'status': False}, safe=False)
      DB.close()

    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)

def  InsertUser(request):
    emailid = request.GET['emailid']
    mobileno=request.GET['mobileno']
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    password = request.GET['password']
    print(emailid,mobileno,firstname,lastname,password)
    try:
      DB, CMD = Pool.ConnectionPooliing()
      Q = "insert into users(emailid,mobileno,firstname,lastname,password)  values('{0}','{1}','{2}','{3}','{4}')".format(emailid,mobileno,firstname,lastname,password)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      print("no error")
      return JsonResponse({'status':True}, safe=False)
    except Exception as e:
      print('Errorrrrrr:', e)
      return JsonResponse({'status':False}, safe=False)

def  CheckUserMobilenoForAddress(request):
    mobileno=request.GET['mobileno']
    try:
      DB, CMD = Pool.ConnectionPooliing()
      Q = "select UA.*,(select U.firstname from users U where U.mobileno=UA.mobileno) as firstname,(select U.lastname from users U where U.mobileno=UA.mobileno) as lastname  from  users_address UA where UA.mobileno='{0}'".format(mobileno)
      CMD.execute(Q)
      record = CMD.fetchone()
      print('User:', record)
      if(record):
          return JsonResponse({'data': record,'status':True}, safe=False)
      else:
          return JsonResponse({'data':[], 'status': False}, safe=False)
      DB.close()

    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)

def MyShoppingCart(request):
    try:
        try:
            CART_CONTAINER = request.session['CART_CONTAINER']
            total = 0
            totalprice = 0
            totalsavings = 0
            for key in CART_CONTAINER.keys():
                amt = (CART_CONTAINER[key]['price'] -
                       CART_CONTAINER[key]['offerprice'])
                CART_CONTAINER[key]['save'] = amt * \
                    int(CART_CONTAINER[key]['qty'])
                totalsavings += CART_CONTAINER[key]['save']
                CART_CONTAINER[key]['productprice'] = CART_CONTAINER[key]['offerprice'] * int(
                    CART_CONTAINER[key]['qty'])
                total += CART_CONTAINER[key]['offerprice'] * \
                    int(CART_CONTAINER[key]['qty'])
                totalprice += CART_CONTAINER[key]['price'] * \
                    int(CART_CONTAINER[key]['qty'])
        except Exception as err:
            CART_CONTAINER = {}
        return render(request, "MyCart.html", {'data': CART_CONTAINER.values(), 'totalamount': total, 'totalproducts': len(CART_CONTAINER.keys()), 'totalprice': totalprice, 'totalsavings': totalsavings})
    except Exception as err:
        return render(request, "MyCart.html", {'data': {}})
    
def  InsertUserAddress(request):
    mobileno=request.GET['mobileno']
    emailid = request.GET['emailid']
    addressone = request.GET['addressone']
    addresstwo = request.GET['addresstwo']
    landmark = request.GET['landmark']
    city = request.GET['city']
    state = request.GET['state']
    zipcode = request.GET['zipcode']
    try:
      DB, CMD = Pool.ConnectionPooliing()
      Q = "insert into users_address(mobileno, emailid, address1, address2, landmark, city, state, zipcode) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(mobileno,emailid,addressone,addresstwo,landmark,city,state,zipcode)
      print(Q)
      CMD.execute(Q)
      DB.commit()
      DB.close()
      return JsonResponse({'status':True}, safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'status':False}, safe=False)
