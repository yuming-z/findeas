from django.urls import path

from . import views

urlpatterns = [
    path('validate/', views.validate, name='validate'),

    path('find-ticker', views.query_ticker, name='query_ticker'),
    path('query', views.query_stock, name='query_stock')
]