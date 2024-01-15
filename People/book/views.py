from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse,JsonResponse

from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Contact

# Create your views here.
def anonymous_required(view_function, redirect_to=None):
    """
    Decorator to ensure that the view function can only be accessed by anonymous users (not logged in).
    """
    if redirect_to is None:
        redirect_to = 'dash'  

    def wrapped(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(redirect_to)
        return view_function(request, *args, **kwargs)

    return wrapped

@anonymous_required
def home(request):
    return render(request,'book/home.html')

@anonymous_required
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST["pwd"]
        
        user = authenticate(username=username, password=pwd)
        
        if user:
            login(request, user)
            return redirect("dash")
        else:
            return redirect('home')
            
        
    return render(request,'book/login.html')
 
@anonymous_required
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        pwd = request.POST["pwd"]
        
        myuser = CustomUser.objects.create_user(username, email, pwd)
        myuser.name = fname
        myuser.phone = phone
        
        myuser.save()
        
        return redirect('login')
    return render(request,'book/signup.html')   

@login_required
def dash(request):
    user_contacts = Contact.objects.filter(user=request.user)
    return render(request,'book/dash.html', {'user_contacts': user_contacts})

@login_required
def log_user(request):
    logout(request)
    return redirect('home')  

def create_contact(request):
    if request.method == 'POST':
        user = request.user  # Get the currently logged-in user
        name = request.POST.get('name')
        mobile_number1 = request.POST.get('mobile_number1')
        mobile_number2 = request.POST.get('mobile_number2')
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        address = request.POST.get('address')
        age = request.POST.get('age')
        ig = request.POST.get('ig')
        x = request.POST.get('x')
        telegram = request.POST.get('telegram')
        linkedin = request.POST.get('linkedin')

        contact = Contact(
            user=user,
            name=name,
            mobile_number1=mobile_number1,
            mobile_number2=mobile_number2,
            email1=email1,
            email2=email2,
            address = address,
            age=age,
            ig=ig,
            x=x,
            telegram=telegram,
            linkedin=linkedin,
        )
        contact.save()

        return redirect('dash')  # Redirect to your contacts list view

    return render(request, 'book/create_contact.html')

def view_contacts(request):
    user_contacts = Contact.objects.filter(user=request.user)
    return render(request, 'book/view_contacts.html', {'user_contacts': user_contacts})

def get_contact_details(request):
    contact_name = request.GET.get('contact_name')
    contact = get_object_or_404(Contact, name=contact_name, user=request.user)

    # Render contact details as HTML
    context = {'contact': contact}
    return render(request, 'book/contact_details.html', context)


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('dash')  # Change 'dashboard' to the appropriate URL

    return render(request, 'book/dash', {'contact': contact})


