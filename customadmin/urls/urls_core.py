from django.urls import path
from . import views

app_name='customadmin'

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
        # User
    path("users/", views.UserListView.as_view(), name="useraccount-list"),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="useraccount-list-ajax"),
    path("users/create/", views.UserCreateView.as_view(), name="useraccount-create"),
    path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="useraccount-detailview"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="useraccount-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="useraccount-delete"),
    path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]

