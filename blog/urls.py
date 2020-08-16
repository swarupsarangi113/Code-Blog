from . import views
from django.urls import path

urlpatterns = [
    path('',views.PostListView.as_view(template_name='blog/home.html'),name='blog-home'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'), 
    path('post/new/',views.PostCreateView.as_view(),name='post-create'), 
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post-delete'), 
    path('about/',views.about,name='blog-about')

]
