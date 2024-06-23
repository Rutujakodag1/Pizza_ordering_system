# # urls.py
# from django.urls import path
# from .views import pizza_detail

# urlpatterns = [
#     path('pizza/<int:pizza_id>/', pizza_detail, name='pizza_detail'),
# ]



from django.urls import path
from .views import pizza_detail, home

urlpatterns = [
    path('pizza/<int:pizza_id>/', pizza_detail, name='pizza_detail'),
    path('', home, name='home'),
]
