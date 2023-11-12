#!/usr/bin/env python
from datetime import datetime


entries = []


def day_summary(now=None):
    now = now or datetime.now()
    parts = ['Day Notes for %s' % now.strftime('%A %b %d %Y'), '']
    for start, text in entries:
        parts.append('[%02d:%02d]\t%s' % (start.hour, start.minute, text))
    return '\n'.join(parts)



def add_entry(entry):
    entries.append((datetime.now(), entry))


class SpecialCommands:

    @staticmethod
    def parse_hh_mm(command):
        parts = command.split(' ')
        hour, minute = [int(part) for part in parts[1].strip('[]').split(':')]
        return hour, minute

    @classmethod
    def clear(cls, command):
        print(f' ✨ Clearing all entries on {command} ✨')
        global entries
        entries = []

    @classmethod
    def delete(cls, command):
        hour, minute = cls.parse_hh_mm(command)
        global entries
        entries = [e for e in entries if not (e[0].hour == hour and e[0].minute == minute)]

    @classmethod
    def replace(cls, command):
        hour, minute = cls.parse_hh_mm(command)
        new_line = command[len(':r [XX:XX]'):]
        global entries
        new_entries = []
        for ts, line in entries:
            if ts.hour == hour and ts.minute == minute:
                line = new_line
            new_entries.append((ts, line))
        entries = new_entries

    @classmethod
    def insert(cls, command):
        hour, minute = cls.parse_hh_mm(command)
        new_line = command[len(':i [XX:XX]'):]
        now = datetime.now()
        insertions = [(datetime(now.year, now.month, now.day, hour, minute), new_line)]
        global entries
        new_entries = []
        for ts, line in entries:
            time_to_insert = ts.hour > hour or ts.hour == hour and ts.minute >= minute
            if time_to_insert and insertions:
                new_entries.extend(insertions)
                insertions = []
            new_entries.append((ts, line))
        if insertions:  # What if we did not find a suitable place? Then it's at the end!
            new_entries.extend(insertions)
        entries = new_entries

    @classmethod
    def help(cls, command):
        print('''Usage:
        <any input> <Enter> — add a log entry with current timestamp
        <Enter> without any input — print out today's log
        == Commands: ==
        :c  - clear all entries
        :d [hh:mm] — delete entry at the specified timestamp
        :r [hh:mm] <any input> — replace the entry at the specified timestamp
        :i [hh:mm] <any input> — insert or backfill an entry 
        \n''')

    @classmethod
    def get_interpreter(cls, command):
        return {
            ':h': cls.help,
            ':?': cls.help,
            ':c': cls.clear,
            ':d': cls.delete,
            ':r': cls.replace,
            ':i': cls.insert,
        }.get(command[:2])


def interpret_command(command):
    # print(f'\t✨\tinterpreting command {command}\n')
    specific_interpreter = SpecialCommands.get_interpreter(command)
    if specific_interpreter:
        specific_interpreter(command)
    elif command:
        add_entry(command)
    else:
        print(day_summary())


def main_loop():
    while True:
        command = input(' 🕒 ')
        interpret_command(command)


if __name__ == '__main__':
    main_loop()
