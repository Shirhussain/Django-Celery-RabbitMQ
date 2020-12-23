from django import forms 
from . tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(label="first name", max_length=50, min_length=4, required=False, widget=forms.TextInput(
        attrs={
            "class": "form-control mb-3",
            "placeholder": "first_name",
            "id": "form-first_name"
        }
    ))
    email = forms.EmailField(required=True, max_length=64, widget=forms.TextInput(
        attrs = {
            "class": "form-control mb-3",
            "placeholder": "Type your email",
            "id": "form-email"
        }
    ))
    review = forms.CharField(label="Review", widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": "5"
    }))

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data["name"], self.cleaned_data["email"], self.cleaned_data["review"]
        )
