# -*- coding: utf-8 -*-
from django.urls import include, path

from .. import views

from . import urls_core, urls_auth,customer_url,seller_url,product_url,category_url

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
    path("", include(urls_auth)),
    path("", include(urls_core)),
    path("", include(customer_url)),
]