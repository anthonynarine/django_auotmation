from django.core.management import BaseCommand
from django.core.management.base import CommandParser

# Proposed command  = python manage.py greeting
# Proposed output  = Hi {name}, good morning
class Command(BaseCommand):
    help = "Greet the user"
    
    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Specifies user name")
    
    def handle(self, *args, **kwargs):
        # Write your logic
        self.stdout.write("Hi Julia, Good Morning")