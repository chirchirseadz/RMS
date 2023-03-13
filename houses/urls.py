from django.urls import path

from .  import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('about/', views.about, name='about_page'),
    path('houses/', views.houses, name='houses'),
    path('house/details/<int:id>', views.house_details, name='house_detail'),
    path('available/houses/', views.available_houses,  name='available_houses'),
    path('contacts/', views.contact_page, name='contact'),
    path('house/category/<int:pk>/', views.category_list, name='house_type'),

]


