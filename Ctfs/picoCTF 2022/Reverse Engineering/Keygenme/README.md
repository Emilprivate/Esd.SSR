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

## Flag
```picoCTF{br1ng_y0ur_0wn_k3y_19836cd8}```
