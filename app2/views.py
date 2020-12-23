from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.edit import FormView 

from .forms import ReviewForm 


class ReviewEmailView(FormView):
    template_name = "review.html"
    form_class = ReviewForm 

    def form_valid(self, form):
        form.send_email()
        msg = "thanks for your review"
        return HttpResponse(msg)
