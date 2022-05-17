from django import forms

rating_choices = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")]


class GenreForm(forms.Form):
    genre = forms.CharField(widget=forms.HiddenInput())


class RatingForm(forms.Form):
    rating1 = forms.ChoiceField(choices=rating_choices, label="Rating for melody 1")
    rating2 = forms.ChoiceField(choices=rating_choices, label="Rating for melody 2")
    rating3 = forms.ChoiceField(choices=rating_choices, label="Rating for melody 3")
    rating4 = forms.ChoiceField(choices=rating_choices, label="Rating for melody 4")
    rating5 = forms.ChoiceField(choices=rating_choices, label="Rating for melody 5")


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='e-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)