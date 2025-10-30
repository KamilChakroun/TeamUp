from django.urls import path
from . import views

app_name = 'sessions'

urlpatterns = [
    path('', views.session_list, name='list'),
    path('create/', views.create_session, name='create'),
    # path('chat/', views.chat, name='chat'),
    path('detail/<int:pk>/', views.session_detail, name='detail'),
    path('invite/<int:pk>/', views.invite_users, name='invite'),
    path('respond/<int:invitation_id>/', views.respond_invitation, name='respond'),

    # ✅ Renamed AI insight route
    path('ai-insight/<int:pk>/', views.ai_insight, name='ai_insight'),

    # Edit/Delete
    path('<int:pk>/edit/', views.SessionUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SessionDeleteView.as_view(), name='delete'),

    # Optional separate join path
    path('<int:pk>/request-join/', views.request_join, name='request_join'),

    # Creator manages pending invitations (accept/refuse)
    path('invitation/<int:invitation_id>/manage/', views.manage_invitation, name='manage_invitation'),

    # Page for session creators to manage join requests for a given session
    path('<int:pk>/manage-requests/', views.manage_requests, name='manage_requests'),
    
    #chat
    path('chat/', views.chat_list, name='chat_list'),
    path('<int:session_id>/messages/', views.chat_room, name='chat_room'),
    path('<int:session_id>/send/', views.send_message, name='send_message'),
    path('<int:session_id>/get-messages/', views.get_messages, name='get_messages'),
    
    
    path('message/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('user/<int:user_id>/block/', views.block_user, name='block_user'),
    path('user/<int:user_id>/unblock/', views.unblock_user, name='unblock_user'),
    path('blocked-users/', views.blocked_users_list, name='blocked_users_list'),
]
