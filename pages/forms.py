from django import forms

rating_choices = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")]


class GenreForm(forms.Form):
    genre = forms.CharField(widget=forms.HiddenInput())


class RatingForm(forms.Form):
    rating1 = forms.ChoiceField(choices=rating_choices)
    rating2 = forms.ChoiceField(choices=rating_choices)
    rating3 = forms.ChoiceField(choices=rating_choices)
    rating4 = forms.ChoiceField(choices=rating_choices)
    rating5 = forms.ChoiceField(choices=rating_choices)


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='e-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)