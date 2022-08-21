from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserChangeForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("roles",)

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "roles",
        )


class CostomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "roles",
        )
