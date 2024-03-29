from django.core.management.base import BaseCommand, CommandError
from accounts.models import TimeSlot
from datetime import time, timedelta, datetime, date


class Command(BaseCommand):
    help = 'Populates the database with time slots from 9:00 to 18:00 at 30-minute intervals'

    def handle(self, *args, **options):
        start_time = time(9, 0)
        end_time = time(18, 0)
        interval = timedelta(minutes=30)

        current_time = start_time
        while current_time < end_time:
            TimeSlot.objects.get_or_create(slot_time=current_time)
            # This combines the current time with today's date, adds the interval, and then extracts the time again
            current_time = (datetime.combine(date.today(), current_time) + interval).time()

        self.stdout.write(self.style.SUCCESS('Successfully populated time slots'))
