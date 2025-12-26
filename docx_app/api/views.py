"""apis for our application"""
from django.views import View
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render
from docx_app.form import FormData
from docx_app.utils import generate_docx


class GenerateMediationDocView(View):
    """Get and post request for form data """

    template_name = 'form.html'

    def get(self, request):
        """To fetch form details"""
        form = FormData()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Handle form submission and document generation."""
        form = FormData(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        try:
            docx_buffer = generate_docx(form.cleaned_data)
            response = FileResponse(
                    docx_buffer,
                    as_attachment=True,
                    filename='Mediation_Application.docx',
                )
            return response
        except Exception:
            messages.error(
                request,
                "An error occurred while generating your document. Please try again."
            )
            return render(request, self.template_name, {'form': form})
