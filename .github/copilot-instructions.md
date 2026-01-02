# Copilot Instructions for Alien Invasion Game

## Project Overview
This is a Pygame-based arcade game project from Python Crash Course. The game is in early development with the core game loop established. The architecture is centered on a single `AlienInvasion` class that manages all game resources and behavior.

## Architecture & Current State

### Core Structure
- **Main Class**: `AlienInvasion` - Manages game initialization, screen setup, and the main event loop
- **Framework**: Pygame - Used for graphics, event handling, and display management
- **Screen Dimensions**: 1200x800 pixels (hardcoded)
- **Game Loop Pattern**: Infinite loop handling pygame events (currently only QUIT), with `pygame.display.flip()` to refresh the screen

### Expected Development Pattern
Based on Python Crash Course progression, anticipate expanding into:
- **Game Objects**: Separate classes for Ship, Alien, Bullet (not yet created)
- **Game Settings**: Configuration class for screen size, speeds, colors (future)
- **Event Handling**: Keyboard input for ship movement, shooting mechanics
- **Collision Detection**: For bullets hitting aliens
- **Game States**: Managing play, game-over, reset logic

## Key Developer Workflows

### Running the Game
```bash
python alien_invasion.py
```
Launches the game window. Close the window to exit.

### Known Issues (Address First)
- **Line 11**: Typo in `pygame.display` - currently reads `pygame.dispay` (missing 'l')
  - Fix: Change `pygame.dispay.set_caption()` to `pygame.display.set_caption()`

## Project Conventions & Patterns

### Naming & Style
- **Classes**: PascalCase (`AlienInvasion`)
- **Methods**: snake_case with descriptive docstrings in triple-quotes
- **Comments**: Use `#` for implementation notes within methods

### Current Design Pattern
- **Centralized Management**: Single class handles all game logic (may need refactoring as complexity grows)
- **Initialization**: `__init__()` sets up pygame and screen; `run_game()` contains event loop
- **Docstring Format**: One-line summary for public methods (e.g., `'''Start the main loop for the game'''`)

## Integration Points & Dependencies

### External Dependencies
- **pygame**: Graphics library - handles display, events, rendering
- **sys**: Standard library - used for `sys.exit()` on window close

### Dependency Installation
Requires pygame. Install with:
```bash
pip install pygame
```

## Guidance for AI Agents

When extending this codebase:

1. **Fix the immediate bug** (`pygame.dispay` typo) before adding features
2. **Follow the emerging pattern**: New game objects should be separate classes (Ship, Alien, Bullet) managed by `AlienInvasion`
3. **Keep game loop simple**: Event handling stays in `run_game()` but delegate rendering/updates to methods
4. **Use hardcoded values** as they are currently - don't introduce Settings class until prompted
5. **Maintain docstring consistency**: One-line descriptive docstrings in triple-quotes for all methods
6. **Test by running**: The game window is the primary test interface at this stage

## File References
- [alien_invasion.py](alien_invasion.py) - Main game class and entry point
