# Stunts AI driver
A Convolutional Neural Network (CNN) written in Python using Tensorflow that attempts to plays [1990's Stunts](https://en.wikipedia.org/wiki/Stunts_(video_game)).

![Stunts Main Menu](img/screenshot00.png)

I chose Stunts as my game environment because I can create custom tracks. The screen resolution is also small and simple which I think will help data analysis.

The game is available via [abandonware](http://www.abandonia.com/en/games/73/Stunts.html) and runs in [DOSBox](https://www.dosbox.com/).
## Status
My model is sitting at ~64% accuracy and it's capable of completing the custom track I've been training on.

I made a custom, banked track that's a simple left-hand then right-hand loop.
![Stunts Main Menu](img/screenshot01.png)

## Recording training data
**NB** Run the game in your primary screen because Pillow (image taking dependency) only applies coordinates in the primary space.
```Python
python recorder.py
```
Run the script then start the game, select a track and begin the race. Press F5 to start recording the screen and your inputs and F5 again to stop recording. Press F12 to stop the script running.

In a future update I want to cache the recording session so that if you crash you can discard the data without saving it to file.

## Training the model
```Python
python trainer.py
```

## Running the model
**NB** Runner takes screenshots of the whole screen so you must run the game in fullscreen mode.
```Python
python runner.py
```
Run the script then start the game, select a track and begin the race. Press F5 to allow the script to send keyboard commands and press F5 again to stop. Press F12 to stop the script running.