# management/commands/backup_user_data.py
from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True)
        
    def handle(self, *args, **options):
        username = options['username']
        
        # KWETSBAAR: Direct user input in shell command
        cmd = f"mysqldump -u root mydb_users_{username} > backup_{username}.sql"
        subprocess.call(cmd, shell=True)