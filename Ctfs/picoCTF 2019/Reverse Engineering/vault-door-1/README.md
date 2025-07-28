# Writeup for picoCTF 2019 : vault-door-1

## Tools:
- Java source code analysis
- Text editor for code examination
- Character position mapping
- String reconstruction techniques

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Java source file that appeared to implement some form of password validation system. The challenge title "vault-door-1" suggested that I needed to find the correct password or key to "unlock" the vault and retrieve the flag.

Unlike binary reverse engineering challenges, having access to the Java source code allowed me to directly examine the validation logic and understand exactly what password the program was expecting.

### 2. Examining the Java Source Code
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My focus was on identifying the password validation mechanism and understanding how the program determined whether a given input was correct.

The code analysis revealed that the program contained a `checkPassword` function that implemented the core validation logic, making this the primary target for my analysis.

### 3. Analyzing the CheckPassword Function
Upon examining the `checkPassword` function, I discovered that it contained a series of character-by-character comparisons. The function used the `charAt()` method to check specific positions within the input password against hardcoded character values.

The validation logic was implemented as a long chain of boolean conditions connected with logical AND operators, meaning that all conditions had to be true for the password to be accepted.

### 4. Understanding the Character Position Logic
The key insight was recognizing that each `charAt()` call specified a particular position in the password string and compared it against a specific character. The function structure revealed:

```java
               password.charAt(0)  == 'd' &&
               password.charAt(29) == 'a' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '6' &&
               password.charAt(30) == 'f' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == 'd' &&
               password.charAt(26) == 'f' &&
               password.charAt(31) == '4';
```

Each line in this validation chain told me exactly which character should appear at each position in the correct password.

### 5. Developing the Reconstruction Strategy
Rather than trying to solve this puzzle manually by looking at the scattered conditions, I developed a systematic approach to reconstruct the password:

1. **Position mapping**: Create a mapping of each position (0-31) to its required character
2. **Sequential reconstruction**: Build the password by placing each character in its correct position
3. **Verification**: Ensure all 32 positions were accounted for

### 6. Character Position Extraction and Mapping
I systematically went through each `charAt()` comparison and extracted the position-character pairs:

- Position 0: 'd'
- Position 1: '3'
- Position 2: '5'
- Position 3: 'c'
- And so on...

This methodical approach ensured that I didn't miss any characters or misplace them in the final password.

### 7. Password Reconstruction
By arranging all the characters according to their specified positions (from `charAt(0)` through `charAt(31)`), I reconstructed the complete password that the validation function was expecting.

The systematic reconstruction process revealed the password in its proper sequence, which followed the standard picoCTF flag format.

### 8. Verification and Solution
Once I had reconstructed the complete password, I verified that:
- All 32 character positions were filled
- The result followed the expected picoCTF flag format
- The character sequence made logical sense as a flag

The successful reconstruction confirmed that my analysis and systematic approach were correct.

### 9. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **Source code analysis**: How to systematically examine validation logic in high-level languages
- **Character position mapping**: Techniques for reconstructing scrambled strings from validation conditions
- **Systematic problem-solving**: The importance of methodical approaches over ad-hoc puzzle solving
- **Validation logic understanding**: How programs implement character-by-character input verification

The challenge served as an excellent introduction to analyzing password validation systems and highlighted the security risks of embedding validation logic directly in client-accessible code.

## Flag:
```picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}```
