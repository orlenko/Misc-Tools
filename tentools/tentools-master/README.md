# 10 (not quite yet) Tools
Little tools that automate some daily tasks

## daylog.py: take notes while you work

Can't remember what tasks you spent your day on? open a console with `daylog.py` running, and simply type things as you
start working on them. The press Enter to see a beautiful log of things you did today.

Plus, helpful interactive commands to work with the log:
  - `:c` to clear the log
  - `:d [HH:MM]` to delete an entry for a specific time
  - `:r [HH:MM] <replacement text>` to replace an entry
  - `:i [HH:MM] <what I did earlier>` to back-fill an log entry you forgot to enter at the time.
  - `<Enter>` to print out the day log
  - `any other text` to add a log entry for the current time.

## dayskel.py: daily notes skeleton generator

Use this on a Mac to generate an outline of your day based on iCal, so that you can annotate your day as it goes.

Example use:
```
ICAL_EMAIL=you@company.com ./dayskel.py
```

## type_current_time.applescript: insert current time at cursor

This is AppleScript snippet that can be used in Automator on MacOS to insert curent time in the format [HH:MM].

## notes_strike_selected.applescript: format current selection as strikethrough
 
In Apple Notes on MacOS, format current selection as strikethrough
