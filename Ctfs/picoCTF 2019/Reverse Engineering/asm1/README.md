# Writeup for picoCTF 2019 : asm1
## Steps:
Below I've translated the assembly to pseudocode and the final equation comes down to:
```0x8be - 0x3``` = `0x8BB`.

## Translated:
```
int userInput = 0x8be (2238)

if (userInput > 0x71c) (1820)
{
  if(userInput != 0x8be)
  {
    eax = userInput
    eax += 0x3
    return
  }else{
    eax = userInput
    eax -= 0x3
    return;
  }
}else{
  if (userInput != 0x6cf) (1743)
  {
    eax = userInput
    eax -= 0x3
    return
  }
}
```

## Flag:
```0x8BB```
