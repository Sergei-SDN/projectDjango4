from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Product.models import Product, Version
from catalog.forms import ProductForm, VersionForm, ModeratorForm
from catalog.services import get_cached_category_for_product


# Create your views here.

class HomeListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        products = Product.objects.all()
        active_versions = {}
        for product in products:
            active_versions[product] = Version.objects.filter(product=product, is_current=True).first()
            context['active_versions'] = active_versions
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'SkyStore'
#     }
#     return render(request, 'catalog/home.html', context)

@login_required()
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        return context


# def product_detail(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'SkyStore {product_item.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'

        # Используем кешированную функцию
        category_list = get_cached_category_for_product()

        context['category_list'] = category_list

        products = Product.objects.all()
        active_versions = {}

        for product in products:
            active_versions[product] = Version.objects.filter(product=product, is_current=True).first()

        context['active_versions'] = active_versions
        return context


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        if self.request.user.is_staff and self.request.user.groups.filter(
                name='moderator').exists():
            return ModeratorForm
        return ProductForm

    def test_func(self):
        _user = self.request.user
        _instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog.set_is_published',
            'catalog.set_category',
            'catalog.set_product_description',
        )
        if _user.is_superuser or _user == _instance.owner:
            return True
        elif _user.groups.filter(name='moderator') or _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        if self.request.user.is_staff and self.request.user.groups.filter(
                name='moderator').exists():
            return ModeratorForm
        return ProductForm

    def test_func(self):
        _user = self.request.user
        _instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog.set_is_published',
            'catalog.set_category',
            'catalog.set_product_description',
        )
        if _user.is_superuser or _user == _instance.owner:
            return True
        elif _user.groups.filter(name='moderator') or _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    template_name = 'catalog/version_form.html'
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    template_name = 'catalog/version_form.html'
    form_class = VersionForm
    permission_required = 'product.change_version_product'
    success_url = reverse_lazy('catalog:home')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     ParentFormset = inlineformset_factory()
    #
    #     return context
    #
    # def form_valid(self, form):
    #     return super().form_valid(form)
