from Emp.models import UsrRg
from django.models import Modelform

class UsregForm(forms.ModelForm):
	class meta:
		model=UsrRg
		fields="__all__"
