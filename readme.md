# Example for finding the absolute position of a the Cursor with KWin

This repository gives a simple example on how one can read the absolute cursor position with kwin and Qt6.
This is needed if you want to get the absolute global cursor position on a kde plasma wayland desktop environment.

## Requirements:
For this example mostly used PyQt6 and the internal KWin and Qt6 capabilities.
-> you just need to install PyQt6

## How to:

The main file is `ListenerExample.py` which hopefully contains all needed explenations.

You should be able to modify this example to only get one coordinate without needing the complete listener
by modifying the KWinPosScript to just send the current cursor position instead of initialising the callback.
With that you would still need to create the service and listen to it, but you can just wait on any output from the listener and continue.