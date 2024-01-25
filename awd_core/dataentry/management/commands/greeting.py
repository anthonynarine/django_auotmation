
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

# Proposed command  = python manage.py greeting any name
# Proposed output  = Hi {name}, good morning
class Command(BaseCommand):
    help = "Greet the user"
    
    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Specifies user name")
        # python manage.py greeting --help will display the arument and command help text
    
    def handle(self, *args, **kwargs):
        # Write your logic
        name = kwargs["name"]
        greeting = f"Hello {name}, good morning"
        self.stdout.write(self.style.SUCCESS(greeting))