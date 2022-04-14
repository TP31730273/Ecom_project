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
from app.models import *
# class CustomerDetailView(MyDetailView):
#     template_name = "customadmin/adminuser/user_detail.html"
#     context = {}

#     def get(self, request, pk):
#         self.context['user_detail'] = Customers.objects.filter(pk=pk).first()
#         # self.context['purchased_products'] = PurchasedProduct.objects.filter(user=pk)
#         # self.context['booked_services'] = BookedService.objects.filter(user=pk)
#         return render(request, self.template_name, self.context)



# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------

class CustomerListView(MyListView):
    """View for User listing"""
    paginate_by = 25
    ordering = ["id"]
    model = Customers
    queryset = model.objects.exclude(is_staff=True).order_by('-id')
    template_name = "customadmin/adminuser/customer_list.html"
    permission_required = ("customadmin.view_user",)
    
    def get_queryset(self):
        return self.model.objects.exclude(is_staff=True).exclude(email=self.request.user).exclude(email=None).order_by('-id')


class CustomerCreateView(MyCreateView):
    """View to create User"""

    model = Customers
    form_class = UserCreationForm
    template_name = "customadmin/adminuser/user_form.html"
    permission_required = ("customadmin.add_user",)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs["user"] = self.request.user
        return kwargs

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("customadmin:useraccount-list")
    

# class CustomerUpdateView(MyUpdateView):
#     """View to update User"""

#     model = Customers
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

# class CustomerDeleteView(MyDeleteView):
#     """View to delete User"""

#     model = Customers
#     template_name = "customadmin/confirm_delete.html"
#     permission_required = ("customadmin.delete_user",)

#     def get_success_url(self):
#         opts = self.model._meta
#         return reverse("customadmin:useraccount-list")