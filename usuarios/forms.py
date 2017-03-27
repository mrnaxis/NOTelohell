from django import forms
from django.contrib.auth.forms import User

class RegistrarForm(forms.Form):
    nome_user = forms.CharField(required=True)
    email_user = forms.EmailField(required=True)
    senha_user = forms.CharField(required=True)
    senha_user_confirm = forms.CharField(required=True)
    nick_user = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarForm, self).is_valid():
            self.adiciona_erro('Verifique os dados inseridos') #just to be safe!
            valid = False

        if (str(self.data['senha_user']) != str(self.data['senha_user_confirm'])):
            self.adiciona_erro('Senha nao confere')
            valid = False

        existe_mail = User.objects.filter(username=self.data['email_user']).exists()

        if existe_mail:
            self.adiciona_erro('E-Mail ja Existente')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)
