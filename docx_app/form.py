"""Fields for form"""
from django import forms

class FormData(forms.Form):
    """
    Docstring for MediationForm
    """
    client_name = forms.CharField(label="Client Name")
    branch_address = forms.CharField(
        label="Branch Address"
    )
    tele_no = forms.CharField(label="Telephone No.")
    mobile = forms.CharField(
        label="Mobile No.",
        required=False
    )
    email = forms.EmailField(label="Email ID", required=False)
    customer_name = forms.CharField(label="Customer Name")
    customer_address = forms.CharField(
        label="Customer Address",
        required=False
    )
    customer_tele_no = forms.CharField(label="Customer Telephone No.")
    customer_mobile_no = forms.CharField(
        label="Customer Telephone No.",
        required=False
    )
    customer_email = forms.EmailField(label="Customer Email Id")
