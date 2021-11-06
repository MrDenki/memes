from django.conf.urls.static import static
from django.urls import path, re_path

from base.views import main, authorization, registration, memes, profile, add_memes, logout_user
from memes import settings

urlpatterns = [
    path('', main, name='home'),
    path('authorization/', authorization, name='authorization'),
    path('registration/', registration, name='registration'),
    path('memes/', memes, name='memes'),
    re_path('profile/(\d+)', profile, name='profile'),
    path('add_memes/', add_memes, name='add_memes'),
    path('logout_user/', logout_user, name='logout_user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)