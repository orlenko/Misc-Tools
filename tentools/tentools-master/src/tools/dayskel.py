#!/usr/bin/env python
import os
from appscript import its, app
from datetime import datetime, timedelta

EMAIL = os.environ['ICAL_EMAIL']


def get_events(email):
    cals = []
    skipped = set()
    for c in app('iCal').calendars():
        if c.name() in email:
            cals.append(c)
        else:
            skipped.add(c.name())
    if not cals:
        return
    now = datetime.now()
    start = datetime(now.year, now.month, now.day)
    end = start + timedelta(1)
    events = []
    for cal in cals:
        events.extend(cal.events[(its.start_date >= start).AND(its.start_date < end)]())
    return sorted(events, key=lambda evt: evt.start_date())


def mktemplate(events):
    now = datetime.now()
    parts = ['Day Notes for %s' % now.strftime('%A %b %d %Y')]
    for evt in events:
        start = evt.start_date()
        end = evt.end_date()
        parts.append('[%02d:%02d—%02d:%02d]\t%s' % (start.hour, start.minute, end.hour, end.minute, evt.summary()))
    return '\n'.join(parts)


if __name__ == '__main__':
    print(mktemplate(get_events(EMAIL)))
