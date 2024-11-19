from django.urls import path
from . import views
from .views import AllScoreView, JapanScoreView,EnglishScoreView,MathScoreView


from django.conf import settings
from django.conf.urls.static import static


app_name = 'scoreapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateScoreView.as_view(), name='post'),  # ショップ投稿の作成
    path('buy/', views.CreateScoreView.as_view(), name='buy'),    
    path('all_score/', AllScoreView.as_view(), name='all_score'),  
    path('japan/', JapanScoreView.as_view(), name='japan'), 
    path('english/', EnglishScoreView.as_view(), name='english'),
    path('math/', MathScoreView.as_view(), name='math'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
