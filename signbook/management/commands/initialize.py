import uuid

from django.core.management.base import BaseCommand

from helios.models import Election, Voter
from helios_auth.auth_systems.password import create_user
from helios_auth.models import User


class Command(BaseCommand):
    args = ''
    help = 'Initialize with example data'

    def handle(self, *args, **options):
        i = 0
        election = Election.objects.first()
        while i < 100:
            username = "mamito{}".format(i)
            email = "{}@{}".format(username, "gmail.com")
            create_user("mamito{}".format(i), "fichitas", name=username, email=email)
            i += 1

        for user in User.objects.all():
            Voter.register_user_in_election(user,election)

        for voter in Voter.objects.all():
            voter.voter_login_id = voter.user.user_id
            voter.voter_password = "mamito"
            voter.save()
