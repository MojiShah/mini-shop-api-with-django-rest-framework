from django.urls import path;
from .views import (ProductListCreateView,ProductDetailView)

app_name = "products"

url_patterns=[
    path("",ProductListCreateView.as_view(),name="product-list-create",),
    path("<int:pk>/",ProductDetailView.as_view(),name="product-detail",),
]