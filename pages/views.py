from django.shortcuts import render, redirect
import src.runner as runner
from .forms import ContactForm, GenreForm, RatingForm

def home_view(request):
    context = {
        "notes": runner.main(),
        "form": GenreForm()
    }
    return render(request, 'home-page.html', context)


def iteration_view(request, genre):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            ratings = [form.cleaned_data['rating1'],
                       form.cleaned_data['rating2'],
                       form.cleaned_data['rating3'],
                       form.cleaned_data['rating4'],
                       form.cleaned_data['rating5']]
            print(ratings)

    print(genre)
    context = {
        "notes": runner.main(),
        "genre": genre,
        "form": RatingForm()
    }
    return render(request, 'iteration.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
    form = ContactForm()
    return render(request, "form.html", {'form': form})