class Clock(object):
    def __init__(self, hour, minutes=00):
        self.minutes = minutes
        self.hour = hour
        self.total_minutes= hour*60+minutes

    @classmethod
    def at(cls, hour, minutes=00):
        return cls(hour, minutes)

    def __str__(self):
        return "%02d:%02d" % (self.hour, self.minutes)

    def __add__(self,minutes):
        total_time=self.total_minutes+minutes
        new_hour=total_time/60
        new_min=total_time%60
        if new_hour>23:
            new_hour=new_hour-24
        return "%02d:%02d" % (new_hour, new_min)


    def __sub__(self,minutes):
        sub_time=self.total_minutes-minutes
        new_shour=sub_time/60
        new_smin=sub_time%60
        if new_shour<0:
            new_shour=new_shour+24
        return "%02d:%02d" % (new_shour, new_smin)


    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes

    def __ne__(self, other):
        return not self==other
