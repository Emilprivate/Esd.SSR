# Writeup for picoCTF 2019 : asm3
## Steps:
For this challenge I decided to compile the assembly code into an object file. From there I would reverse it using Ghidra to see the decompiled function and then clean that code up and import it into a `main.c` file, call the function with the given challenge parameters and get the flag from the result.

Not entirely sure if this challenge was meant to be solved like so, but I've learned throughout ctf challenges that getting to the result matters more than the quality of the solution, so I'm assuming that it's a valid solution.

All files can be found in the workfolder.

`nasm -f elf32 test-cleaned.S -o test-cleaned.o`

After opening and decompiling `test-cleaned.o` in Ghidra we get:

```C
ushort asm3(undefined4 param_1,undefined4 param_2,undefined4 param_3)

{
  return CONCAT11((undefined)param_2,-param_2._1_1_) ^ param_3._2_2_;
}
``` 

If we clean that pseudo code up, we get the following:

```C
uint16_t asm3(uint32_t param_1, uint32_t param_2, uint32_t param_3) {
    uint8_t byte1 = (uint8_t)param_2;
    uint8_t byte2 = -(param_2 >> 8);
    uint16_t result = (byte1 << 8) | byte2;
    return result ^ (param_3 >> 16);
}
```

And then we can call this function like so:

```C
#include <stdint.h>
#include <stdio.h>

uint16_t asm3(uint32_t param_1, uint32_t param_2, uint32_t param_3) {
    uint8_t byte1 = (uint8_t)param_2;
    uint8_t byte2 = -(param_2 >> 8);
    uint16_t result = (byte1 << 8) | byte2;
    return result ^ (param_3 >> 16);
}

int main(int argc, char* argv[])
{
    printf("0x%x\n", asm3(0xba6c5a02,0xd101e3dd,0xbb86a173));
    return 0;
}
```

```
❯ ./main                                                       │
0x669b
```

## Flag:
``` 0x669b ```
