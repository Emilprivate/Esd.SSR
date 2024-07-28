# Writeup for picoGym Exclusive : GDB  baby step 2
## Steps:
With this challenge we open the binary with GDB, check the functions `info functions`, break at the main function `b *main`, since there's a loop and it's not immedietely clear what value is in the eax register, we can just set a break at the pop instruction of the base pointer and then check the value of the eax register, `b *0x401141`, `c`. Here we just type `info registers eax` and we get `eax   0x4af4b   307019`.

## Flag:
```picoCTF{307019}```
