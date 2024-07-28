# Writeup for picoGym Exclusive : Bit-O-Asm-4
## Steps:
Below I've pseudo translated the assembly to code and as we can see, since 0x9fe1a is not less or equal to 0x2710, we subtract 0x65 and get 0x9FDB5.

## Translated to code:
```cpp
int x4 = 0x9fe1a;
if (x4 <= 0x2710)
{
  x4 += 0x65;   
}else{
  x4 -= 0x65;
}
eax = x4;
```

## Flag:
```picoCTF{654773}```
