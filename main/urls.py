from django.urls import path
from main.views import show_main, create_product_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]