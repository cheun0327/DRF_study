from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users.models import User


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many users do you want to create?",
        )

    def handle(self, *args, **options):

        number = options.get("number", 1)
        seeder = Seed.seeder()
        # 장고 user에서 자동으로 설정하는 것들 꺼주기
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!!"))
