from django.apps import AppConfig

class OneloveappConfig(AppConfig):
    """
    AppConfig for the 'oneloveapp' Django app.

    Attributes:
        default_auto_field (str): The default auto field for model primary keys.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oneloveapp'
