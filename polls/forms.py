from django.forms import ModelForm
from polls.models import UserModel
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create the form class.
class RegisterForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['password', 'email' , 'first_name', 'last_name']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data['email']

        try:
            if email and UserModel.objects.get(email=email):
                raise ValidationError("Look like user all ready use this email")
        except UserModel.DoesNotExist:
            print('')

        # Always return the full collection of cleaned data.
        return cleaned_data

# Create the form class.
class UpdateForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['email' , 'first_name', 'last_name']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data['email']

        try:
            if email and UserModel.objects.get(email=email):
                raise ValidationError("Look like user all ready use this email")
        except UserModel.DoesNotExist:
            print('')

        # Always return the full collection of cleaned data.
        return cleaned_data

# Create the form class.
class LoginForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
    
    def clean(self):
        
        cleaned_data = self.cleaned_data

        try:
            get_email = cleaned_data['email']
        except KeyError as e:
            raise ValidationError("Error")

        get_password = cleaned_data['password']

        try:
            user = UserModel.objects.get(email=get_email)
            user.check_password(get_password)
        except UserModel.DoesNotExist:
            raise ValidationError("It's look like your account it's not recognized")

        return cleaned_data