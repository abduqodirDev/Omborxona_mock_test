from django.urls import path
from .views import OmborxonaView

urlpatterns = [
    path('get-material/', OmborxonaView.as_view())
]
