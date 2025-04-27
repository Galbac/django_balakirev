from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.forms import Textarea
from django.template.defaultfilters import title, default
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

from women.models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code, params={"value": value})


# НЕ СВЯЗАННАЯ С МОДЕЛЬЮ
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, min_length=5, label="Заголовок",
#                             widget=forms.TextInput(attrs={'class': 'form-input'}),
#                             # validators=[
#                             #     RussianValidator(),
#                             # ],
#                             error_messages={
#                                 'min_length': 'Слишком короткий заголовок',
#                                 'required': 'Без заголовка - никак',
#                             })
#
#     slug = forms.SlugField(max_length=255, label="URL", validators=[
#         MinLengthValidator(5, message="Минимум 5 символов"),
#         MaxLengthValidator(100, message="Максимум 100 символов"),
#     ])
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Контент')
#     is_published = forms.BooleanField(required=False, initial=True, label='Статус')
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label="Не замужем", required=False,
#                                      label='Муж')
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
#         if not (set(title) <= set(ALLOWED_CHARS)):
#             raise ValidationError("Должны быть только русские символы, дефис и пробел.")
#
#         return title

class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='Не замужем',
                                     label='Муж')

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Длина превышает 50 символов')
        return title

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'tags', 'husband']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {
            'slug': 'URL'
        }


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=5, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    email = forms.EmailField(min_length=5, required=False, label='E-mail',
                             widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    first_name = forms.CharField(max_length=50, required=False, label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    last_name = forms.CharField(max_length=50, required=False, label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    password1 = forms.CharField(min_length=6, label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-register-input'}))
    password2 = forms.CharField(min_length=6, label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-register-input'}))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']
        ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_"

        if not (set(password1) <= set(ALLOWED_CHARS)) or not (set(password1) <= set(ALLOWED_CHARS)):
            raise ValidationError("Некорректно введенный пароль.")
        elif len(password2) < 6 or len(password1) < 6:
            raise ValidationError("Слишком короткий пароль.")
        elif password1 != password2:
            raise ValidationError("Пароли не совпадают.")


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')



