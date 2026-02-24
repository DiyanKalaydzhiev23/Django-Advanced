from django.core.exceptions import ValidationError


class PracticalPasswordValidator:
    def validate(self, password: str, user=None) -> None:
        if len(set(password)) < 6:
            raise ValidationError("Password must contain at least 6 unique characters")


    def get_help_text(self) -> str:
        return "Your password should contain at least 6 unique characters"