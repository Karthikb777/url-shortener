from django.shortcuts import render, redirect
from .models import url
from .forms import newUrlForm
from django.http import HttpResponseNotFound, Http404
from .forms import LoginForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    form = newUrlForm()

    print("full uri: " + request.build_absolute_uri())
    if request.method == 'POST':
        form = newUrlForm(request.POST)

        if form.is_valid():
            user = request.user
            full_url = form.cleaned_data['full_url']
            ext = form.cleaned_data['ext']
            url.objects.create(user=user, full_url=full_url, ext=ext)
            return redirect('home')

    context = {
        'newUrlForm': form,
        'allUrls': url.objects.filter(user=request.user)[::-1],
        'baseUrl': request.build_absolute_uri()
    }

    return render(request, 'mainapp/home.html', context)

# redirect view
def redirect_to_url(request, uid):
    try:
        url_obj = url.objects.get(ext=uid)
        return redirect(url_obj.full_url)
    except:
        # raise Http404()
        return HttpResponseNotFound("<h1>404 not found</h1>")

# delete url view
def delete_url(request, ext):
    try:
        url_obj = url.objects.get(ext=ext)
        url_obj.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound("<h1>404 not found</h1>")

# register view
def register_new_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'mainapp/signUp.html', context)

# login view
def login_user(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user=user)
                return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'mainapp/login.html', context)


# logout view
def logout_user(request):
    logout(request)
    return redirect('login')