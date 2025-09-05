from django.core.management.base import BaseCommand
from api.models import Service
from api.services_data import SERVICES


class Command(BaseCommand):
    help = 'Populate services from services_data.py'

    def handle(self, *args, **options):
        for service_id, service_data in SERVICES.items():
            service, created = Service.objects.get_or_create(
                id=service_id,
                defaults={
                    'emoji': service_data['emoji'],
                    'name_en': service_data['name']['en'],
                    'name_hi': service_data['name']['hi'],
                    'name_mr': service_data['name']['mr'],
                    'tagline_en': service_data['tagline']['en'],
                    'tagline_hi': service_data['tagline']['hi'],
                    'tagline_mr': service_data['tagline']['mr'],
                    'before_en': service_data['before']['en'],
                    'before_hi': service_data['before']['hi'],
                    'before_mr': service_data['before']['mr'],
                    'after_en': service_data['after']['en'],
                    'after_hi': service_data['after']['hi'],
                    'after_mr': service_data['after']['mr'],
                    'steps_en': service_data['steps']['en'],
                    'steps_hi': service_data['steps']['hi'],
                    'steps_mr': service_data['steps']['mr'],
                    'perks_en': service_data['perks']['en'],
                    'perks_hi': service_data['perks']['hi'],
                    'perks_mr': service_data['perks']['mr'],
                    'options': service_data['options'],
                    'is_active': True
                }
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created service: {service.name_en}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Service already exists: {service.name_en}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated services!')
        )