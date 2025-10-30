# apps/sessions/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

# Exemple de choix de sports
SPORT_CHOICES = [
    ('soccer', 'Soccer'),
    ('basketball', 'Basketball'),
    ('tennis', 'Tennis'),
    ('running', 'Running'),
    # ajouter d'autres si nécessaire
]

STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('proposed', 'Proposed'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
    ('completed', 'Completed'),
]

INVITATION_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('refused', 'Refused'),
    ('rescheduled', 'Rescheduled'),
]


class Session(models.Model):
    sport_type = models.CharField(max_length=20, choices=SPORT_CHOICES)
    start_datetime = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_sessions'
    )
    invitees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Invitation',
        related_name='invited_sessions'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sport_type} session on {self.start_datetime.date()}"

    def is_upcoming(self):
        return self.start_datetime > timezone.now()


class Invitation(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    invitee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=INVITATION_STATUS_CHOICES, default='pending')
    response_notes = models.TextField(blank=True)
    rescheduled_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Invite to {self.session} for {self.invitee.email}"


class ChatRoom(models.Model):
    """Salon de chat pour une session"""
    session = models.OneToOneField('Session', on_delete=models.CASCADE, related_name='chat_room')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Chat Room'
        verbose_name_plural = 'Chat Rooms'
    
    def __str__(self):
        return f"Chat for {self.session}"
    
    def get_participants(self):
        """Retourne tous les participants (créateur + invités acceptés)"""
        accepted_invitees = self.session.invitees.filter(
            invitation__status='accepted'
        )
        return [self.session.creator] + list(accepted_invitees)

# MODIFIER le modèle Message existant pour ajouter is_deleted
class Message(models.Model):
    """Message dans un salon de chat"""
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)    
    
    is_deleted = models.BooleanField(default=False, help_text="Message supprimé")
    deleted_at = models.DateTimeField(null=True, blank=True, help_text="Date de suppression")
    

    attachment = models.FileField(upload_to='chat_attachments/', blank=True, null=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"
    
    def mark_as_read(self):
        """Marquer le message comme lu"""
        self.is_read = True
        self.save(update_fields=['is_read'])
    
    def soft_delete(self):
        """Suppression logique du message"""
        from django.utils import timezone
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

class MessageReadReceipt(models.Model):
    """Suivi de lecture des messages par utilisateur"""
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='read_receipts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['message', 'user']
        verbose_name = 'Message Read Receipt'
        verbose_name_plural = 'Message Read Receipts'
    
    def __str__(self):
        return f"{self.user.username} read message {self.message.id}"


class BlockedUser(models.Model):
    """Utilisateurs bloqués par un utilisateur"""
    blocker = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='blocked_users'
    )
    blocked = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='blocked_by'
    )
    blocked_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True, help_text="Raison du blocage (optionnel)")
    
    class Meta:
        unique_together = ['blocker', 'blocked']
        verbose_name = 'Blocked User'
        verbose_name_plural = 'Blocked Users'
        ordering = ['-blocked_at']
    
    def __str__(self):
        return f"{self.blocker.username} blocked {self.blocked.username}"



# Optionnel, stub pour IA / suggestions
class SuggestedSlot(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='suggestions')
    proposed_datetime = models.DateTimeField()
    rationale = models.TextField()

    def __str__(self):
        return f"Suggested slot for {self.session} at {self.proposed_datetime}"
