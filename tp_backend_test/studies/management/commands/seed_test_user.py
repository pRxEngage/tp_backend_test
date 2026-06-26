from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create or update the local admin user used for the assessment."

    def add_arguments(self, parser):
        parser.add_argument("--email", default="admin@example.com")
        parser.add_argument("--password", default="password123")

    def handle(self, *args, **options):
        email = options["email"]
        password = options["password"]
        user_model = get_user_model()
        user, created = user_model.objects.update_or_create(
            email=email,
            defaults={
                "is_active": True,
                "is_staff": True,
                "is_superuser": True,
            },
        )
        user.set_password(password)
        user.save(update_fields=["password", "is_active", "is_staff", "is_superuser"])

        action = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{action} admin user {email}"))
