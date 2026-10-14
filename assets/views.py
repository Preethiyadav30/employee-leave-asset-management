from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AssetRequestForm

@login_required
def request_asset(request):
    print("Request method:", request.method)

    if request.method == "POST":
        form = AssetRequestForm(request.POST)
        print("Form valid:", form.is_valid())

        if form.is_valid():
            asset = form.save(commit=False)
            asset.employee = request.user
            asset.save()

            print("Asset saved successfully!")

            messages.success(
                request,
                "Your asset request has been submitted successfully!"
            )
            return redirect("request_asset")
        else:
            print("Form errors:", form.errors)
    else:
        form = AssetRequestForm()

    return render(
        request,
        "assets/request_asset.html",
        {"form": form}
    )