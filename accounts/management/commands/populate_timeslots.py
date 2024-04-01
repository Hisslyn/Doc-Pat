from django.core.management.base import BaseCommand
from accounts.models import TimeSlot
from datetime import datetime, time, timedelta

class Command(BaseCommand):
    help = 'Populates the database with time slots from 9:00 to 18:00 at 30-minute intervals'

    def handle(self, *args, **options):
        start_time = time(9, 0)
        end_time = time(18, 0)
        interval = timedelta(minutes=30)

        current_time = start_time
        while current_time < end_time:
            # Here we assume that if the timeslot already exists, its availability doesn't change.
            timeslot, created = TimeSlot.objects.get_or_create(
                slot_time=current_time,
                defaults={'is_available': True}  # This sets is_available only if the timeslot is being created
            )
            current_time = (datetime.combine(datetime.today(), current_time) + interval).time()

        self.stdout.write(self.style.SUCCESS('Successfully populated time slots'))
