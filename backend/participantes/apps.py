from django.apps import AppConfig

class ParticipantesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "participantes"
    

    def ready(self):
        
        from . import create_admin
        create_admin.run()