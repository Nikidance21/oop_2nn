from django.core.validators import RegexValidator
from django import forms
from django.core.exceptions import ValidationError
from catalog.models import User, Application


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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UpdateApplicationForm(forms.ModelForm):
    status = forms.CharField(max_length=200, label='Комментарий')

    img = forms.ImageField(label='Фото работы', required=False)
    comment = forms.CharField(label='Комментарий', required=False, help_text='Комментарий')

    def clean(self):
        super().clean()
        print(self.cleaned_data)

        status = self.cleaned_data.get('status')
        comment = self.cleaned_data.get('comment')
        img = self.cleaned_data.get('img')
        if status == 'in work' and comment == '':
            errors = {'status': ValidationError(
                'После изменения статуса на принят в работу нужно добавить комментарий'
            )}
            raise ValidationError(errors)
        elif status == 'done' and img is None:
            errors = {'status': ValidationError(
                'После изменения статуса на выполнено нужно добавить фото'
            )}
            raise ValidationError(errors)
        elif status == 'new':
            errors = {'status': ValidationError(
                'Вы не можете изменить статус на новый'
            )}
            raise ValidationError(errors)

    class Meta:
        model = Application
        fields = ('status', 'img', 'comment')
