# Stardate

This package is meant to convert an existing date to a stardate similar to
*Star Trek : The Next Generation*.  It is feature complete in that regard. I
would like to add more options and different packages to this eventually. If
you want to work on something feel free to make a pull request and submit your
own changes.

## Usage

On the command line, run `stardate -d YYYY-MM-DD` to get the stardate for a
given date:

```console
$ stardate -d 2378-04-06
53443.5
```

Use the `-v` flag to get verbose outout including calculations.

As a library, use the `get_stardate` function to return a given date as a
stardate:

```pycon
>>> from stardate_goddard import get_stardate
>>> get_stardate('2378-04-06')
54867.5
```

## Roadmap

1.  Add additional timelines
2.  Create additional plugins for various other sources(gnome shell, kde,
    pelican, wordpress)

## License

MIT: see [LICENSE](LICENSE)

## Credits

If you use this project please include my information. Appreciate it.
