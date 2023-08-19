from django.apps import AppConfig


class Part1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'part1'

    def ready(self):
        import part1.signals
