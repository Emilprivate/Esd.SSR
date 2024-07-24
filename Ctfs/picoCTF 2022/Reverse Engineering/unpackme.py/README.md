# Writeup for picoCTF 2022 : unpackme.py

## Tools:
- python

## Explanation
This problem was simply about understanding the contents of the python file, so when opening it in a text editor it becomes clear that there is some encryption being done on a payload and then executed once the python file is executed. This payload is descrypted just before it gets executed, so if the decrypted contents could be printed before executing, one could find the flag, which is exactly what I did.

Flag:
```
picoCTF{175_chr157m45_cd82f94c}
```
