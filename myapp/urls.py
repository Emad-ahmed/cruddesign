from django import views
from django.urls import path
from myapp.views import HomwView, ShowDetails, Editview, Deleteview, SearchView

urlpatterns = [
    path('', HomwView.as_view(), name='home'),
    path('showdetail', ShowDetails.as_view(), name='showdetail'),
    path('updateview/<int:id>/', Editview.as_view(), name='updateview'),
    path('delteview/<int:id>/', Deleteview.as_view(), name='delteview'),
    path('search', SearchView.as_view(), name='search'),
]
