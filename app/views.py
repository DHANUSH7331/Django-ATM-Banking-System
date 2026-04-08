from .forms import AccountCreationForm , Recaptcha
from django.shortcuts import render , redirect
from .models import Accounts
from django.core.mail import send_mail
from .utils.otp import otp
from django.conf import settings
from pyexpat.errors import messages

# Create your views here.

def  index(request):
    return render(request,'index.html')

def acc_creation(request):
    form = AccountCreationForm()
    form1 = Recaptcha()
    if request.method == "POST":
        form = AccountCreationForm(request.POST,request.FILES)
        form1 = Recaptcha(request.POST)
        if form.is_valid() and form1.is_valid():
            form.save()
            print('added')
    context = {
        'form':form,
        'form1':form1
    }
    return render(request,"acc_creation.html",context)

def pin_gen(request):
    msg = ""
    data = None
    if request.method == "POST":
        acc = int(request.POST.get('acc'))
        aadhar = int(request.POST.get('aadhar'))
        phone = int(request.POST.get('phone'))
        try:
            data = Accounts.objects.get(acc_num = acc)
        except:
            msg = "Account Doesn't Exist"
        if data:
            if data.aadhar == aadhar:
                if data.phone == phone:
                    b = otp()
                    send_mail(f"OTP id {b}","Don't Share Your One time password It'll Expire in 10 mins",settings.EMAIL_HOST_USER,[data.email],fail_silently=True)
                    request.session['acc'] = data.acc_num
                    request.session['opt'] = b
                    return redirect('valid')
                else:
                    msg = 'Phone Number is not Valid'
            else:
                msg = 'Aadhar Number is not Valid'
    context = {
        'msg':msg
    }
    return render(request,'pin_gen.html',context)

def validation(request):
    msg = ""
    if request.method == 'POST':
        opt = int(request.session('opt'))
        acc = int(request.session('acc'))
        otp = int(request.POST.get('otp'))
        pin = int(request.POST.get('pin'))
        c_pin = int(request.POST.get('c_pin'))
        if otp == opt:
            if pin == c_pin:
                data = Accounts.objects.get(acc_num = acc)
                data.set_pin (str(pin))
                data.save()
                return redirect('home')
            else:
                msg = 'Pin Mismatch'
        else:
            msg = 'OTP is Invalid please try again'
    context = {
        'msg':msg
    }
    return render(request,'valid.html',context)

def check_balance(request):
    msg = ""
    data = None
    if request.method == 'POST':
        acc = int(request.POST.get('acc'))
        pin = int(request.POST.get('pin'))
        try:
            data = Accounts.objects.get(acc_num = acc)
        except:
            msg = "Acc Number is Invalid"
        if data:
            d_pin = data.get_pin()
            print(d_pin,pin)
        if int(d_pin)==pin:
            msg = f'Your Current Balance is {data.balance}₹'
    context = {
        'msg' : msg
        }
    return render(request,'check.html',context)

def deposit(request):
    data = None
    if request.method == 'POST':
        acc = int(request.POST.get('acc'))
        pin = int(request.POST.get('pin'))
        amt = int(request.POST.get('amt'))
        try:
            data = Accounts.objects.get(acc_num = acc)
        except:
            messages.error(request,"Acc not Found",'transaction.html')
        if data:
            if int(data.get_pin())==pin:
                if amt >= 100:
                    if amt <= 100000:
                        old_bal = data.balance
                        data.balace = old_bal + amt
                        data.save()
                        return redirect('home')
                    else:
                        messages.error(request,'Amount is high so please contact the bank','transaction.html')
                else:
                    messages.error(request,'Amount is low to deposit','transaction.html')
            else:
                messages.error(request,'Incorrect PIN','transaction.html')
    return render(request,'transaction.html')

def withdrawl(request):
    data = None
    if request.method == 'POST':
        acc = int(request.POST.get('acc'))
        pin = int(request.POST.get('pin'))
        amt = int(request.POST.get('amt'))
        try:
            data = Accounts.objects.get(acc_num = acc)
        except:
            messages.error(request,"Acc not Found",'transaction.html')
        if data:
            if int(data.get_pin())==int(pin):
                if amt >= 100:
                    if amt <= data.balance:
                        old_bal = data.balance
                        data.balace = old_bal - amt
                        data.save()
                        return redirect('home')
                    else:
                        messages.error(request,'Amount is high so please contact the bank','transaction.html')
                else:
                    messages.error(request,'Amount is low to deposit','transaction.html')
            else:
                messages.error(request,'Incorrect PIN','transaction.html')
    return render(request,'transaction.html')

def acc_transfer(request):
    data = None
    if request.method == 'POST':
        f_acc = int(request.POST.get('f_acc'))
        pin = int(request.POST.get('pin'))
        t_acc = int(request.POST.get('t_acc'))
        amt = int(request.POST.get('amt'))
        try:
            f_data = Accounts.objects.get(acc_num = f_acc)
            t_data = Accounts.objects.get(acc_num = t_acc)
        except:
            messages.error(request,"Acc not Found","acc_transfer.html")
        if f_data:
            if int(f_data.get_pin()) == int(pin):
                if amt >= 1:
                    if amt <= f_data.balance:
                        f_data.balance = f_data.balance = amt
                        f_data.save()
                        t_data.balance = t_data.balance + amt
                        t_data.save()
                        return redirect('home')
                    else:
                        messages.error(request,'Amount is high so please contact the bank','acc_transfer.html')
                else:
                    messages.error(request,'Amount is low to deposit','acc_transfer.html')
            else:
                messages.error(request,'Incorrect PIN','acc_transfer.html')
    return render(request,'acc_transfer.html')