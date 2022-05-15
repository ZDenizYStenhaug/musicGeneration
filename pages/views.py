from django.shortcuts import render, redirect
import src.runner as runner
from .forms import ContactForm, GenreForm

def home_view(request):
    context = {
        "notes": runner.main(),
        "form": GenreForm()
    }
    return render(request, 'home-page.html', context)


def iteration_view(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            selected_genre = form.cleaned_data['genre']
            return render(request, 'iteration.html', {'genre': selected_genre})

    context = {
        "notes": runner.main(),
        "form": GenreForm()
    }
    return render(request, 'home-page.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
    form = ContactForm()
    return render(request, "form.html", {'form': form})