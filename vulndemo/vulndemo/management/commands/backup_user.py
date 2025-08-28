# management/commands/backup_user_data.py
from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True)
        
    def handle(self, *args, **options):
        username = options['username']
        
        # KWETSBAAR: Direct user input in shell command
        # Gebruik SQLite dump in plaats van MySQL
        cmd = f"sqlite3 db.sqlite3 '.dump' > backup_{username}.sql"
        subprocess.call(cmd, shell=True)