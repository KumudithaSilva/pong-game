# 🏓 Pong Game – A Python Turtle-Based Arcade Game

Pong Game is a Python-based arcade game that simulates the classic Pong gameplay using the `turtle` graphics module. The project is structured with a strong emphasis on Object-Oriented Programming (OOP), applying principles such as **encapsulation**, **modularization**, and **class responsibility separation**.

A major educational aspect of this project is the use of **encapsulation**, where each game component (e.g., paddles, ball, scoreboard, net) is implemented as an independent class with its own state and behavior. These components interact with each other only through well-defined public methods, ensuring clean and predictable behavior. For example, the `Ball` class encapsulates all movement and collision logic, while the `Scoreboard` manages scoring and text display independently of game physics.

Additionally, **inheritance** is demonstrated by extending the `Turtle` base class to create custom visual objects like paddles, the ball, and the net. This leverages built-in turtle behavior (such as movement and drawing) while allowing us to override or enhance functionality for game-specific purposes. For instance, the `Paddle` class inherits from `Turtle` and adds vertical movement control via keyboard input.


---

## 🎮 Gameplay Overview

- **Two Player Mode:**
  - **Player A** (Right Paddle): `↑` / `↓` arrow keys
  - **Player B** (Left Paddle): `W` / `S` keys
- The ball continuously bounces around the arena.
- Players defend their side using paddles to prevent the ball from passing.
- A point is awarded to the opponent if a paddle misses.
- **First player to score 5 points wins**.

---


## 🎨 Gameplay  Output

Below are sample outputs of Pong Game:

<img width="400" alt="pong_game" src="https://github.com/user-attachments/assets/d196335e-3451-40a4-bf49-66fe92759293" />

---

## 🧠 Features

- 🧱 **Modular Object-Oriented Design**
- 📦 No external libraries required (pure Python)
- 🎯 Clean bounce physics and score tracking
- 🧵 Center net drawn using `BoundaryNet`
- 🎉 Game Over display with winner or draw message

---

## 🧱 System Architecture and Class Design

The game has been modularized into well-defined Python classes, each responsible for a specific element of the game. This makes the codebase clean, readable, and scalable.

### 🔹 `Ball` Class
- Controls movement, wall bouncing, paddle collision, and resetting upon a score.
- Methods:
  - `move()`: Advances the ball in the current direction.
  - `bounce_x()`, `bounce_y()`: Reverses direction upon collisions.
  - `reset_position()`: Centers the ball and changes direction when a player scores.

### 🔹 `Paddle` Class
- Represents each player's paddle and supports vertical movement.
- Methods:
  - `move_up()`
  - `move_down()`

### 🔹 `Scoreboard` Class
- Tracks and displays each player’s score.
- Displays a “Player X Wins!” or “Draw!” message upon game over.
- Methods:
  - `update_scoreboard()`
  - `l_point()`, `r_point()`
  - `game_over(winner)`

### 🔹 `BoundaryNet` Class
- Draws the dashed center net line on the playfield.
- Method:
  - `draw_net()`

### 🔹 `GameManager` Class
- Coordinates the interactions between ball, paddles, net, and scoreboard.
- Handles game-over logic including hiding game elements and announcing results.
- Methods:
  - `game_over(winner)`
  - `hide_game_objects()` *(optional utility)*

---

## 🖼️ Game Interface

- Screen Size: `800 x 600`
- Paddles are initialized on the left and right edges.
- Net is drawn at the center using a dashed line.
- Ball starts in the center and moves at a fixed speed.
- Scoreboard is displayed at the top of the screen.

---

## 🕹️ Controls

| Player | Move Up Key | Move Down Key |
|--------|-------------|---------------|
| A      | `↑`         | `↓`           |
| B      | `W`         | `S`           |

---

## ⚙️ Game Flow Logic

1. **Startup:**
   - The screen and all game elements (paddles, ball, net, scoreboard) are initialized.

2. **Main Loop:**
   - While `game_is_on` is `True`, the ball continuously moves and checks for:
     - Paddle collisions
     - Wall collisions
     - Scoring conditions

3. **Scoring:**
   - When the ball crosses the left or right boundary, a point is awarded to the opposite player and the ball resets.

4. **Game Over:**
   - When either player reaches the winning score (`5`), the game stops.
   - `GameManager` hides game objects and `Scoreboard` displays the result.

---

## 💻 File Structure

```text
pong-game/
├── main.py             # Main game loop and input handling
├── ball.py             # Ball logic
├── paddle.py           # Paddle control logic
├── scoreboard.py       # Score display and game over text
├── boundary_net.py     # Center net drawing logic
├── game_manager.py     # Game coordination and state management
└── README.md           # Project documentation
