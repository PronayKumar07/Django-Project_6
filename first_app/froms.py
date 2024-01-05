from django import forms
from django.core import validators

class contactForm(forms.Form):
  name = forms.CharField(label = "User Name", help_text='Enter Your name', widget= forms.Textarea(attrs = {'placeholder': 'Enter Your Name:'}))
  # file = forms.FileField()
  email = forms.EmailField()
  age = forms.IntegerField()
  weight = forms.FloatField()
  check = forms.BooleanField()
  Birthday = forms.DateField(widget = forms.DateInput(attrs = {'type': 'datetime-local'}))
  appointment = forms.DateTimeField(widget = forms.DateInput(attrs = {'type': 'date'}))
  CHOICES = [('s', 'Small'), ('M', 'Medium'), ('L', 'Large')]
  size = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
  meal = [('P', 'Pepperoni'), ('M', 'Musrom'), ('C', 'Chicken')]
  pizza = forms.MultipleChoiceField(choices = meal, widget= forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#   name = forms.CharField(widget= forms.TextInput)
#   email = forms.CharField(widget= forms.EmailInput)
#   # def clean_name(self):
#   #   valname = self.cleaned_data['name']
#   #   if len(valname) < 10:
#   #     raise forms.ValidationError('Enter a name with 10 charcters')
#   #   return valname
#   def clean(self):
#     cleaned_data = super().clean()
#     valname = self.cleaned_data['name']
#     valemail = self.cleaned_data['email']
#     if len(valname) < 10:
#       raise forms.ValidationError('Enter a name with 10 charcters')
#     if '.com' not in valemail:
#       raise forms.ValidationError('Enter email with .com')


class StudentData(forms.Form):
  name = forms.CharField(widget= forms.TextInput, validators= [validators.MinLengthValidator(10, message= 'Enter a name with 10 charcter')])
  email = forms.CharField(widget= forms.EmailInput, validators=[validators.EmailValidator(message= 'Enter valid Email')])
  age = forms.CharField()
  file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message= 'File extension must be .pdf')])


class PasswordValidationProject(forms.Form):
  name = forms.CharField(widget=forms.TextInput)
  Password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)

  def clean(self):
    cleaned_data = super().clean()
    val_pass = self.cleaned_data['Password'] 
    val_pass2 = self.cleaned_data['confirm_password'] 
    if val_pass != val_pass2:
      raise forms.ValidationError('Password not match')