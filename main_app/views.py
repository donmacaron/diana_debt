from django.shortcuts import render, redirect
from .models import Debt, Payment
from .forms import PaymentForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def show(request):
    d_form = PaymentForm
    # l_form = LoginForm
    debt = Debt.objects.first()
    payments = Payment.objects.filter().order_by('-when')
    final_debt = debt.debt - sum([x['how_much'] for x in payments.values('how_much')])
    if request.method == 'POST':
        if request.user.is_authenticated:
            print('DA')
            d_form = PaymentForm(request.POST)
            r_debt = d_form.save()
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'main_app/index.html', {'debt':debt, 'payments':payments})
            else:
                return HttpResponse('<h1>неправильный пароль. или юзернейм. или твоя жизнь</h1>')
    return render(request, 'main_app/index.html', {'debt':debt, 'payments':payments, 'final_debt':final_debt})
