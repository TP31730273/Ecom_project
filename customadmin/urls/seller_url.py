from django.urls import path
from . import views
app_name='customadmin_seller'

urlpatterns = [
    
    path("sellers/", views.SellerListView.as_view(), name="sellers-list"),
    # path("ajax-users", views.UserAjaxPagination.as_view(), name="useraccount-list-ajax"),
    path("seller/create-seller/", views.SellerCreateView.as_view(), name="sellers-create"),
    path("seller/<int:pk>/detail/", views.SellerDetailView.as_view(), name="sellers-detailview"),
    path("seller/<int:pk>/update/", views.SellerUpdateView.as_view(), name="sellers-update"),
    path("seller/<int:pk>/delete/", views.SellerDeleteView.as_view(), name="sellers-delete"),
    # path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]
