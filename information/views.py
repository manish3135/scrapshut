from django.shortcuts import render
from .models import Information
from . import forms
from django.shortcuts import redirect

def information_list(request):
    Info = Information.objects.all()
    return render(request, 'information_list.html', {'Info': Info})

def add_detail(request):
    if request.method == "POST":
        form = forms.Adddetail(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('information:list')
        else:
            return render(request, 'adddetail.html', {'form': form})

    else:
        form = forms.Adddetail()
        return render(request, 'adddetail.html', {'form': form})
