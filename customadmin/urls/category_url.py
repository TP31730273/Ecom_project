from django.urls import path
from . import views
app_name='customadmin_customer'

urlpatterns = [
    
    path("customers/", views.CustomerListView.as_view(), name="customers-list"),
    # path("ajax-users", views.UserAjaxPagination.as_view(), name="useraccount-list-ajax"),
    path("customer/create-customer/", views.CustomerCreateView.as_view(), name="customers-create"),
    # path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="useraccount-detailview"),
    # path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="useraccount-update"),
    # path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="useraccount-delete"),
    # path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]
