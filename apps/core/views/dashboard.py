from django.shortcuts import render, redirect
from apps.core.forms.dashboard import DeveloperModelForm


def dashboard(request):
    form = DeveloperModelForm()
    if request.method == "POST":
        form = DeveloperModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin:index")
        else:
            print(form.errors)

    return render(request, "base.html", {"form": form})
