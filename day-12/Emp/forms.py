from Emp.models import UserRg
from django import forms


class UsregForm(forms.ModelForm):
	class Meta:
		model=UserRg
		fields=['username','email','password']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username","required":True, 
		}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","required":True, }),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email id","required":True, }),
		
	}