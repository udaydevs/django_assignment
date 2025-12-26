"""Fields for form"""
from django import forms
from django.core.validators import RegexValidator


class FormData(forms.Form):
    """
    Docstring for MediationForm
    """
    client_name = forms.CharField(
        label="Client Name",
        validators=[RegexValidator(r'^[A-Za-z\s]{2,50}$', "Only letters allowed.")]
    )
    branch_address = forms.CharField(
        label="Branch Address"
    )
    tele_no = forms.CharField(
        label="Telephone No.",
        validators=[RegexValidator(r'^[6-9]\d{9}$', "Enter valid 10-digit phone number.")]
    )
    mobile = forms.CharField(
        label="Mobile No.",
        required=False,
        validators=[RegexValidator(r'^[6-9]\d{9}$', "Enter valid 10-digit phone number.")]
    )
    email = forms.EmailField(
        label="Email ID",
        required=True
    )
    customer_name = forms.CharField(
        label="Customer Name",
        validators=[RegexValidator(r'^[A-Za-z\s]{2,50}$', "Only letters allowed.")]
    )
    customer_address = forms.CharField(
        label="Customer Address",
        required=False
    )
    customer_tele_no = forms.CharField(
        label="Customer Telephone No.",
        validators=[RegexValidator(r'^[6-9]\d{9}$', "Enter valid 10-digit phone number.")]

    )
    customer_mobile_no = forms.CharField(
        label="Customer Telephone No.",
        required=False,
        validators=[RegexValidator(r'^[6-9]\d{9}$', "Enter valid 10-digit phone number.")]
    )
    customer_email = forms.EmailField(label="Customer Email Id")
