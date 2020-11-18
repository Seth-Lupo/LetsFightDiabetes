from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html", {})

def article1(request):
    return render(request, "article1.html", {})

def article2(request):
    return render(request, "article2.html", {})

def article3(request):
    return render(request, "article3.html", {})

def article4(request):
    return render(request, "article4.html", {})

def citations(request):
    return render(request, "citations.html", {})


