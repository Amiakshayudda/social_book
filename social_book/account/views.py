from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from users.models import CustomUser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def register(request):

    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        city = request.POST['city']
        state = request.POST['state']
        public_visibility = bool(request.POST.get('public_visibility', False))
        birth_year = int(request.POST['birth_year'])
        age = timezone.now().year - birth_year

        if password1 == password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, "Email taken")
                return redirect('register.html')
            else:
                
                user = CustomUser.objects.create_user(email=email, password=password1, full_name=full_name, gender=gender, city=city, state=state, public_visibility=public_visibility, age=age, birth_year=birth_year)
                user.save()
                messages.info(request, "User created")
                return redirect('login.html')

        else:
            messages.info(request, "Password not matching..")
            return redirect('register.html')
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            otp = random.randint(100000, 999999)
            request.session['otp'] = otp
            message = f'Hello! You have recently tried to log in to our website.. The OTP for your login is {otp}'
            send_mail(
                'OTP for your sign in!',
                message,
                'Django Project',
                [request.user.email],
                fail_silently=False,
            )
            return redirect("otp")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login.html")

    elif 'code' in request.GET:
        user = request.user
        login(request, user.email, user.password)
        return redirect('index.html')

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('login.html')

@login_required(login_url='login.html')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login.html')
def otp(request):
    if request.method == 'POST':
        entered_otp = request.POST['otp']
        session_otp = request.session['otp']
        print(session_otp + session_otp)
        if entered_otp == str(session_otp):
            return redirect('index')
        else:
            messages.info(request, "Invalid OTP.. Please enter correct OTP")
            return redirect('otp')
    else:
        return render(request, 'otp.html')

def password(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            user = CustomUser.objects.get(email=email)
            if user is not None:
                message = f'Please click on the link to reset password http://localhost:8000/account/changepassword?email={email}'
                send_mail(
                    'Reset Password for DeskApp',
                    message,
                    'Django Project',
                    [email],
                    fail_silently=False,
                )
                messages.info(request, "Email has been sent. Please check check your registered email.")
                return redirect('login')
        except Exception:
            messages.info(request, "Email is not registered")
            return redirect('password')
    else:
        return render(request, 'password.html')

# @csrf_exempt
def changepassword(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST.get('email')
        print(password1, password2, email)

        if password1 == password2:
            user = CustomUser.objects.get(email=email)
            user.set_password(password1)
            user.save()
            messages.info(request, "Password updated successfully")
            return redirect('login')
        else:
            messages.info(request, "Password and confirm password should match..")
            return redirect('changepassword')
    else:
        email = request.GET.get('email')
        return render(request, 'changepassword.html', {'email': email})

@login_required(login_url='login.html')
def profile(request):
    return render(request, 'profile.html')