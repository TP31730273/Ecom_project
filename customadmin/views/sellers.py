from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyDetailView,
    MyLoginRequiredView,
    MyUpdateView,
)
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import TemplateView, DetailView
from django_datatables_too.mixins import DataTableMixin

from ..forms import UserChangeForm, UserCreationForm
from django.shortcuts import reverse, render

# from customadmin.models import User, PurchasedProduct, BookedService
from app.models import Sellers
# class UserDetailView(MyDetailView):
#     template_name = "customadmin/adminuser/user_detail.html"
#     context = {}

#     def get(self, request, pk):
#         self.context['user_detail'] = UserAccount.objects.filter(pk=pk).first()
#         # self.context['purchased_products'] = PurchasedProduct.objects.filter(user=pk)
#         # self.context['booked_services'] = BookedService.objects.filter(user=pk)
#         return render(request, self.template_name, self.context)



# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------

class SellerListView(MyListView):
    """View for User listing"""
    paginate_by = 25
    ordering = ["id"]
    model = Sellers
    queryset = model.objects.exclude(is_staff=True).order_by('-id')
    template_name = "customadmin/adminuser/seller_list.html"
    permission_required = ("customadmin.view_user",)
    
    def get_queryset(self):
        return self.model.objects.exclude(is_staff=True).exclude(email=self.request.user).exclude(email=None).order_by('-id')

# class UserAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
#     """Built this before realizing there is
#     https://bitbucket.org/pigletto/django-datatables-view."""

#     model = UserAccount
#     queryset = UserAccount.objects.all()

#     def _get_is_superuser(self, obj):
#         """Get boolean column markup."""
#         t = get_template("customadmin/partials/list_boolean.html")
#         return t.render({"bool_val": obj.is_superuser})

#     def _get_actions(self, obj, **kwargs):
#         """Get actions column markup."""
#         # ctx = super().get_context_data(**kwargs)
#         t = get_template("customadmin/partials/list_basic_actions.html")
#         # ctx.update({"obj": obj})
#         # print(ctx)
#         return t.render({"o": obj})

#     def filter_queryset(self, qs):
#         """Return the list of items for this view."""
#         # If a search term, filter the query
#         if self.search:
#             return qs.filter(
#                 Q(username__icontains=self.search)
#                 # | Q(state__icontains=self.search)
#                 # | Q(year__icontains=self.search)
#             )
#         return qs

#     def prepare_results(self, qs):
#         # Create row data for datatables
#         data = []
#         for o in qs:
#             data.append(
#                 {
#                     "username": o.username,
#                     "is_superuser": self._get_is_superuser(o),
#                     # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
#                     # "actions": self._get_actions(o),
#                 }
#             )
#         return data

#     """Built this before realizing there is
#     https://bitbucket.org/pigletto/django-datatables-view."""


#     def _get_is_superuser(self, obj):
#         """Get boolean column markup."""
#         t = get_template("customadmin/partials/list_boolean.html")
#         return t.render({"bool_val": obj.is_superuser})

#     def _get_actions(self, obj, **kwargs):
#         """Get actions column markup."""
#         # ctx = super().get_context_data(**kwargs)
#         t = get_template("customadmin/partials/list_basic_actions.html")
#         # ctx.update({"obj": obj})
#         # print(ctx)
#         return t.render({"o": obj})

#     def filter_queryset(self, qs):
#         """Return the list of items for this view."""
#         # If a search term, filter the query
#         if self.search:
#             return qs.filter(
#                 Q(username__icontains=self.search)
        
#                 # | Q(state__icontains=self.search)
#                 # | Q(year__icontains=self.search)
#             )
#         return qs

#     def prepare_results(self, qs):
#         # Create row data for datatables
#         data = []
#         for o in qs:
#             data.append(
#                 {
#                     "username": o.username,
                    
#                     "is_superuser": self._get_is_superuser(o),
#                     # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                   
#                 }
#             )
#         return data

# class UserCreateView(MyCreateView):
#     """View to create User"""

#     model = UserAccount
#     form_class = UserCreationForm
#     template_name = "customadmin/adminuser/user_form.html"
#     permission_required = ("customadmin.add_user",)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         # kwargs["user"] = self.request.user
#         return kwargs

#     def get_success_url(self):
#         # opts = self.model._meta
#         return reverse("customadmin:useraccount-list")
    

# class UserUpdateView(MyUpdateView):
#     """View to update User"""

#     model = UserAccount
#     form_class = UserChangeForm
#     template_name = "customadmin/adminuser/user_form_update.html"
#     permission_required = ("customadmin.change_user",)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         # kwargs["user"] = self.request.user
#         return kwargs

#     def get_success_url(self):
#         # opts = self.model._meta
#         return reverse("customadmin:useraccount-list")

# class UserDeleteView(MyDeleteView):
#     """View to delete User"""

#     model = UserAccount
#     template_name = "customadmin/confirm_delete.html"
#     permission_required = ("customadmin.delete_user",)

#     def get_success_url(self):
#         opts = self.model._meta
#         return reverse("customadmin:useraccount-list")