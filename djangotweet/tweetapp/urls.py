from django.urls import path
from . import views
from .views import SignUpView

app_name='tweetapp'

urlpatterns = [
    path('',views.listTweet,name='listTweet'),
    path('addTweet/',views.addTweet,name='addTweet'),
    path('addtweetbyform/',views.addtweetbyform,name='addtweetbyform'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('deletetweet/<int:id>',views.deletetweet,name='deletetweet')



]
