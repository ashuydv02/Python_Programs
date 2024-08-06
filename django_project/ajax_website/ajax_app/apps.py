from django.apps import AppConfig


class AjaxAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ajax_app"

    def ready(self):
        import ajax_app.signals