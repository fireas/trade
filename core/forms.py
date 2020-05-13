from allauth.account.forms import SignupForm,LoginForm
from django import forms
from .models import Book,GENRE_CHOICES,TRADETYPE_CHOICES

class Signup_Form(SignupForm):

    def __init__(self, *args, **kwargs):
        super(Signup_Form, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'username',
        'type': 'text',
        'id': 'form10'
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
        'class': 'form-control',
        'name': 'email',
        'type': 'email',
        'id': 'form11'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'name': 'password',
        'type': 'password',
        'id': 'form12'
        })


class Login_Form(LoginForm):

    def __init__(self, *args, **kwargs):
        super(Login_Form, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'login',
        'type': 'text',
        'id': 'form2'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'name': 'password',
        'type': 'password',
        'id': 'form8'
        })




class AddForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'bookname',
        'type': 'text',
        'id': 'bookname',
        'placeholder':'Nom du Livre'
        }))
    author = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'bookauthor',
        'type': 'text',
        'id': 'bookauthor',
        'placeholder':'Auteur du Livre'
        }))
    genre = forms.CharField(widget=forms.Select(choices=GENRE_CHOICES,attrs={
        'name':'bookgenre',
        'class':'browser-default custom-select'
    }))
    tradeType = forms.CharField(widget=forms.Select(choices=TRADETYPE_CHOICES,attrs={
        'name':'booktrade',
        'class':'browser-default custom-select'
    }))
    price = forms.FloatField( widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name':'bookprice',
        'type': 'number',
        'id': 'bookprice',
        'placeholder':'Prix du Livre'
    }))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'style':"display:none;",
        'name':'bookimage',
        'id':'bookimage'
    }))
    description = forms.CharField(max_length=50, widget=forms.Textarea(attrs={
        'class':'form-control rounded-0',
        'name':'bookdesc',
        'type': 'text',
        'id': 'bookdescription',
        'placeholder':'Description du Livre'
    }))
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'genre',
            'tradeType',
            'price',
            'image',
            'description'
        ]
