from django.http import JsonResponse
from django.shortcuts import render
from .models import Response

# Create your views here.

def responses1(request):

    if request.method == "POST":
        return saveResponse(request, "1")

    if request.method == "GET":
        responses = reversed(list(Response.objects.filter(article="1").reverse()))
        return render(request, "responses.html", {"responses": responses, "article": "1", "question": "How could you warn people in your community about their risk of getting diabetes? How could you do this in a way that is not negative, but positive?"})

def responses2(request):

    if request.method == "POST":
        return saveResponse(request, "2")

    if request.method == "GET":
        responses = reversed(list(Response.objects.filter(article="2").reverse()))
        return render(request, "responses.html", {"responses": responses, "article": "2", "question": "How has your income made it easier or harder to stay healthy?"})

def responses3(request):

    if request.method == "POST":
        return saveResponse(request, "3")

    if request.method == "GET":
        responses = reversed(list(Response.objects.filter(article="3").reverse()))
        return render(request, "responses.html", {"responses": responses, "article": "3", "question": "How would medicare for all affect you personally. Do you believe that you need it or that you already have sufficient healthcare?"})

def responses4(request):

    if request.method == "POST":
        return saveResponse(request, "4")

    if request.method == "GET":
        responses = reversed(list(Response.objects.filter(article="4").reverse()))
        return render(request, "responses.html", {"responses": responses, "article": "4", "question": "How can you effectively get the attention of politicians?"})


def saveResponse(request, article):

    print(request.POST.get("name"))

    r = Response()

    r.name = request.POST.get("name")
    r.content = request.POST.get("responses")
    r.article = article

    r.save()

    return JsonResponse({})