from django.urls import path

from .views import (ProductListView, ProductDetailView, CommentCreateView, test_translation)


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name='product_comment'),
    path('test_hello/', test_translation,),
]
