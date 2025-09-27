🖼️ 5-Day Pygame: Window Builder
Practice creating your own game window and making it respond to your key presses!
---
### Day 1: Basic Window Setup
1.  Create a file named `game_window.py`.
2.  Start your Pygame project by importing Pygame and initializing it.
3.  Create a game window that is `800` pixels wide and `600` pixels tall.
4.  Set the window's title to "My First Window".
5.  Include the basic game loop that keeps the window open until you click the 'X' button to close it.
6.  Remember to update the display at the end of the loop.
```
# Expected Output (when running the code):
# A black window titled "My First Window" appears.
# Clicking the 'X' button on the window closes it.
```
---
### Day 2: Quit with 'Q'
1.  Continue using your `game_window.py` from Day 1.
2.  Inside your game loop, check which keys are currently being pressed.
3.  Add code so that if the 'Q' key is held down, the game window closes.
```
# Expected Output:
# A black window titled "My First Window" appears.
# You can close the window by clicking 'X' OR by holding down the 'Q' key.
```
---
### Day 3: Colorful Background
1.  Continue using your `game_window.py` from Day 2.
2.  Inside your game loop, before checking for keys, fill the screen with a light gray color `(180, 180, 180)` by default.
3.  Now, add code so that when the Spacebar is held down, the screen instantly changes to a bright red color `(255, 0, 0)`.
4.  *(After core implementation)* Change the bright red color to *any other color you like*! (Hint: find RGB values online, like for blue `(0, 0, 255)` or green `(0, 255, 0)`).
```
# Expected Output:
# A gray window appears.
# If you hold Spacebar, the window turns red (or your chosen color).
# Releasing Spacebar makes it gray again.
# 'Q' or 'X' still closes the window.
```
---
### Day 4: Always Showing Color
1.  Continue using your `game_window.py` from Day 3.
2.  Modify your code so that the screen is *always* filled with either the default gray or your chosen color from Day 3, depending on whether the Spacebar is held down. (Hint: Think about filling the screen *every time* in the loop with the correct color.)
3.  Make sure the gray color is `(180, 180, 180)` and your chosen color from Day 3 is used when Spacebar is pressed.
```
# Expected Output:
# A gray window appears.
# If you hold Spacebar, the window turns your chosen color.
# Releasing Spacebar makes it immediately turn gray again.
# The window never appears black, only gray or your chosen color.
# 'Q' or 'X' still closes the window.
```
---
### Day 5: More Color Options
1.  Continue using your `game_window.py` from Day 4.
2.  Add a new feature: When you hold down the 'C' key, the background color should change to a *different* third color of your choice (e.g., blue `(0, 0, 255)`).
3.  Make sure that only one special color shows at a time (Spacebar color OR 'C' key color), and if neither is pressed, the default gray `(180, 180, 180)` shows.
```
# Expected Output:
# A gray window appears.
# Holding Spacebar turns it to your Day 3 color.
# Holding 'C' turns it to your Day 5 color.
# Releasing both makes it gray again.
# If you hold both Spacebar and 'C', decide which color takes priority!
# 'Q' or 'X' still closes the window.
```
