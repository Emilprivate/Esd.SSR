# Writeup for picoCTF 2019 : asm4
## Steps:
Similar to the last assembly challenge (asm3) I cleaned up the assembly code and compiled it.

`nasm -f elf32 test_cleaned.S -o test_cleaned.o`

After that I opened the object file up using Ghidra and used Ghidra's decompiler to decompile the `asm4` function to pseudo C code.

```C
int asm4(const char *param_1)
{
    int local_14;
    int local_10;
    int local_c;
  
    local_14 = 0x27a;
    for (local_10 = 0; param_1[local_10] != '\0'; local_10 = local_10 + 1) {
    }
    for (local_c = 1; local_c < local_10 - 1; local_c = local_c + 1) {
        local_14 = ((int)param_1[local_c + 1] - (int)param_1[local_c]) +
                   ((int)param_1[local_c] - (int)param_1[local_c - 1]) +
                   local_14;
    }
    return local_14;
}
```

After that we just had to setup the `main` function similar to `asm3`, call `asm4` using the given argument from the challenge and we should get the flag.

```C
#include <stdio.h>

int asm4(const char *param_1)
{
    int local_14;
    int local_10;
    int local_c;
  
    local_14 = 0x27a;
    for (local_10 = 0; param_1[local_10] != '\0'; local_10 = local_10 + 1) {
    }
    for (local_c = 1; local_c < local_10 - 1; local_c = local_c + 1) {
        local_14 = ((int)param_1[local_c + 1] - (int)param_1[local_c]) +
                   ((int)param_1[local_c] - (int)param_1[local_c - 1]) +
                   local_14;
    }
    return local_14;
}

int main(void){
    printf("0x%x\n", asm4("picoCTF_f97bb"));
    return 0;
}
```

```
> ./main
0x265
```

## Flag:
``` 0x265 ```
