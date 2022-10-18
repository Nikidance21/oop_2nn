from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from catalog.models import User


class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(label='Имя', validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                                   message='Разрешены только кириллица,тире и пробелы')],
                           error_messages={
                               'required': "Обязательное поле",
                           })
    surname = forms.CharField(label='Фамилия', validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                                          message="Разрешены только кириллица,тире и пробелы")],
                              error_messages={
                                  'required': "Обязательное поле",
                              })
    username = forms.CharField(label='Логин', validators=[RegexValidator('^[a-zA-Z-]+$',
                                                                         message='Разрешены только латиница и тире')],
                               error_messages={
                                   'required': "Обязательное поле",
                                   'unique': "Данный логин занят"
                               })
    email = forms.EmailField(label='Адрес электронной почты',
                             error_messages={
                                 'invalid': "Не правильный формат адреса",
                                 'unique': "Данный адрес занят"
                             })
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': "Обязательное поле"
                               })
    password2 = forms.CharField(label='Пароль(повторно)',
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': "Обязательное поле"
                                })
    rules = forms.BooleanField(required=True,
                               label='Согласие с правилами регистрации',
                               error_messages={
                                   'required': "Обязательное поле"
                               })

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Введенные данные не совпадают', code='password_mismatch')
            })

    class Meta:
        model = User
        fields = ('name', 'surname', 'username', 'email', 'password', 'password2', 'rules')
