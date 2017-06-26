# screeps-clock

This app pulls the `Game.time` value from the Screeps server and converts it to
a date time by pretending it's a unix timestamp.

The app provides an ajax based front end that keeps updating as well as a
`/time.js` endpoint that contains both the current tick and the current time.

A "time factor" can be added in to "speed up" the clock. This is essentially
just a multiplier added to `Game.time`.


# Requirements
- Postgres
- Python 3.x


# Setup

Update the info in settings.example

```bash
cp settings.distro settings
nano settings # add api settings.
make
source bin/envvar
flask run
```


# Javascript Library

The library `js/screepstime.js` provides a simple set of functions to generate
the dates from inside screeps directly.
