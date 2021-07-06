from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from School import settings
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control


urlpatterns = [
    path("register/",views.register_user , name="register"),
    path("login/",views.LoginUser.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),{"next_page":settings.LOGOUT_REDIRECT_URL},name="logout")

]
