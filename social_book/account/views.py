from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from users.models import CustomUser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
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
                messages.info(request, "Email taken")
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
            send_mail(
                'New Sign In',
                'Hello! You have recently logged in to our website..',
                'Django Project',
                [request.user.email],
                fail_silently=False,
            )
            return redirect("index.html")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login.html")

    else:
        return render(request, "login.html")
    

def logout(request):
    auth.logout(request)
    return redirect('login.html')

@login_required(login_url='login.html')
def index(request):
    return render(request, 'index.html')
