from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import Country, City, Category, Wishlist
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# from django.http import JsonResponse
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
        'cities' : City.objects.all(),
        'categories':Category.objects.all(),
        'Countries' : Country.objects.all()[:10],
        'mostRated' : City.objects.order_by('-rating')[:10],
    })

def explore(request):
    # category_filter = request.GET.get('category_exact')
    # country_filter = request.GET.get('country_exact')
    searchbar = request.GET.get('searchbar')

    
    countries= Country.objects.all()
    categories = Category.objects.all().exclude(type__in = ['Most Rated','Not Specified'])

    # if category_filter != 'All' and country_filter!= 'All' and searchbar != '' and searchbar is not None:
    #     cities = cities.filter(Q(name__icontains = searchbar) | Q(country__name__icontains = searchbar)).filter(category__type__iexact = category_filter, country__name__iexact = country_filter)

    # if category_filter != 'All':
    #     cities = cities.filter(category__type__exact = category_filter)

    # if country_filter != 'All':
    #     cities = cities.filter(country__name__exact = country_filter)

    if searchbar != '' and searchbar is not None:
        cities = City.objects.all()
        cities = cities.filter(Q(name__icontains = searchbar) | Q(country__name__icontains = searchbar))
        return render(request, 'pages/explore.html',{
            'cities': cities,
            'foundedResults': cities.__len__,
            'countries': countries,
            'categories': categories,
        })
    return render(request, 'pages/explore.html',{'errorMsg': 'Please type somthing to search for!'})

@login_required
def wishlist(request):
    wishlist = Wishlist.objects.get(user=request.user)
    cities = wishlist.cities.all()
    context = {'cities': cities}
    return render(request, 'pages/wishlist.html', context)

@login_required
def wishlist_add_remove(request, city_id):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    city = get_object_or_404(City, id=city_id)
    
    if city in wishlist.cities.all():
        wishlist.cities.remove(city)
        message = 'City removed from wishlist'
    else:
        wishlist.cities.add(city)
        message = 'City added to wishlist'
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required 
@csrf_exempt
def profile(request):
    if request.method == 'POST':
        # Handle first name and last name changes
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        if first_name:
            request.user.first_name = first_name
        if last_name:
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
            else:
                request.user.last_name = last_name
        if username:
            request.user.username = username
        request.user.save()
        messages.success(request, 'Profile updated successfully')

        # Handle password change
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully')
        # else:
        #     for field, errors in password_form.errors.items():
        #         for error in errors:
        #             messages.error(request, f"{field}: {error}")
    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'pages/profile.html', {'password_form': password_form})

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
@csrf_exempt
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
        Wishlist.objects.create(user=myuser)
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
        
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = 'Something went wrong try again!'
    return render(request, 'pages/signin.html', {'error_message': error_message})

def signout(request):
    logout(request)
    return redirect(reverse('signin'))

def categories(request, category):
    cities = City.objects.filter(category=category)
    return render(request, 'pages/categories.html', {'cities': cities})

def details(request, countryName , cityId):
    cityInfo = City.objects.get(id=cityId)
    context = {
        'name': cityInfo.name,
        'category': cityInfo.category,
        'rating': cityInfo.rating,
        'exchangeRate': cityInfo.exchangeRate,
        'image': cityInfo.image,
        'caption': cityInfo.caption,
        'country': cityInfo.country,
        'inWishlist': cityInfo.inWishlist,
        'mapSrc' : cityInfo.mapSrc,
        'activities': cityInfo.activities,
        'restaurants': cityInfo.restaurants,
        'hotels': cityInfo.hotels,
    }
    return render(request, 'pages/details.html', context)

def countries(request, countryName = None):
    country = Country.objects.all().filter(name = countryName) if countryName is None else Country.objects.all().get(name = countryName)
    # cityInfo = City.objects.get(id = cityId)
    return render(request, 'pages/countries.html', {
        'cities' : City.objects.all(),
        'country' : country,
        'countries' : Country.objects.all(),
        'categories': Category.objects.all().exclude(type = 'Most Rated'),

        # 'cname': cityInfo.name,
        # 'ccategory': cityInfo.category,
        # 'crating': cityInfo.rating,
        # 'cexchangeRate': cityInfo.exchangeRate,
        # 'cimage': cityInfo.image,
        # 'ccaption': cityInfo.caption,
        # 'ccountry': cityInfo.country,
        # 'cinWishlist': cityInfo.inWishlist,

    })

# def trimSpace(category):
#     return trim()

# def toggleFavorite(request, cityName) :
#     favIcon = get_object_or_404()
#     for i in favIcon:
#         if (favIcon.item(i).getAttribute('src') == "/static/img/Icons/Favorite-outlined.svg"):
#             favIcon.item(i).setAttribute('src', "/static/img/Icons/Favorite-filled.svg")
#         else:
#             favIcon.item(i).setAttribute('src', "/static/img/Icons/Favorite-outlined.svg")