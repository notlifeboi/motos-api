#motos_api/urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from .views import MotoListApiView, MotoDetailsApiView
from .views import MotoListView, MotoCreateView, MotoEditView, MotoDeleteView
urlpatterns = [
    path('', MotoListView.as_view(), name="Moto_list"),
    # path('<int:moto_id>/', MotoDetailsApiView.as_view(), name="Moto_detail"),
    path('create/', MotoCreateView.as_view(), name="Moto_create"),
    path('update/<int:id>/', MotoEditView.as_view(), name="Moto_update"),
    path('delete/<int:id>/', MotoDeleteView.as_view(), name="Moto_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)