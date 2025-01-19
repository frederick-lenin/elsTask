from django.urls import path
from.views import add_member,role_create,signup

# from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
# from .views import login_view, protected_view

    
urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('protected/', protected_view, name='protected'),
    # path('myfirst.html/',views.add_member,name='myfirst.html'),
    # path('login_view/',views.login_view, name='login_view'),
    # # path('login_view/<int:id>/', views.login_view, name='login_view'),
    path('add-member/', add_member, name='add_member'),
    path('role-create/', role_create ,name='role_create'),
    path('signup/', signup,  name='signup'),
    



]   
