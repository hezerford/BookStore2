from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "street",
            "city",
            "postal_code",
            "country",
            "birth_date",
            "bio",
            "phone_number",
            "profile_picture",
        ]

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")
        if birth_date and birth_date.year < 1900:
            raise ValidationError("Пожалуйста, укажите настоящую дату рождения.")
        return birth_date

    def clean_postal_code(self):
        postal_code = self.cleaned_data.get("postal_code")
        if postal_code and not postal_code.isalnum():
            raise ValidationError(
                "Почтовый индекс должен содержать только буквы и цифры."
            )
        return postal_code


class FavoriteBooksForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["favorite_books"]
