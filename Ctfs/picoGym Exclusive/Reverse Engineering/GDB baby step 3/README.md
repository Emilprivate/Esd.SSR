# Writeup for picoGym Exclusive : GDB baby step 3
## Steps:
Following the instrunctions of the challenge reveals the flag very easily. We just open the binary in gdb, then we set a breakpoint on main `b *main`, `r` and after running it we can see in memory in the address `0x401115` that the mentioned memory is being loaded, so let's set a breakpoint after this `b *main+22`, `c` and then we can reveal the contents in the address where the memory is loaded with the provided gdb command `x/4xb $rbp-0x4`, we get: `0x6b   0xc9   0x62   0x22`.

## Flag:
```picoCTF{0x6bc96222}```
