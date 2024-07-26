# Writeup for picoCTF-2022 : Keygenme

## Steps
- First give the application execution permissions:
```chmod +x keygenme```

- After running the application we see that we need a license:

![running_keygen](executing_keygen.png)

- Opening this keygen in ghidra, we can locate one of the output strings under 'Defined strings' and follow the cross-reference to it and see the decompiled code of the main function:

![defined_strings](defined_strings.png)
![cross_referenced_string](cross_reference_string.png)
![cross_referenced_code](cross_referenced_code.png)
![decompiled_code](decompiled_code.png)

- In the decompiled main function we can see that before the if-branch there's a validation process where `cVar1` is being assigned the result of some function (presumably some validation function) with `local_38` as argument which is the user input of the requested license with size 40 characters. However, we can see that fgets only takes `0x25` in hex or `37` in decimal as the size of the input, so we can safely assume that the input is capped at 37 characters or rather 36 characters to leave room for the null terminator `\0`.

- If we dig deeper into the presumed validation function to see the structure and decompiled pseudocode of it, we see a bunch of poorly decompiled code using Ghidra, this task would be better for IDA64 or some other decompiler. However, there was a part of the decompiled code that did turn out to be useful as shown in the picture below but still knowing this, we can try to use GDB instead.

![decompiled_val_func](decompiled_validation_func.png)

- In the picture above we can see that there's an if statement checking if the length of the given argument is `0x24` or `36` characters long. We can use this to get to the assembly in GDB, find the correct compare instruction, set a breakpoint and see if there are any useful strings that can point to the flag. 

- Opening up GDB using `gdb keygenme`, we can immidietely run `info functions` to see what functions we can work with. As we can see the main function is not there because the binary is `stripped` which you can see by running `file keygenme`, this means that the debugging information and symbols have been removed from the binary, however, we do have printf and fgets which we can use to get to the main function.

![functions](info_functions.png)



## Flag
```picoCTF{br1ng_y0ur_0wn_k3y_19836cd8}```
