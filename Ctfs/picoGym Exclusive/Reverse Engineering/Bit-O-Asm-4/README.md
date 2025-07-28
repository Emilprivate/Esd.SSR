# Writeup for picoGym Exclusive : Bit-O-Asm-4

## Tools:
- Assembly code analysis
- Conditional branching understanding
- Hexadecimal comparison and arithmetic
- C++ pseudocode translation

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the fourth installment in the "Bit-O-Asm" series, introducing conditional branching and control flow concepts. Unlike the previous challenges that focused on straightforward arithmetic operations, this one required understanding how assembly implements conditional logic and branching instructions.

The challenge presented me with assembly code containing conditional statements that I needed to analyze to determine which execution path would be taken and what the final result would be.

### 2. Examining the Assembly Instructions
Upon analyzing the provided assembly code, I identified a sequence of instructions that implemented a conditional branch structure. The code contained:
- A comparison operation between two hexadecimal values
- A conditional jump instruction based on the comparison result
- Two different arithmetic operations depending on which branch was taken
- Final storage of the result in the EAX register

### 3. Identifying the Conditional Logic
Through careful analysis of the assembly instructions, I determined that the program was implementing a conditional statement that compared a value against a threshold and performed different arithmetic operations based on the result.

The key elements I identified were:
- **Initial value**: `0x9fe1a` (the value being tested)
- **Comparison threshold**: `0x2710` (the value used for comparison)
- **True branch operation**: Addition of `0x65`
- **False branch operation**: Subtraction of `0x65`

### 4. Translating Assembly to Pseudocode
To better understand the logic flow, I translated the assembly instructions into equivalent C++ pseudocode:

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

This translation helped clarify the conditional logic and made it easier to determine which branch would be executed.

### 5. Evaluating the Condition
To determine which branch would be taken, I needed to compare the two hexadecimal values:

**Comparison Analysis:**
- Value to test: `0x9fe1a` = 654,874 in decimal
- Threshold: `0x2710` = 10,000 in decimal
- Condition: Is 654,874 ≤ 10,000?
- Result: **False** (654,874 is much greater than 10,000)

Since the condition evaluates to false, the program would execute the `else` branch, performing the subtraction operation.

### 6. Performing the Final Calculation
With the condition determined to be false, I calculated the result of the subtraction operation:

```
0x9fe1a - 0x65 = 0x9fdb5
```

**Verification:**
- Original value: `0x9fe1a` (654,874 decimal)
- Subtract: `0x65` (101 decimal)
- Result: `0x9fdb5` (654,773 decimal)

### 7. Converting to Final Answer
The final step required converting the hexadecimal result `0x9fdb5` to its decimal equivalent for the flag format:

`0x9fdb5` = 654,773 in decimal

This challenge effectively demonstrated the importance of understanding conditional branching in assembly language and the ability to trace through different execution paths based on comparison results, skills that are crucial for more advanced reverse engineering and malware analysis tasks.

## Flag:
```picoCTF{654773}```
