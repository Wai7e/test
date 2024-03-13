from django import forms


class AddBookForm(forms.Form):
    name = forms.CharField(max_length=256)
    author = forms.CharField(max_length=256)
    category = forms.CharField(max_length=256)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['name'] == cleaned_data['author'] == cleaned_data['category']:
            self.add_error("name", "все поля одинаковы!")
        return cleaned_data


class RegisterForm(forms.Form):
    email = forms.EmailField()
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error("password", "password incorrect")
        return cleaned_data
