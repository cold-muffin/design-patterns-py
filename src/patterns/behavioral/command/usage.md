# Command
The command pattern removes repitition in a codebase by turning repeatable implementation code into an object.

## Problem
```
SaveButton00 -> Save imp. -> Hardrive
SaveButton01 -> Save imp. -> Hardrive
SaveAndClose -> Save imp. -> Hardrive
```
Each button fundamentally does the same thing but they have their own independent (repeated) implementation which all reference the same reciever (the hardrive).

## Solution
```
SaveButton00 \
SaveButton01  +-> SaveCommand -> Hardrive
SaveAndClose /
```
Now each button uses one save object which contains the data the hardrive can implement. The reciever handles the implementation so that other recievers (eg. cloud storage) can handle the data differently, increasing scalability.