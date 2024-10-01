# Smiley Face Game

## Overview

The Smiley Face Game is an interactive Python program that allows users to click on a smiley face displayed on the screen. When clicked, the face changes its position and color. The game utilizes basic graphical elements and demonstrates user interaction through mouse events.

## Features

- **Interactive Gameplay**: Users can click on the smiley face to move it around the window and change its color.
- **Random Color Selection**: Each time the user clicks outside the smiley face, it changes to a new random color from a predefined list.
- **Graphical Interface**: The game is built using the `graphics.py` library, providing a visually engaging experience.

## Requirements

- Python 3.x
- `graphics.py` library (available [here](http://mcsp.wartburg.edu/zelle/python/graphics.py))
- `random` and `math` standard Python libraries

## How to Play

1. Clone or download this repository.
2. Install the required `graphics.py` library if you haven't already.
3. Run the script using Python:

    ```sh
    python smiley_face_game.py
    ```

4. Click anywhere in the window to move the smiley face. If you click outside the face, it will change to a new color.
5. Enjoy interacting with the smiley face!

## Functions

### `newcolor(colorlist)`
Chooses and returns a random color from the provided list.

- **Inputs**: `colorlist` - The list of colors the face can be.
- **Outputs**: `color` - The randomly selected color.

### `distance(p, x, y)`
Calculates the distance between the mouse click point and the center of the smiley face.

- **Inputs**: `p` - The point where the user clicked, `x`, `y` - The coordinates of the smiley face center.
- **Outputs**: `distance` - The distance between the center of the face and the clicked point.

### `main()`
Controls the main flow of the game, handling window creation, event listening, and smiley face rendering.

## Game Flow

1. **Initialization**: A window is created, and the smiley face is drawn in the center.
2. **User Interaction**: The program waits for mouse clicks:
   - If the click is within the face, the face changes color.
   - If the click is outside the face, the face moves to the new location and changes to a new random color.
3. **Exit**: The program will close the window when the user clicks again.

## Future Improvements

- **Enhanced Graphics**: Improve the design of the smiley face and background.
- **Score Tracking**: Add a scoring system for clicks on the face within a certain time frame.
- **More Interactive Elements**: Introduce additional shapes or animations for a more engaging experience.

## License

This project is open-source and available.

---

**Author**: Alexander Harshman
