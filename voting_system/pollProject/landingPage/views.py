from django.shortcuts import render

def home(request):
    return render(request, 'landingpage/home.html')

def about(request):
    return render(request, 'landingpage/about.html')

def contact(request):
    return render(request, 'landingpage/contact.html')
