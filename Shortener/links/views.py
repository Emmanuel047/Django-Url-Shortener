from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import Links
# Create your views here.
def home(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        if not url.startswith(('http://', 'https://')):
            return render(request, 'home.html', {'form_error': 'Enter Full urls (https:// or http:.. //)'})
        
        existing = Links.objects.filter(url=url).first()
        if existing:
            link = existing
        else :
            link = Links(url = url)
            link.save()

        return render(request, 'home.html', {
        'success' : f"Your short url: /<b>{link.short_code}/</b>" ,
        'short_code' : link.short_code})

    else:
        return render(request, 'home.html')

def redirect_url(request, short_code):
    link =get_object_or_404(Links, short_code=short_code)
    link.on_click += 1
    link.save()

    return redirect(link.url)

def stats(request, short_code):
    link = get_object_or_404(Links, short_code=short_code)

    context = {
        'link': link,
        'short_url' :  f"https:127.0.0:8000/{short_code}/",
    }

    return render(request, 'stats.html', context)