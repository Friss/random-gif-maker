Random Movie GIF Maker
=====

### Using Random Movie GIF Maker
To use just the random GIF maker run:

```
$ python randomGif.py
```

Then enter the path to your movies / video files.

### Using Random Movie GIF Maker Twitter Bot
To use the Twitter Box first:

```
$ cp config.cfg-dist config.cfg
```

Then fill in your API and OAUTH Keys into the config file from Twitter and Imgur.

Then run:

```
$ python twitterBot.py
```

The bot will now tweet every hour.

### Notes

My movie file structure is:

```
/root/Movie Name/Movie (1080p) [2013].mkv
```

If script is outputting the wrong Movie Title or errors on generating ```moviename``` I would look into how the movie name is generated. 

### Resources
The twitter bot is from [https://github.com/LindseyB/starwars-dot-gif/](Lindsey B's Starwars dot Gif) I plan to make more modifications later to make it my own. 

The script uses [https://github.com/Zulko/moviepy](MoviePy) to generate the GIFs so there are endless possbilities of GIFs that could be created.  