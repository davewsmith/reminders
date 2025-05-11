# Reminders of upcoming events

A cleaned-up version of an old thing I had running on Google App Engine.
This scratches a personal itch. If it works for you, great. Have at.

Takes a set of files named `*.dates` that contain lines of the form

    YYYY-MM-DD Event name

and emits a page of HTML with events listed soonest-first showing the number of days remaining before the event.
Dates prior to the day the script is run are ignored -- no looking back.
The first event with a given name is kept; subsequent occurences with that name are ignored.

## Usage

One-time setup

    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

then

    venv/bin/python reminders.py > /var/www/html/.../index.html

Running the latter daily from `cron` (after a `git pull`) keeps the days straight.

## Maintenance

The `*.dates` files need periodic attention, because time passes.

## License

MIT, incorporated by reference.
