from django.shortcuts import render, redirect
from .forms import PostCreateFormSet


def add(request):
    formset = PostCreateFormSet(request.POST or None)
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:index')

    context = {
        'formset': formset
    }

    return render(request, 'app/post_formset.html', context)
