"""Urls are defined here"""
from django.urls import path
from docx_app.api.views import GenerateMediationDocView

urlpatterns = [
    path('', GenerateMediationDocView.as_view(), name='generate_doc'),
]
