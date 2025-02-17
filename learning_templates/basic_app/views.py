from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {
        'text':'hello_world',
        'number':100
    }
    return render(
        request,
        'basic_app/index.html',
        context=context_dict
    )


def other(request):
    return render(
        request,
        'basic_app/other.html'
    )


def relative(request):
    return render(
        request,
        'basic_app/relative_url_templates.html'
    )
