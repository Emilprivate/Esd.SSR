# Writeup for picoCTF 2019 : vault-door-8

## Tools:
- Java source code analysis
- Text editor for code examination
- Java compiler (javac)
- Bit manipulation understanding

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the eighth installment in the vault door series, building upon the concepts from previous challenges while introducing significantly more complex bit manipulation techniques. The challenge title "vault-door-8" suggested that this would be one of the more advanced challenges in the series, requiring deep understanding of bitwise operations.

Unlike earlier vault door challenges that used simple character rearrangement or basic encoding, this one implemented sophisticated bit-level scrambling that required careful reverse engineering to solve.

### 2. Examining the Java Source Code Structure
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My analysis revealed that the program contained a more complex validation system compared to previous vault door challenges.

The code structure showed:
- An `expected` array containing scrambled password data
- A `scramble` function that performed bit manipulation operations
- A `switchBits` utility function for swapping individual bits
- Complex validation logic that required understanding the scrambling algorithm

### 3. Understanding the Bit Scrambling Algorithm
Upon examining the `scramble` function, I discovered that it implemented a sophisticated bit manipulation algorithm that performed multiple bit-swapping operations on each character of the password. The function executed the following sequence of bit switches:

1. Switch bits 1 and 2
2. Switch bits 0 and 3
3. Switch bits 5 and 6
4. Switch bits 4 and 7
5. Switch bits 0 and 1
6. Switch bits 3 and 4
7. Switch bits 2 and 5
8. Switch bits 6 and 7

Each operation used the `switchBits` helper function to swap specific bit positions within each character.

### 4. Analyzing the SwitchBits Function
The `switchBits` function was the core utility that enabled the bit manipulation. It worked by:
- Extracting specific bits from their original positions
- Swapping their values
- Reconstructing the character with the swapped bits

Understanding this function was crucial for developing the reverse algorithm.

### 5. Developing the Reverse Algorithm Strategy
To solve this challenge, I needed to create an `unscramble` function that would reverse the effects of the `scramble` function. The key insight was that bit-swapping operations are inherently reversible - if you swap two bits and then swap them again, you return to the original state.

However, since the scramble function applied multiple operations in sequence, I needed to reverse them in the exact opposite order to correctly unscramble the data.

### 6. Implementing the Unscramble Function
I created the reverse function by applying the same bit-swapping operations in reverse order:

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

This function applied the bit-swapping operations in exactly the reverse order of the original scramble function.

### 7. Extracting the Flag
With the unscramble function implemented, I modified the `checkPassword` function to reveal the flag:

```java
char[] unscrambledArray = unscramble(expected);

String flag = new String(unscrambledArray);

System.out.println("Flag: " + flag);
```

This code took the scrambled `expected` array, applied the unscrambling algorithm, and converted the result back to a readable string.

### 8. Executing and Verifying the Solution
When I ran the modified program, it successfully unscrambled the password and revealed the flag:

```
Enter vault password: 21321312321321
Flag: s0m3_m0r3_b1t_sh1fTiNg_91c642112
Access denied
```

The dummy password input satisfied the program's input requirements, while the unscrambling logic revealed the actual flag content.

### 9. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **Advanced bit manipulation**: Understanding complex bit-swapping algorithms
- **Reversible operations**: Recognizing how to undo sequences of bit operations
- **Algorithm analysis**: Breaking down complex scrambling functions into understandable components
- **Reverse engineering methodology**: Developing systematic approaches to undo obfuscation

The challenge showed how bit-level operations can create sophisticated obfuscation that requires careful analysis and methodical reversal to solve.

## Flag:
```picoCTF{s0m3_m0r3_b1t_sh1fTiNg_91c642112}```
