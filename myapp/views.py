from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login as authlogin,logout,authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.decorators.cache import never_cache
from django.contrib import messages
@login_required(login_url='login')
@never_cache
def home(request):
    if request.user.user_type == 'Admin':
        return redirect('admin_home')
    
    return render(request, 'home.html')
@never_cache
def login(request):
    if request.session.session_key :
        return redirect(home)
    User=None 
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username ,password=password)
        if user:
            if user.is_staff == False:
                authlogin(request, user)
                return redirect(home)
            elif user.is_staff == True:
                authlogin(request, user)
                return redirect(admin_home)
        else :
            messages.error(request,'Please check the username and password')
            return redirect(login)
    return render(request,'login.html')

def signout(request):
    logout(request)
    return redirect(login)

@never_cache
def signup(request):
    if request.session.session_key :
        return redirect(home)
    user=None
    error_message=None
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email')
        
        try:
            user = User.objects.create_user(username=username, password=password, email=email, user_type="user")
            return redirect(login)
        except Exception as e:
            error_message = "This username or email address is already taken. Please choose another one."
    return render(request, 'signup.html', {'user': user, 'error_message': error_message})


@never_cache
@login_required(login_url='login')
def admin_home(request):
    if request.user.user_type == 'Admin':
        username_s = None
        users = User.objects.all()
        if request.method == 'POST' :
            username_s = request.POST['username']
            users = User.objects.filter(username__icontains=username_s )
            if not users :
                messages.error(request,username_s+' des not exist in users')
                return redirect(admin_home)
        return render(request, 'admin_home.html', {'users': users, 'username_s':username_s})
    else :
        return redirect(home)
@never_cache
@login_required
@user_passes_test(lambda u: u.user_type == "Admin")
def admin_delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    messege=None
    if user.is_staff and user.is_superuser :
        username_s = None
        users = User.objects.all()
        messege = "you can't delete the main admin"
        return render(request, 'admin_home.html', {'messege' : messege,'users': users, 'username_s':username_s})
    user.delete()
    return redirect('admin_home')
@never_cache
@login_required
@user_passes_test(lambda u: u.user_type == "Admin")
def admin_edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.user_type = request.POST['user_type']
        user.save()
        return redirect('admin_home')
    return render(request, 'admin_edit_user.html', {'user': user})

@never_cache
@login_required
@user_passes_test(lambda u: u.user_type == "Admin")
def create_user(request):
    user=None
    error_message=None
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST.get('password')
        email = request.POST['email']
        user_type = request.POST['user_type']
        try:
            user = User.objects.create_user(username=username, password=password, email=email, user_type=user_type)
            return redirect(admin_home)
        except Exception as e:
            error_message = "This username or email address is already taken. Please choose another one."
    return render(request, 'create_user.html',{'error_message': error_message})




def admin_signout(request):
    logout(request)
    return redirect(login)



