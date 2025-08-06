from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewForm
from .models import Review


class ReviewView(View):
    def get(self, request):
        data = Review.objects.all()[::-1]
        form = ReviewForm()

        return render(request, "review/review.html", {
            "form": form,
            'data': data,
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('thank_you')
            return HttpResponseRedirect('')

        return render(request, "review/review.html", {
            "form": form,
        })


def thank_you(request):
    return render(request, "review/thank_you.html")
