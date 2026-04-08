from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ="home"),
    path('acc',views.acc_creation,name="acc"),
    path('pin',views.pin_gen,name="pin"),
    path('valid',views.validation,name="valid"),
    path('balance-Enquiry',views.check_balance,name="bal"),
    path('deposit',views.deposit,name = "deposit"),
    path('withdrawal',views.withdrawl,name = "withdraw"),
    path('transfer',views.acc_transfer,name = "transfer"),
]