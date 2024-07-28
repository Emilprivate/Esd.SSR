# Writeup for picoGym Exclusive : GDB baby step 4
## Steps:
Opening the binary in gdb and checking the available functions, we can see `func1`, `info functions`. Let's set a breakpoint on this one, `b *func1`, `r`. Without having to layout the entire memory map of this function we can see the value 0x3269 being multiplied into the eax register as per the information in the challenge. So that's the flag.

## Flag:
```picoCTF{12905}```
