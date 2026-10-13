from django.urls import path
from . import views


urlpatterns = [

    path(
        "request/",
        views.request_asset,
        name="request_asset"
    ),

]