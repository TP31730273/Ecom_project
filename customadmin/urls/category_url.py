from django.urls import path
from . import views
app_name='customadmin_category'

urlpatterns = [
    
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    # path("ajax-users", views.UserAjaxPagination.as_view(), name="useraccount-list-ajax"),
    path("category/create-category/", views.CategoryCreateView.as_view(), name="category-create"),
    # path("users/<int:pk>/detail/", views.UserDetailView.as_view(), name="useraccount-detailview"),
    path("category/<int:pk>/update/", views.CategoryUpdateView.as_view(), name="category-update"),
    path("category/<int:pk>/delete/", views.CategoryDeleteView.as_view(), name="category-delete"),
    # path("export_user_csv", views.export_user_csv, name="export_user_csv"),
]
