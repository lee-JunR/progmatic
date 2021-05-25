from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreattionForm(ModelForm):
    class meta:
        model = Profile
        fields = ['image', 'nickname', 'message']