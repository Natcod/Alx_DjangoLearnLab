from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.backends.sqlite3'
    name = 'relationship_app'

    def ready(self):
        import relationship_app.signals  # Import signals when app is ready
