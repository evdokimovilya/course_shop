from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views, update_session_auth_hash
from django.http import Http404

from apps.course.models import Course
from apps.basket.models import Basket

from .forms import AuthenticationForm, RegisterForm, ChangePssword
from . models import Profile


# def login_view(request):

#     if request.method == 'POST':
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('profile')

#     context = {"login_form": LoginForm()}

#     return render(request, 'user_profile/login.html', context )


def login(request):

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)

            return redirect('home')
        
    return render(request, 'user_profile/login.html', {"form": form})
    

def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password_one')

            user = User.objects.create_user(username=username, password=password)
            Profile.objects.create(user=user)
            user = authenticate(request, username=username, password=password)
            auth_login(request=request, user=user)

            return redirect('home')

    return render(request, 'user_profile/register.html', {"form": form} )


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')



@login_required
def profile(request):

    return render(request, 'user_profile/home.html')


@login_required
def courses(request):

    return render(request, 'user_profile/courses.html')


@login_required
def course_learn(request, course_id): 
    
    course = get_object_or_404(Course, id=course_id)

    if course not in request.user.profile.get_courses():
        raise Http404
    
    return render(request, 'course/learn.html', {"course": course})


@login_required
def change_password(request):
    form = ChangePssword(request.user)

    if request.method == 'POST':
        form = ChangePssword(request.user, request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('password_two')
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('home')
    return render(request, 'user_profile/change_password.html', context={'form': form})