from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['title', 'text', 'category',  'rating', 'author']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("description")
        title = cleaned_data.get("name")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data