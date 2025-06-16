from django.contrib.auth.forms import (
    UserCreationForm,
    
    UserChangeForm
)
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email", "role", "team")
        labels = {
            "email": _("Email Address"),
            "role": _("Role"), 
            "team": _("Team")
        }
        help_texts = {
            "email": _("Enter Email Address"),
            "role": _("Enter your role"),
            "team": _("What is your assigned team?")
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields