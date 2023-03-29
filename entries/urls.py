from .import views
from django.urls import path

urlpatterns = [
    path('hello/', views.say_hello,name='hello'),
    path('signup/', views.signup,name='Signup'),
    path('login/', views.login,name='login'),
    path('', views.landing,name='landing'),
    path('app/', views.app,name='app'),
    path('logout/', views.logout,name='logout'),
    path( 'list/', views.EntryListView.as_view(),name="entry-list"),
    path('entry/<int:pk>',views.EntryDetailView.as_view(),name="entry-detail"),
    path(
        "create",
        views.EntryCreateView.as_view(),
        name="entry-create"
    ),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),

]


