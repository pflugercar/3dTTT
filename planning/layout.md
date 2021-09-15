# Layouts for each of the menus

## Main Menu layout
```
Welcome to 3d Tic Tac Toe!

Please, make a selection.

1) Number of players = 3
2) Player names and pieces
    --Name--  --piece--
    Player1       X
    Player2       O
    Player3       Z
3) No changes

Which do you want to change? :
```

## Change player info menu layout
```
1) Change player names
2) Change player pieces
3) Back to main menu

Selection: 
```

## Layout of the board in Terminal
For reference:   <a href="https://theasciicode.com.ar/">The ASCII Code</a>
```
ASCII CODE 176 : ░
ASCII CODE 219 : █
ASCII CODE 197 : ┼
ASCII CODE 196 : ─
ASCII CODE 179 : │
```
```
          Top                  Middle               Bottom

    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░ 
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │ ███ │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
```

## Player input options
### Move cursor with arrows?  This is can be added later.
## 3 step choice.
##   select layer - 1 "Top", 2 "Middle", 3 "Bottom"
```
     (1) Top                (2) Middle           (3) Bottom

    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │ ███ │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
```
##   select row - 1 top, 2, middle, 3 bottom
```
            Top                  Middle               Bottom

(1)    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
     ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
(2)    ░  │  ░  │  ░         ░  │ ███ │  ░         ░  │  ░  │  ░
     ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
(3)    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
```
**OR**
```
            Top                  Middle               Bottom

    ░  │  ░  │  ░      (1)   ░  │  ░  │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────        ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░      (2)   ░  │ ███ │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────        ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░      (3)   ░  │  ░  │  ░         ░  │  ░  │  ░
```
**OR**
```
            Top                  Middle               Bottom

    ░  │  ░  │  ░         ░  │  ░  │  ░      (1)   ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────        ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │ ███ │  ░      (2)   ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────        ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │  ░  │  ░      (3)   ░  │  ░  │  ░
```

##  select colum - 1 first, 2 middle, 3 last
```
         Top                  Middle               Bottom
   (1)   (2)   (3)
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │ ███ │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
```
**OR**
```
         Top                  Middle               Bottom
                         (1)   (2)   (3)
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │ ███ │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
```
**OR**
```
         Top                  Middle               Bottom
                                               (1)   (2)   (3)
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │ ███ │  ░         ░  │  ░  │  ░
  ─────┼─────┼─────     ─────┼─────┼─────     ─────┼─────┼─────
    ░  │  ░  │  ░         ░  │  ░  │  ░         ░  │  ░  │  ░
```

##   Player may type u (or U) to go back one level of selection
###   Because of the core being removed, 2, 2, 2 is not an option.
