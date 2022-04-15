from django.urls import path
from . import views
app_name='customadmin_product'

urlpatterns = [
    
    path("products/", views.ProductListView.as_view(), name="product-list"),
    # path("ajax-users", views.UserAjaxPagination.as_view(), name="useraccount-list-ajax"),
    path("product/create-product/", views.ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/detail/", views.ProductDetailView.as_view(), name="product-detailview"),
    path("product/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product-update"),
    # path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="useraccount-delete"),
    # path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]
