from django.shortcuts import redirect, render
from django.contrib import messages
# from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, ('An error prevented the item from being added to the list. Please try again'))

        messages.success(request, ('Item has been successfully added to the list'))
        list = List.objects.all()
        context = {
            'list': list,
        }
        return render(request, 'home.html', context)

    else:
        list = List.objects.all()
        context = {
            'list': list,
        }
        return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been successfully deleted from the list'))
    return redirect('home')

def action(request, list_id):
    item = List.objects.get(pk=list_id)
    if item.is_completed:
        item.is_completed = False
    else:
        item.is_completed = True
    item.save()
    return redirect('home')