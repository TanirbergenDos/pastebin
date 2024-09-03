from django.shortcuts import redirect, render
from django.utils.timezone import timedelta, now

from .models import Paste
from .forms import AddPasteForm
from .utils import random_url, is_less_than_1mb

URL_LENGTH = 6
EXPIRATION_DATE = timedelta(days=1)


def create_paste(request):
    if request.method == "POST":
        data = request.POST.copy()
        
        if is_less_than_1mb(data.get("text")):
            if not data.get("url").strip():
                data.update({"url": random_url(URL_LENGTH)})

            if not data.get("expired_at"):
                data.update({"expired_at": now() + EXPIRATION_DATE})

            form = AddPasteForm(data=data)
            if form.is_valid():
                paste = form.save()
                return redirect(paste.get_absolute_url())

        else:
            form = AddPasteForm(data=data)

    else:
        form = AddPasteForm()
    context = {"form": form}
    return render(request, "pastes/create_paste.html", context)


def show_paste(request, pk):
    context = {"paste": Paste.not_expired.get(url=pk)}
    return render(request, "pastes/show_paste.html", context)
