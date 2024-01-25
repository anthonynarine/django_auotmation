from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # to run this command in the terminal python manage.py helloworld --help
    # ever command in django has help ex python manage.py runserver --help
    help = "Prints hello Julia"
    

