from django.contrib import admin
from django.urls import path

from housing_portal.views import home_view
from house.views import house_create_view, house_detail_view

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('house/create/', house_create_view),
    path('house/<int:id>', house_detail_view),
]
