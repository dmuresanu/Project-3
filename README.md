# Battleships 
## A Python Command Line Game

![Battleships logo](/images/logo.png)

This application is a Python-based battleships style game. The game takes the user's name to begin with and then proceeds into the game.

- **By:** Doru Muresanu

### [Live Site](https://battl3ships-7fc5338331a4.herokuapp.com/)
### [Repository](https://github.com/dmuresanu/Project-3)

---

## Index – Table of Contents
* [Pre-Project](#pre-project-planning)
* [User Experience (UX)](#user-experience-ux)
* [Target Audience](#target-audience)
* [Design](#design)
* [Features](#features)
* [Features Left to Implement](#features-left-to-implement)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [References and Inspirations](#references-and-inspirations)
* [Aknowledgements](#acknowledgements)

## Flow

### Pre-Project Planning

For this project, I decided to create a battleships-style Python game for the command line. The concept was inspired by classic battleship games, and I wanted to bring that experience into a Python-based console application.

To begin, I mapped out the game flow and logic using diagrams and flowcharts, which helped guide the development process. Understanding the sequence of actions and the interaction between different components was crucial for ensuring smooth gameplay.

#### Please see the below flow chart to better understand the initial design and concept

![Flow Chart](/images/Flow%20Chart.png)

### Pre-Planning Structure

#### Game Structure
- **Grid Structure**
  - Grid size options between 5x5 and 10x10.
  - Rows and columns labeled for easy reference.
  
- **Ship Placement**
  - Random placement of ships on the grid.
  - Both player and computer have their own grid with hidden ships.

- **Player Structure**
  - Player's name.
  - Player's guesses and their results (hit/miss).
  
- **Computer Structure**
  - Random guesses with logic to avoid duplicate guesses.
  - Feedback on player’s hits and misses.

#### Game Flow
When the user starts the game, they are prompted to enter their name. After that, the game rules are displayed, and the user needs to choose the grid size. Once the game starts, the user can make a guess and play the game or quit it by typing 'quit'.

**Game Start**
- The player and the computer each have their grids set up with ships placed randomly.
- The player and the computer take turns guessing coordinates on the opponent's grid to hit ships.
- Hits and misses are visually represented on the grid.
- The game ends when all ships of one side are sunk.

**End of Game**
- The winner is announced based on who sinks all of the opponent's ships first.
- The player is then prompted to either play again or exit.


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

## Features
- Initialize a game grid of customizable size (5-10).
- Player vs. Computer mode.
- Random ship placement for both player and computer.
- Turn-based guessing of coordinates.
- Real-time feedback on hits, misses, and remaining ships.
- Option to quit the game at any time.

## Features Left to Implement

- **Multiplayer Mode**: Allow two players to compete against each other instead of playing against the computer.
- **Difficulty Levels**: Introduce difficulty levels for the computer's guessing strategy.
- **Visual Enhancements**: Add more colors and effects using `Colorama` to enhance the user interface.
- **Sound Effects**: Integrate sound effects for hits, misses, and game events.

## Technologies Used

### Python
- Used to create the application

### Heroku
- Used to deploy and host the application

### Github
- Used to deploy and host the application

### Gitpod
- IDE used for creating the application

### Git
- Used for version control

### Libraries Used
- [Colorama](https://pypi.org/project/colorama/): Used for colored text output in the console.

## Testing

### Testing Phase
Manual testing was carried out to ensure the game functions as intended. Below are the key test cases and their results:

| Test | Result |
| ---- | ------ |
| Grid initializes correctly | Pass |
| Random ship placement does not overlap | Pass |
| Player input validation for coordinates | Pass |
| Game handles hit and miss correctly | Pass |
| Game ends correctly when all ships are sunk | Pass |
| Player is prompted to play again or exit | Pass |

### User Testing
Additional user tests were conducted to check for error handling, such as invalid grid input, invalid coordinate input, and to verify that the game responds appropriately.

![Invalid Grid Input](/images/Invalid%20grid%20input.png)
![Invalid Coordonate Input](/images/Invalid%20Coordonate%20Input.png)

### Bugs

#### Fixed Bugs
- **Ship Lengths**: Initially, ships of lengths 3, 2, and 1 were used, causing incorrect ship count reflections. This was fixed by using ships of length 1 only.

![Ship Length Bug](/images/ships%20count%20bug.png)

- **Code Linter Warnings**: The Python code contained lines that exceed the 79-character limit as specified by PEP 8. The  code has been refactored to adhere to PEP 8 guidelines, specifically ensuring that all lines are within the 79-character limit. This improves readability and maintains consistency with Python's best practices.

![Code Linter Warnings](/images/Code%20Linter%20Warnings.png)

![Code Linter no errors](/images/Code%20Linter%20no%20errors.png)

#### Unfixed Bugs
- **None**: All known issues have been resolved.

## Deployment

1. Navigate to heroku.com & log in.
2. Click "new" and create a new App.
3. Give the application a name and then choose your region and Click "Create app".
4. On the next page click on the Settings tab to adjust the settings.
5. Click on the 'config vars' button.
6. Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.
7. Buildpacks now need to be added.
8. These install future dependancies that we need outside of the requirements file.
9. Select Python first and then node.js and click save.
10. **Make sure they are in this order.**
11. Then go to the deploy section and choose your deployment method.
12. To connect with github select github and confirm.
13. Search for your repository select it and click connect.
14. You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes.
15. For this option choose the branch to deploy and click enable automatic deploys.
16. This can be changed at a later date to manual.
17. Manual deployment deploys the current state of a branch.
18. Click deploy branch.
19. We can now click on the open App button above to view our application.

## References and Inspirations

Here are some sources that influenced the development of this game and provided useful insights:

- **Battleship Game Rules**: [Wikipedia - Battleship (game)](https://en.wikipedia.org/wiki/Battleship_(game))
  - Provides an overview of the classic Battleships game rules and strategies.

- **Colorama Documentation**: [Colorama - PyPI](https://pypi.org/project/colorama/)
  - Documentation for the Colorama library used for colored text output.

- **ASCII Art**: [ASCIIART.EU](https://www.asciiart.eu/vehicles/navy#google_vignette)
  - Used to create the ascii art used for this project  

- **PEP 8 Style Guide**: [PEP 8 - Style Guide for Python Code](https://pep8.org/)
  - Provides the style guidelines for Python code, including line length recommendations.

- **Youtube**: [YouTube](https://www.youtube.com/)
  - One of the best free learning platforms in the world and has I use it every day when coding to help me better understand concepts from different perspectives.  

## Aknowledgements

### Alan Bushell

My mentor in CI, who provided invaluable feedback and guidance throughout this project.