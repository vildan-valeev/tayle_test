from django.urls import path, include


from apps.account.views import AccountDetail

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('current/', AccountDetail.as_view(), name='account-detail'),
]
