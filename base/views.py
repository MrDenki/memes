from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from base.forms import RegistrationForm, ImageForm
from base.models import Users, CollectionsMemes


def main(request):
    return render(request, "main.html", context=locals())


def authorization(request):
    if request.method == 'POST':
        nickname = request.POST.get("nickname")
        password = request.POST.get("password")
        user = authenticate(username=nickname, password=password)
        if user is not None:
            login(request, user)
            return redirect('memes')
    return render(request, "authorization.html", context=locals())


def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            django_user = User.objects.create_user(email=form.instance.email, username=form.instance.nickname, password=form.instance.password)
            form.save()
            django_user.save()
            login(request, django_user)
            return redirect('memes')
    return render(request, "registration.html", context=locals())


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
def memes(request):
    posted = CollectionsMemes.objects.all().reverse().order_by('id')
    return render(request, "memes.html", context=locals())


@login_required()
def profile(request, id):
    user_profile = Users.objects.get(id=id)
    if user_profile.id == request.user.id:
        posted_by_user = CollectionsMemes.objects.filter(user=id)
        return render(request, "profile.html", context=locals())


@login_required()
def add_memes(request):
    all_memes = CollectionsMemes()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            if f.user.id == request.user.id:
            # CollectionsMemes.objects.create(user=request.user, photo=request.FILES.get('photo'),
            #                                 description=request.POST.get('description'))
            # all_memes.user_id = Users.objects.filter(id=request.user.id)[0].id
            # all_memes.photo = request.FILES.get('photo')
            # all_memes.description = request.POST.get('description')
            # all_memes.save()
                f.save()
                return redirect('memes')
    else:
        form = ImageForm()
    return render(request, "add_mem.html", context=locals())