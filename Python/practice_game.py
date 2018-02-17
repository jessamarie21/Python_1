Python 3.3.2 (v3.3.2:d047928ae3f6, May 13 2013, 13:52:24) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Please enter a grid size: 4
0 0|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0

Player A please enter move: 0, 1, 2
0 2|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0
Player B please enter move: s
Please enter a file name: sudoku
>>> ================================ RESTART ================================
>>> 
Please enter a grid size: 4
0 0|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0

Player A please enter move: 0, 1, 2
0 2|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0
Player B please enter move: s
Please enter a file name: sudoku
>>> ================================ RESTART ================================
>>> 
Please enter a grid size: 4
0 0|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0

Player A please enter move: 0, 1, 2
0 2|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0
Player B please enter move: 1, 2, 3
0 2|0 0
0 0|3 0
-------
0 0|0 0
0 0|0 0
Player A please enter move: 0, 0, 4
4 2|0 0
0 0|3 0
-------
0 0|0 0
0 0|0 0
Player B please enter move: 0,2,1
Traceback (most recent call last):
  File "/Users/jessamariezabala/Documents/game.py", line 191, in <module>
    play()
  File "/Users/jessamariezabala/Documents/game.py", line 32, in play
    move[k] = int(move[k])
ValueError: invalid literal for int() with base 10: '0,2,1'
>>> ================================ RESTART ================================
>>> 
Please enter a grid size: 4
0 0|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0

Player A please enter move: 0, 1, 2
<class 'str'>
0, 1, 2
0 2|0 0
0 0|0 0
-------
0 0|0 0
0 0|0 0
Player B please enter move: q
<class 'str'>
q
>>> tup()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    tup()
NameError: name 'tup' is not defined
>>> 
