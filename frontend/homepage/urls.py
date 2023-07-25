from django.urls import path
from homepage import views
from django.views.generic import RedirectView

urlpatterns = [
    path('summarize/', views.homepage, name='homepage'),
    path('submit/', views.get_data, name='submit_data'),
    path('', RedirectView.as_view(url='/summarize/', permanent=True))
]