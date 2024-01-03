from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    text = _('Hello World this is going to translate in persian')
    return render(request, 'home.html', {'text': text})
