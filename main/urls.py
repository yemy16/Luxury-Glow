from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from main.views import (
    show_main,
    create_product_entry,
    edit_product,
    delete_product,
    show_xml,
    show_json,
    show_xml_by_id,
    show_json_by_id,
    register,
    login_user,
    logout_user,
)

from django.urls import include, path
from main.views import show_main, create_product_entry, edit_product, delete_product, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('products/', show_products, name='show_products'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>', delete_product, name='delete_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)