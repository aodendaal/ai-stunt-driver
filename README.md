# Stunts AI driver
A Convolutional Neural Network (CNN) written in Python using Tensorflow that attempts to plays [1990's Stunts](https://en.wikipedia.org/wiki/Stunts_(video_game)).

![Stunts Main Menu](img/screenshot00.png)

I chose Stunts as my game environment because I can create custom tracks. The screen resolution is also small and simple which I think will help data analysis.

The game is available via [abandonware](http://www.abandonia.com/en/games/73/Stunts.html) and runs in [DOSBox](https://www.dosbox.com/).
## Status
I'm currently on getting 12%-15% accuracy so the car either does nothing (decides there's no input required) or only accelerates. This project is still a work-in-progress.

I made a custom, banked track that's a simple left-hand then right-hand loop.
![Stunts Main Menu](img/screenshot01.png)

## Recording training data
**NB** Recorder takes screenshots of the whole screen so you must play the game in fullscreen mode.
```Python
python recorder.py
```

## Training the model
```Python
python trainer.py
```

## Running the model
**NB** Runner takes screenshots of the whole screen so you must run the game in fullscreen mode.
```Python
python runner.py
```