# Battleships Game

![Battleships logo](/images/Battleships.png)

## Purpose
This console-based Battleships game allows players to take turns guessing coordinates to sink enemy ships. The game is designed for single-player mode, where the user competes against the computer. It is a fun and strategic game that tests your prediction and planning skills.

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
* [Target Audience](#target-audience)
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [References and Inspirations](#references-and-inspirations)

## User Experience (UX)

The Battleships game is designed to provide an intuitive and enjoyable experience:

#### Intuitive Gameplay:
- Easy-to-understand rules and controls.
- Simple input method for guessing coordinates.
- Clear feedback on hits and misses.

#### Visual Feedback:
- Colored text for different game states (e.g., hits, misses, ships).
- Real-time updates on remaining ships.

#### Structured Layout:
- Grids are displayed with headers and borders for clarity.
- Scores and game status are prominently shown.

#### Consistent Styling:
- Uniform style for all game elements.
- Consistent color scheme for different game states.

#### Accessibility:
- High contrast colors for better visibility.
- Clear instructions and prompts.

These UX considerations ensure a smooth, accessible, and engaging experience for all users.

## Target Audience

The target audience for this game includes:

- **Casual Gamers**: Individuals looking for a simple yet engaging game to pass the time.
- **Strategy Enthusiasts**: Players who enjoy games that require planning and foresight.
- **All Ages**: Suitable for both young and old gamers who appreciate classic games.
- **Retro Game Fans**: Individuals who enjoy traditional games with a modern twist.

This game aims to provide an engaging and thought-provoking experience reminiscent of classic board games.

## Features
- Initialize a game grid of customizable size (5-10).
- Player vs. Computer mode.
- Random ship placement for both player and computer.
- Turn-based guessing of coordinates.
- Real-time feedback on hits, misses, and remaining ships.
- Option to quit the game at any time.

## Design

#### Layout:
- Grid Display: Rows and columns labeled for easy reference.
- Visual Indicators: Clear symbols and colors for hits, misses, and ships.

#### Styling:
- Consistent Color Scheme: Different colors for hits, misses, and ships.
- Structured Grid: Clearly defined borders and headers for grids.

#### Accessibility:
- High Contrast Colors: Ensures visibility for all users.
- Simple Text Prompts: Clear instructions and feedback for user actions.

#### Interactivity:
- Command-line Inputs: Simple and straightforward input method for coordinates.
- Real-time Feedback: Immediate visual response for user actions.

## Technologies Used

### Languages Used
- Python

### Libraries Used
- [Colorama](https://pypi.org/project/colorama/): Used for colored text output in the console.

## Testing

### Code Testing
- **Manual Testing**: Extensive manual testing was performed to ensure all game features function as intended.
  - Validated that the grid initializes correctly.
  - Ensured random ship placement does not overlap.
  - Verified that hits, misses, and ship counts update correctly.
  - Tested user input validation for coordinate guessing.
  - Checked game over conditions and restart functionality.

### Bugs

#### Fixed Bugs
- **Ship Lengths**: Initially, ships of lengths 3, 2, and 1 were used, causing incorrect ship count reflections. This was fixed by using ships of length 1 only.

![Ship Length Bug](/images/ships%20count%20bug.png)

#### Unfixed Bugs
- **Code Linter Warnings**: The Python code contains lines that exceed the 79-character limit as specified by PEP 8. Despite refactoring efforts, some lines still exceed this limit. The game functions correctly, but these warnings are acknowledged in the code linter results.

![Code Linter Warnings](/images/Code%20Linter%20Warnings.png)

## Deployment

### Steps to Deploy to Heroku
1. Ensure you have Python and Git installed on your machine.
2. Create a `requirements.txt` file with the necessary dependencies:
   ```bash
   pip freeze > requirements.txt

## References and Inspirations

Here are some sources that influenced the development of this game and provided useful insights:

- **Battleship Game Rules**: [Wikipedia - Battleship (game)](https://en.wikipedia.org/wiki/Battleship_(game))
  - Provides an overview of the classic Battleships game rules and strategies.

- **Colorama Documentation**: [Colorama - PyPI](https://pypi.org/project/colorama/)
  - Documentation for the Colorama library used for colored text output.

- **PEP 8 Style Guide**: [PEP 8 - Style Guide for Python Code](https://pep8.org/)
  - Provides the style guidelines for Python code, including line length recommendations.
