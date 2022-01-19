from django.urls import path

from CoworkingSite.main import views

urlpatterns = {
    path('', views.MainView.main_view, name='main view')
}
