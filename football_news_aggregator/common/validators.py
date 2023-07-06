from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FirstCharMustBeLetterValidator:
    def __call__(self, value):
        if not value[0].isalpha():
            raise ValidationError("Your name must start with a letter!")


@deconstructible
class NameContainsOnlyLettersValidator:
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError("Name should contain only letters!")


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))

    return validate
