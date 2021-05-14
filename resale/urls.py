from django.conf.urls import url
from django.urls import path
from .views import AllAdsView, ProductView, CategoryView
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('indexlogin', views.indexlogin, name = "indexlogin"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logoutUser, name="logout"),
    path('postad', views.postad, name="postad"),
    path('allads', AllAdsView.as_view(), name="allads"),
    path('product/<int:pk>', ProductView.as_view(), name="product-details"),
    path('category/<str:cats>/', CategoryView, name="category"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
