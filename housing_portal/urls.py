from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from housing_portal.views import home_view
from house.views import house_create_view, house_detail_view, house_search_view
from accounts.views import login_view, logout_view, register_view, profile, profile_view
from rents.views import rent_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path("house/", house_search_view),
    path('house/create/', house_create_view, name='house-create'),
    path('house/<str:slug>', house_detail_view, name='house-detail'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", register_view, name='register'),
    path("profile/", profile, name='profile'),
    path("profile/<str:username>", profile_view, name='profile-view'),
    path("rent/", rent_view, name='rent'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
