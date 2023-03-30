from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, reverse, render
from django.utils.translation import gettext as _
from django.http import HttpResponse
from django.contrib import messages

from .models import (Product, Comment)
from .forms import CommentForms
from cart.forms import AddToCartProductForm


def test_translation(request):
    result = _('hello')
    messages.success(request, 'this is a success message.')
    messages.error(request, 'this is a error message.')
    messages.info(request, 'this is a info message.')
    messages.warning(request, 'this is a warning message.')
    return render(request, 'test_hello.html')


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForms()
        # context['add_to_cart_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForms

    def form_valid(self, form):
        # return super().form_valid(form)
        obj = form.save(commit=False)
        obj.author = self.request.user

        pk = int(self.kwargs['pk'])
        product = get_object_or_404(Product, id=pk)
        obj.product = product
        messages.success(self.request, _('Comment successfully created'))
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('product_list', )
