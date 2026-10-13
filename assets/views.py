from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AssetRequestForm


@login_required
def request_asset(request):

    if request.method == "POST":

        form = AssetRequestForm(request.POST)

        if form.is_valid():

            asset = form.save(commit=False)

            asset.employee = request.user

            asset.save()

            return redirect("asset_history")

    else:
        form = AssetRequestForm()

    return render(
        request,
        "assets/request_asset.html",
        {"form": form}
    )