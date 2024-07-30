from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Paste
from .forms import AddPasteForm
from .utils import random_url, is_less_than_1mb


URL_LENGTH = 6


def create_paste(request):
    if request.method == "POST":
        url = random_url(URL_LENGTH)
        data = request.POST.copy()
        if is_less_than_1mb(data.get("text")):
            if not data.get("url").strip():
                data.update({"url": url})

            form = AddPasteForm(data=data)
            if form.is_valid():
                form.save()

                return redirect(reverse("pastes:show", args=(data["url"],)))

        form = AddPasteForm(data=request.POST)
    else:

        form = AddPasteForm()
    context = {"form": form}
    return render(request, "pastes/create_paste.html", context)


def show_paste(request, pk):
    context = {"paste": Paste.not_expired.get(url=pk)}
    return render(request, "pastes/show_paste.html", context)
