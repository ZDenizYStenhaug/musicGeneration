from django import forms

rating_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class GenreForm(forms.Form):
    genre = forms.CharField(widget=forms.HiddenInput())


# class RatingForm(forms.Form):


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='e-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)