# The Farmer Was Replaced

Repo for scripts for [the game](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/) on Steam.

## Built Ins

I've added refs, typing, and docs for many built-in variables and functions. More to come. To reference, these, use `from game.builtins import *`

## Importing

Unfortunately, I haven't found a way to trick the IDE into gathering definitions for all file globally in the project, so you still need to add imports at the top even though they can't be used in the game.

Even more unfortunately, I tried using a single file to import/export everything then have that be the sole import statement, but this causes circular importing issues and breaks the intellisense as well. 

If anyone finds a solution, please open a PR!
