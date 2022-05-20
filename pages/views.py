from django.shortcuts import render, redirect
import src.runner as runner
from .forms import GenreForm, RatingForm


ITERATION_NUM = 1


def home_view(request):
    context = {
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
            global ITERATION_NUM
            ITERATION_NUM += 1
            melodies_path = runner.create_melodies(genre, ITERATION_NUM, ratings=ratings)
    else:
        melodies_path = runner.create_melodies(genre, ITERATION_NUM)
    context = {
        "melodies_path": melodies_path,
        "genre": genre,
        "iteration_num": ITERATION_NUM,
        "form": RatingForm()
    }
    return render(request, 'iteration.html', context)
