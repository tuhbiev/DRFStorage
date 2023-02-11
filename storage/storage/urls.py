from django.contrib import admin
from django.urls import path, include, re_path
from mainapp.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/product/', ProductAPIList.as_view()),
    path('api/product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/productdelete/<int:pk>/', ProductAPIDestroy.as_view()),

    path('api/category/', CategoryAPIList.as_view()),
    path('api/category/<int:pk>/', CategoryAPIUpdate.as_view()),
    path('api/categorydelete/<int:pk>/', CategoryAPIDestroy.as_view()),

    path('api/price/', PriceAPIList.as_view()),
    path('api/price/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/pricedelete/<int:pk>/', PriceAPIDestroy.as_view()),


    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

