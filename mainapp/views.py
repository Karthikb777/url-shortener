from django.shortcuts import render, redirect
from .models import url
from .forms import newUrlForm
from django.http import HttpResponseNotFound, Http404

# Create your views here.

def home(request):
    form = newUrlForm()

    print("full uri: " + request.build_absolute_uri())
    if request.method == 'POST':
        form = newUrlForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'newUrlForm': form,
        'allUrls': url.objects.all()[::-1],
        'baseUrl': request.build_absolute_uri()
    }

    return render(request, 'mainapp/home.html', context)

def redirect_to_url(request, uid):
    try:
        url_obj = url.objects.get(ext=uid)
        return redirect(url_obj.full_url)
    except:
        # raise Http404()
        return HttpResponseNotFound("<h1>404 not found</h1>")

def delete_url(request, ext):
    try:
        url_obj = url.objects.get(ext=ext)
        url_obj.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound("<h1>404 not found</h1>")




