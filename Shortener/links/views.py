from django.shortcuts import render
import random
from .models import Links
# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_short(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        if not url.startswith(('http://', 'https://')):
            return render(request, 'home.html', {'form_error': 'Enter Full urls (https:// or http:.. //)'})
        
        link = Link(url = url)
        link.save()

        return render(request, 'home.html', {
        'success' : f"Your short url: /<b>{link.short_code}/</b>"}) 

    else:
        return render(request, 'home.html')
