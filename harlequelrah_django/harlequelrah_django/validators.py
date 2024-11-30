from django.core.exceptions import ValidationError


class ContainLetterValidator:

    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                "Le mot de passe doit contenir au moins une lettre",
                code="password_no_letters",
            )

    def get_help_text(self):
        return "Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule"


class AlphaPasswordValidator:

    def validate(self, password, user=None):
        if all(char.isalpha() for char in password):
            raise ValidationError(
                "Le mot de passe doit contenir au moins un chiffre",
                code="password_no_number",
            )

    def get_help_text(self):
        return "Le mot de passe doit contenir au minimum un chiffre "




class ValidatorFileExtension:
    def validate_file_extension(value):
        import os

        extension = os.path.splitext(value.name)[1]
        valide_extension = [".pdf", ".doc", ".docx"]
        if extension.lower() not in valide_extension:
            raise ValidationError(
                "Les formats de fichers acceptés sont PDF , DOC , DOCX uniquement "
            )
