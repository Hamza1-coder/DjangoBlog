from django.shortcuts import render, redirect


def BASE(request):
    return render(request, 'Main/base.html')

def INDEX(request):
    return render(request, 'Main/index.html')

