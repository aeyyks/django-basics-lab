from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

from .models import Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
]

MAX_IMAGE_SIZE = 5 * 1024 * 1024
ALLOWED_IMAGE_FORMATS = ('jpeg', 'png')


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')

    def _validate_forbidden_words(self, value):
        if not value:
            return value
        lower_value = value.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_value:
                raise ValidationError(f'Использование слова «{word}» запрещено.')
        return value

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return self._validate_forbidden_words(name)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return self._validate_forbidden_words(description)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if isinstance(image, UploadedFile):
            if image.size > MAX_IMAGE_SIZE:
                raise ValidationError('Размер изображения не должен превышать 5 МБ.')
            if image.name.rsplit('.', 1)[-1].lower() not in ALLOWED_IMAGE_FORMATS:
                raise ValidationError('Допустимы только изображения в форматах JPEG или PNG.')
        return image
