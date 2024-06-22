from string import ascii_lowercase
from random import choice
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Paste

RESULT = ascii_lowercase + "0123456789"
def random_url():
    return ''.join(choice(RESULT) for _ in range(8))



def create_paste(request):
    if request.method == "POST":
        url = random_url()
        Paste.objects.create(text=request.POST["text"], url=url)
        return HttpResponseRedirect(reverse("pastes:show", args=(url,)))
    return render(request, "pastes/create_paste.html")

def show_paste(request, pk):
    context = {
        "paste": Paste.objects.get(url=pk)
    }
    return render(request, "pastes/show_paste.html", context)