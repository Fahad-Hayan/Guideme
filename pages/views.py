from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Country, City
# from django.http import HttpResponse
# from django.core.mail import EmailMessage, send_mail
# from Guideme import settings
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_str
# from . tokens import generate_token


# Create your views here.

def home(request):
    return render(request, 'pages/home.html',{
        'cities' : City.objects.all().exclude(category='Not Specified')[:10],
        'categories': [
        'Most Rated',
        'Leisure Tourism',
        'Archaeological Tourism',
        'Religious Tourism',
    ],
    'Countries' : Country.objects.all()[:10]
    })

def categories(request):
    return render(request, 'pages/categories.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')

def about(request):
    return render(request, 'pages/about.html')

def email_confirmation(request):
    pass

# def activate(request,uidb64,token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser = None

#     if myuser is not None and generate_token.check_token(myuser,token):
#         myuser.is_active = True
#         # user.profile.signup_confirmation = True
#         myuser.save()
#         login(request,myuser)
#         messages.success(request, "Your Account has been activated!!")
#         return redirect('signin')
#     else:
#         return render(request,'pages/activation_failed.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!")
            return redirect('signup')
                
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email

        # subject = "Welcome to Guideme"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Guideme!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address."        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email

        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email"
        # message2 = render_to_string('email_confirmation.html',{
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [myuser.email],)
        # email.fail_silently = True
        # email.send()
        return redirect('signup')
    else:
        return render(request, "pages/signup.html")
        

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            firstname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "pages/home.html",{"firstname":firstname})
        else:
            messages.error(request, "User not found")
            return redirect('signin')
    else:
        return render(request, "pages/signin.html")

def signout(request):
    logout(request)
    return redirect("signin")

def details(request):
    return render(request, 'pages/details.html')

def countries(request, countryId = None):
    country = Country.objects.all().filter(id = countryId) if countryId is None else Country.objects.all().get(id = countryId)
    return render(request, 'pages/countries.html', {
        'cities' : City.objects.all(),
        'country' : country,
        'countries' : Country.objects.all(),
    })
