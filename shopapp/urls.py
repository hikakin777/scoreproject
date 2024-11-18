from django.urls import path
from . import views
from .views import AllShopView, JapanShopView,EnglishShopView,MathShopView


from django.conf import settings
from django.conf.urls.static import static


app_name = 'shopapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateShopView.as_view(), name='post'),  # ショップ投稿の作成
    path('buy/', views.CreateShopView.as_view(), name='buy'),    
    path('all_shop/', AllShopView.as_view(), name='all_shop'),  
    path('japan/', JapanShopView.as_view(), name='japan'), 
    path('english/', EnglishShopView.as_view(), name='english'),
    path('math/', MathShopView.as_view(), name='math'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
