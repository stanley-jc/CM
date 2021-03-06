import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command
from django.contrib.auth.models import User
from apps.org_accounts.models import OrganisationDetails
from apps.user_accounts.models import UserDetails

class Command(BaseCommand):
    help = 'Shortcut for running the development server'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # get apps list
        apps_dir = os.path.join(settings.BASE_DIR, 'apps')
        to_remove = []
        db_file = os.path.join(settings.BASE_DIR, 'db.sqlite3')

        if os.path.isfile(db_file):
            to_remove.append(db_file)

        for app in os.listdir(apps_dir):
            full_path = os.path.join(apps_dir, app)
            if os.path.isdir(full_path):
                migration_folder = os.path.join(full_path, 'migrations')
                for f in os.listdir(migration_folder):
                    if '__' not in f and 'DS_Store' not in f:  # Don't remove files that aren't migrations
                        migration = os.path.join(migration_folder, f)
                        print(migration)
                        to_remove.append(migration)

        if len(to_remove) == 0:
            print('There are currently no migrations to remove')
            return
        print('This command will remove the following files:')
        for f in to_remove:
            print('\t-', f)

        choice = input('Are you sure you want to do this? (y/N): ')
        if choice not in ['y', 'Y']:
            return

        for f in to_remove:
            try:
                os.unlink(f)
                print('Removed:', f)
            except FileNotFoundError:
                pass

        # Set up admin user again
        call_command('m')
        u = User(username='admin')
        u.set_password('password')
        u.is_superuser = True
        u.is_staff = True
        u.save()

        # Create a staff user
        email = 'a@a.com'
        u = User(username=email, email=email)
        u.set_password('password')
        u.is_superuser = False
        u.is_staff = True
        u.save()

        details = OrganisationDetails(user=u, display_name='Focus Churches')
        details.save()

        # Create a attendee user
        email = 'b@b.com'
        u = User(username=email, email=email)
        u.set_password('password')
        u.is_superuser = False
        u.is_staff = False
        u.save()

        details = UserDetails(user=u, display_name='xXx 1337 h4ck3r xXx')
        details.save()
