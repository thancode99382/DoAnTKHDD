from django import forms

from applications.models import CV


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ["file", "full_name", "email", "phone_number"]

        labels = {
            "full_name": "Họ và tên",
            "email": "Email",
            "phone_number": "Số điện thoại",
            "file": "CV",
        }