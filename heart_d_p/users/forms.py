from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    dob=forms.DateField(required=True,widget=forms.SelectDateWidget(years=range(1900, 2024)))
    Hospital_name = forms.CharField(required=True,max_length=100)
 
    class Meta:
        model = User
        fields = ['username', 'email','phone_number','dob','Hospital_name','password1', 'password2']
       

class Health_Prediction_form(forms.Form):
    
    height = forms.FloatField(
        label='Height (cm)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    weight = forms.FloatField(
        label='Weight (kg)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    temperature = forms.FloatField(
        label='Tempreature (c)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    heart_rate = forms.FloatField(
        label='Heart_rate (c)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    cholestrol = forms.FloatField(
        label='Cholesterol (mg/dL)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    blood_sugar = forms.FloatField(
        label='Blood_Sugar (mg/dL)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    systolic_bp = forms.FloatField(
        label='Systolic_BP',
       widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    diastolic_bp = forms.FloatField(
        label='Diastolic_BP',        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    existing_conditions = forms.ChoiceField(
        choices=[
            ('Diabetes', 'Diabetes'),
            ('Hypertension', 'Hypertension'),
            ('High Cholesterol', 'High Cholesterol'),
            ('Asthma', 'Asthma'),
            ('Unknown', 'Unknown')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    family_history = forms.ChoiceField(
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No'),
            ('Unknown', 'Unknown')
        ],
        label='Family History of Heart Disease',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    smoking_status = forms.ChoiceField(
        choices=[
            ('Never', 'Never'),
            ('Former', 'Former'),
            ('Current', 'Current'),
            ('Unknown', 'Unknown')
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )