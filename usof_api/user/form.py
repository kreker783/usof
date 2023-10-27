from django.forms import ModelForm
from .models import User


class PictureForm(ModelForm):
    class Meta:
        model = User
        fields = ('login', 'picture',)
