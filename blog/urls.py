from django.urls import path

from .views import(
        BlogListView ,
        BlogDetailView,
        BlogCreateView,
        BlogUpdateView,
        BlogDeleteView,
) 


urlpatterns = [
    
    path('post/<int:pk>/delete/',
            BlogDeleteView.as_view() , name='post_delete'),

    path('post/<int:pk>/edit/',
            BlogUpdateView.as_view(), name='post_edit'),

    path('post/new/' , BlogCreateView.as_view(), name='post_new'),               #new 2

    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #new added

    path('' , BlogListView.as_view(), name='home')    
]