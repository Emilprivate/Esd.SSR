# Writeup for picoCTF 2019 : vault-door-8
## Steps:
For this challenge there's a more complicated bitshift scramble for the password. In order to reverse the `expected` array to get the flag, we have to reverse the `scramble` function. 

We do this by reversing the order of the applied bit shift in the for loop.

```java
  public char[] unscramble(char[] scrambledPassword) {
    for (int b = 0; b < scrambledPassword.length; b++) {
        char c = scrambledPassword[b];

        c = switchBits(c, 6, 7);
        c = switchBits(c, 2, 5);
        c = switchBits(c, 3, 4);
        c = switchBits(c, 0, 1);
        c = switchBits(c, 4, 7);
        c = switchBits(c, 5, 6);
        c = switchBits(c, 0, 3);
        c = switchBits(c, 1, 2);

        scrambledPassword[b] = c;
    }
    return scrambledPassword;
  }
```

And then within the `checkPassword` function we do the following:
```java
char[] unscrambledArray = unscramble(expected);

String flag = new String(unscrambledArray);

System.out.println("Flag: " + flag);

```

```
Enter vault password: 21321312321321
Flag: s0m3_m0r3_b1t_sh1fTiNg_91c642112
Access denied
```
## Flag:
```picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112} ```
