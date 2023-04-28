from django.urls import path

from .views import product_detail_view, product_list_create_view, product_alt_view


urlpatterns = [
    path('', product_list_create_view),
	path('<int:pk>/', product_detail_view),
]
