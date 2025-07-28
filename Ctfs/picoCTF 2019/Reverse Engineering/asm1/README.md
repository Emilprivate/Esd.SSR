# Writeup for picoCTF 2019 : asm1

## Tools:
- Assembly code analysis
- Pseudocode translation
- Conditional logic tracing
- Hexadecimal arithmetic

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with an assembly code snippet that I needed to analyze to determine what value would be returned given a specific input. The challenge required understanding assembly language syntax, conditional branching, and arithmetic operations.

The assembly code contained multiple conditional branches and arithmetic operations that needed to be traced through systematically to determine the final result.

### 2. Understanding the Input Parameter
The challenge provided a specific input value that I needed to trace through the assembly code. The input value was `0x8be`, which equals 2238 in decimal. This value served as the starting point for analyzing the program's execution flow.

### 3. Analyzing the Assembly Structure
Upon examining the assembly code, I identified several key components:
- Multiple conditional jump instructions that created branching logic
- Comparison operations that tested the input against specific threshold values
- Arithmetic operations (addition and subtraction) performed on the input
- Register operations involving the EAX register for return values

### 4. Translating Assembly to Pseudocode
To better understand the program's logic flow, I systematically translated the assembly instructions into equivalent pseudocode. This translation process helped clarify the conditional structure and made it easier to trace through the execution path.

## Translated to pseudocode:
```c
int userInput = 0x8be; // 2238 in decimal

if (userInput > 0x71c) // 1820 in decimal
{
  if(userInput != 0x8be) // 2238 in decimal
  {
    eax = userInput;
    eax += 0x3;
    return eax;
  }
  else
  {
    eax = userInput;
    eax -= 0x3;
    return eax;
  }
}
else
{
  if (userInput != 0x6cf) // 1743 in decimal
  {
    eax = userInput;
    eax -= 0x3;
    return eax;
  }
}
```

### 5. Tracing the Execution Path
With the pseudocode translation complete, I traced through the execution path using the provided input value `0x8be` (2238):

**Step 1: First Conditional Check**
- Check: `userInput > 0x71c` (2238 > 1820)
- Result: **True** - proceed to the nested if statement

**Step 2: Nested Conditional Check**
- Check: `userInput != 0x8be` (2238 != 2238)
- Result: **False** - proceed to the else branch

**Step 3: Execute Else Branch**
- Set `eax = userInput` (eax = 0x8be)
- Perform `eax -= 0x3` (subtract 3 from the value)
- Return the result

### 6. Performing the Final Calculation
Based on the execution path analysis, the final operation performed was:
```
0x8be - 0x3 = 0x8bb
```

**Verification:**
- Original value: `0x8be` (2238 decimal)
- Subtract: `0x3` (3 decimal)
- Result: `0x8bb` (2235 decimal)

### 7. Learning Outcomes
This challenge effectively demonstrated several important assembly analysis concepts:
- **Conditional branching**: Understanding how assembly implements if-else logic
- **Comparison operations**: Analyzing how values are compared in assembly
- **Register operations**: Following how values are stored and modified in registers
- **Pseudocode translation**: Converting assembly to higher-level language for easier analysis

The systematic approach of translating assembly to pseudocode and then tracing execution paths proved to be an effective method for understanding complex conditional logic in assembly programs.

## Flag:
```0x8bb```
