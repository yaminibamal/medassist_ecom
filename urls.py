"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from medassist_ecom import SubCategory_Controller
from . import Category_Controller
from . import Brand_Controller
from . import Product_Controller
from . import Login_Controller
from . import UserInterface

urlpatterns = [
    path('admin/', admin.site.urls),
    # for Categories
    path('categoryinterface/', Category_Controller.Category_Interface),
    path('submitcategory', Category_Controller.Submit_Category),
    path('displayallcategories/', Category_Controller.Display_All_Category),
    path('editcategory/', Category_Controller.Edit_Category),
    path('deletecategory/', Category_Controller.Delete_Category),
    path('editcategoryicon', Category_Controller.Edit_CategoryIcon),
    path('fetch_all_category_json', Category_Controller.Fetch_All_Category_JSON),
    # for Sub Categories
    path('subcategoryinterface/', SubCategory_Controller.Subcategory_Interface),
    path('submitsubcategory', SubCategory_Controller.Submit_Subcategory),
    path('displayallsubcategories', SubCategory_Controller.Display_All_Subcategory),
    path('editsubcategory/', SubCategory_Controller.Edit_Subcategory),
    path('deletesubcategory/', SubCategory_Controller.Delete_Subcategory),
    path('editsubcategoryicon', SubCategory_Controller.Edit_SubcategoryIcon),
    # for Brand
    path('brandinterface/', Brand_Controller.Brand_Interface),
    path('submitbrand', Brand_Controller.Submit_Brand),
    path('fetchallsubcategoriesjson', Brand_Controller.Fetch_All_SubCategory_JSON),
    path('displayallbrands', Brand_Controller.Display_All_Brands),
    path('editbrand/', Brand_Controller.Edit_Brands),
    path('deletebrand/', Brand_Controller.Delete_Brand),
    path('editbrandicon', Brand_Controller.Edit_BrandIcon),
    # for Products
    path('productinterface/', Product_Controller.Product_Interface),
    path('submitproduct', Product_Controller.Submit_Product),
    path('fetchallbrandsjson', Product_Controller.Fetch_All_Brands_JSON),
    path('displayallproducts', Product_Controller.Display_All_Products),
    path('editproducts/', Product_Controller.Edit_Products),
    path('editproducticon', Product_Controller.Edit_ProductIcon),
    path('deleteproduct/', Product_Controller.Delete_Product),
    # for Login Page
    path('logininterface/', Login_Controller.Login_Interface),
    path('adminlogout/', Login_Controller.Admin_Logout),
    path('loginvarification', Login_Controller.Login_Varification),
    path('dashboard/', Login_Controller.Dashboard_Interface),

    # for user interface
    path('home/', UserInterface.Index),
    path('fetch_all_user_category/', UserInterface.Fetch_All_Category_JSON),
    path('fetch_all_products/', UserInterface.Fetch_All_Products),
    path('fetch_all_subcategory_json/', UserInterface.Fetch_All_SubCategory_JSON),
    path('buy_product', UserInterface.Buy_Product),
    path('add_to_cart/', UserInterface.AddToCart),
    path('fetch_cart/', UserInterface.FetchCart),
    path('remove_from_cart/', UserInterface.RemoveFromCart),
    path('signin/', UserInterface.Signin),
    path('myshoppingcart/',UserInterface.MyShoppingCart),
    path('check_user_mobileno/',UserInterface.CheckUserMobileno),
    path('insert_user/',UserInterface.InsertUser),
    path('check_user_mobileno_for_address/',UserInterface.CheckUserMobilenoForAddress),
    path('insert_user_address/',UserInterface.InsertUserAddress),

]
