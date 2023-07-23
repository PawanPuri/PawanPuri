from testapp.models import Emp_model
from django import forms
class EmloyeeForm(forms.ModelForm):
    class Meta:
        model = Emp_model
        fields= '__all__'

