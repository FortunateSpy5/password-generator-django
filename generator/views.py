from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list(string.ascii_lowercase)

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase', ''):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('numbers', ''):
        characters.extend(list(string.digits))

    if request.GET.get('special', ''):
        characters.extend(list(string.punctuation))

    the_password = ''.join([random.choice(characters) for _ in range(length)])
    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
