from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('thanks/<int:order_id>/', views.thanks, name='thanks'),
    path('history/', views.orderHistory.as_view(), name='order_history'),
    path('<int:order_id>/', views.orderDetail.as_view(), name='order_detail'),
    path('thanks/', views.thank_you, name='thank_you'), # url to appear after review submission
    path('<int:order_id>/feedback/', views.submit_feedback, name='submit_feedback'),
    # path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('feedbacks/', views.latest_feedbacks, name='latest_feedbacks'),
]