from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(r):
    return render(r, 'index.html', context={"i": "Aici va fi o pagina de \"Bun venit\""})

def rei(r):
    return render(r, "reg_intrari.html", {"i": "Aici va fi Registrul Electronic - Intrări"})

def reo(r):
    return render(r, "reg_iesiri.html", context={"i":"Aici va fi Registrul Electronic - Intrări"})

def svp(r):
    return render(r, "svp.html", context={"i":"Aici va fi Registrul Electronic - Supravegheri"})

def ref(r):
    return render(r, "referate.html", context={"i":"Aici va fi Registrul Electronic - Referate"})