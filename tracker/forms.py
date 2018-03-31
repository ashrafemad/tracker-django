from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserAllData(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff')
