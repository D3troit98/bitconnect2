from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit/<int:uniqueid>/', views.polling_unit_result, name='polling_unit_result'),
    path('select_lga/', views.select_lga, name='select_lga'),
    path('lga_polling_unit_results/', views.lga_polling_unit_results, name='lga_polling_unit_results'),
    path('new_polling_unit_result/', views.new_polling_unit_result, name='new_polling_unit_result'),
]
