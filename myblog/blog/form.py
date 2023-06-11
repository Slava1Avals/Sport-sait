from django import forms
from .models import Coments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ('name', 'email', 'text_comment')
