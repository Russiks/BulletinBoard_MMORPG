from django.urls import path

from .views import (
    BoardList, BoardDetail, BoardCreate, BoardEdit, BoardDelete, FeedbackList,
    FeedbackDetail, FeedbackCreate, FeedbackDelete, feedback_activ, feedback_deactive
)

urlpatterns = [
    path('', BoardList.as_view(), name='board_list'),
    path('<int:pk>/', BoardDetail.as_view(), name='board_detail'),
    path('create/', BoardCreate.as_view(), name='board_create'),
    path('<int:pk>/delete/', BoardDelete.as_view(), name='board_delete'),
    path('<int:pk>/update/', BoardEdit.as_view(), name='board_edit'),
    path('feedback/', FeedbackList.as_view(), name='feedback_list'),
    path('<int:pk>/<int:pk_feed>/', FeedbackDetail.as_view(), name='feedback_detail'),
    path('<int:pk>/response_create/', FeedbackCreate.as_view(), name='feedback_create'),
    path('<int:pk>/<int:pk_feed>/feedback_delete/', FeedbackDelete.as_view(), name='feedback_delete'),
    path('<int:pk>/<int:pk_feed>/feedback_active/', feedback_activ, name='feedback_active'),
    path('<int:pk>/<int:pk_feed>/feedback_deactive/', feedback_deactive, name='feedback_deactive'),
]
