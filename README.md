# Stardate

This package is meant to convert an existing date to a stardate similar to
*Star Trek : The Next Generation*.  It is feature complete in that regard. I
would like to add more options and different packages to this eventually. If
you want to work on something feel free to make a pull request and submit your
own changes.

## Usage

On the command line, run `stardate` to get the current date as a stardate, or
pass in the date in YYYY-MM-DD format to get the stardate for a given date:

```console
$ stardate -d 1999-12-24
53443.5
```

Use the `-v` flag to get verbose outout including calculations.

As a library, use the `get_stardate` function to return a given date as a
stardate:

```pycon
>>> from stardate_goddard import get_stardate
>>> get_stardate()
75108.2
>>> get_stardate('1999-12-24')
53443.5
```

## Roadmap

1.  Add additional timelines
2.  Create additional plugins for various other sources(gnome shell, kde,
    pelican, wordpress)

## License

This project I made is open source. Feel free to use it and make changes.

## Credit

If you use this project please include my information. Appreciate it.
