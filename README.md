# TBAGE
**Text Based Adventure Game Engine**

## Project Summary
TBAGE is a game engine to create Text Based Adventures. It is open source and free for people to use. The core concept is people with little to no programming experience would be able to write game "scripts" that the engine would then parse into a playable Text Based Adventure game. The classes and functions in the engine could also be pulled into a seperate project and used as a base to create a more indepth adventure in python.

### Concept of Operation
A game creator would create a game with a minimum of two(2) files:
* Game Map
* Game Script
The game map would outline the layout of the game tiles, the Game script would be where "Scenes" were written for each tile. The engine would then parse these into a playable game that a player would navigate around using the command line with simple commands like "Go North", or "Pick up [Item]"

### Tentative Roadmap for initial release
1. Create a basic [Map Creation structure](https://github.com/silverback338/tbage/wiki/Map-Creation) *In-Process*
2. Create a [Text-Parser](https://github.com/silverback338/tbage/wiki/Text-Parser) Module to take care of in game player commands
2. Create a basic Player Character Structure
3. Create a basic [Inventory Management System](https://github.com/silverback338/tbage/wiki/Inventory)
4. Create an NPC Character Structure
5. Create a Simple Combat mechinism
6. Create a basic [scripting language](https://github.com/silverback338/tbage/wiki/Scripting-Language) for game "scripts"

### After the Initial Release
- Create a Multi-player protocol to allow 2 or more people to play the same story at the same time
- Generate an economy system
- Create a web interface to allow people to play games in a web browser
- Globalization features to allow scripts to be automatically translated

## Installation
Requires Python 3 <br>
Clone the repo and run
```
pip install -r requirements.txt
```

## Contributors
* Kyle Ranous
