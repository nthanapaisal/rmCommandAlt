# rmCommandAlt

Purpose:
- create an alternative to the rm command. This program, rm.py, will take an arbitrary number of paths as arguments and, for each argument, move them to ∼/rm_trash . If ∼/rm_trash does not already exist, it will be created.


File:
  - rm.py
  
Command Lines: 
  - python3 rm.py ./file . . . . -r 
  - notes: -r is for recurse through the directory.
  - Ex: python3 rm.py ./file ./test ./foldee ./haha -r
  
