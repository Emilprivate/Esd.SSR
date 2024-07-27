# Writeup for picoGym : Picker II

## Steps:
Instead of calling the win function and doing all the useless things that the win function does, we can just print out the contents of the flag.txt thereby not needing to convert from hex to ascii: `print(open('flag.txt','r').read())`

## Flag:
```picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}```
