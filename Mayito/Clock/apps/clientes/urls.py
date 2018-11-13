from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #Para que no haya conflicto con las views normales
from django.conf.urls import url
from django.urls import reverse_lazy
from . import views 

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name="login"), #vista de login
    path('logout/',auth_views.LogoutView.as_view(), name="logout"), #vista de logout
    path('enter/',include("apps.comprar.urls")),
    path('registrate/',views.registrate, name="registrate"),
    path('password/recovery/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',html_email_template_name='registration/password_reset_email.html'),name='password_reset'),
    path('password/recovery/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),

    url(
    	r'^password/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
    	r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    	auth_views.PasswordResetConfirmView.as_view(
    		success_url= reverse_lazy('inicio'),
    		post_reset_login=True,
    		template_name='registration/password_reset_confirm.html',
    		post_reset_login_backend=('django.contrib.auth.backends.AllowAllUsersModelBackend'
    		),
    	),
    	name='password_reset_confirm'
    	),
]