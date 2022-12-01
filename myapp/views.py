from django.shortcuts import render, get_object_or_404


def input_url(request):
    return render(request, 'myapp/index.html')
