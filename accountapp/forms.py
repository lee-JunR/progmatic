from django.contrib.auth.forms import UserCreationForm

# id창 비활성화
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True