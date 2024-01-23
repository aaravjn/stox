from django.apps import AppConfig

class BsestoxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bsestox'

    def ready(self):
        from .startup import import_data
        import_data()