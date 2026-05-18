from rest_framework import serializers
from dateutil.rrule import rrulestr
from django.utils import timezone
import datetime
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    next_occurrences = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__' 
        extra_kwargs = {'user': {'read_only': True}}

    def get_next_occurrences(self, obj):
        if not obj.rrule_rule or not obj.start_date:
            return []

        try:
            now = timezone.now()

            start_datetime = datetime.datetime.combine(obj.start_date, datetime.time.min)
            start_aware = timezone.make_aware(start_datetime)

            start_utc = start_aware.astimezone(datetime.timezone.utc)
            rrule_string = f"DTSTART:{start_utc.strftime('%Y%m%dT%H%M%SZ')}\nRRULE:{obj.rrule_rule}"
            
            rule = rrulestr(rrule_string)

            occurrences = rule.between(
                now, 
                now + datetime.timedelta(days=30), 
                inc=True
            )

            return [date.date() for date in occurrences[:3]]

        except Exception:
            return []
