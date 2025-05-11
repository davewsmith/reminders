# Reminders of upcoming events

A cleaned-up version of an old thing I had running on Google App Engine.
This scratches a personal itch. If it works for you, great. Have at.

Take a set of files named `*.dates` that contains lines of the form

    YYYY-MM-DD Event Name

and emits a page of HTML. Dates prior to "today" (the day the script is run) are ignored.
The first event with a given name is kept; subsequent occurences with that name are ignored.

## Usage

One-time setup

    python3 -m venv venv
    venv/bin/pip install -r requirements.txt

then

    venv/bin/python reminders.py > /var/www/html/.../index.html

Running the latter daily from `cron` keeps the days straight.

## License

MIT, incorporated by reference.
