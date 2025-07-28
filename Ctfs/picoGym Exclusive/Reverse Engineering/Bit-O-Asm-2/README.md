# Writeup for picoGym Exclusive : Bit-O-Asm-2

## Tools:
- Assembly code analysis
- Stack pointer understanding
- Hexadecimal to decimal conversion
- x86-64 register knowledge

## Steps:

### 1. Initial Challenge Analysis
This challenge is the second in the "Bit-O-Asm" series, building upon the fundamental assembly concepts introduced in the first challenge. Unlike the previous challenge that dealt with simple register assignments, this one required understanding stack operations and memory addressing.

The challenge presented me with assembly code that I needed to analyze to determine what value would be accessed or stored at a specific memory location relative to the base pointer.

### 2. Understanding Stack Frame Operations
The key to solving this challenge was understanding how stack frames work in x86-64 assembly. The instruction I needed to analyze involved accessing memory relative to the RBP (base pointer) register.

The critical instruction pattern involved:
- A memory location specified as `rbp-0x4`
- A previous instruction that stored a value at this location
- The need to determine what value was stored there

### 3. Analyzing the Assembly Instructions
Upon examining the provided assembly code, I identified that there was a prior instruction that moved a hexadecimal value to the memory location `rbp-0x4`. This is a common pattern in assembly where:

- `rbp` represents the base pointer of the current stack frame
- `-0x4` indicates an offset of 4 bytes below the base pointer
- This location is typically used for local variables in the function

The specific value that was moved to this location in the prior instruction was `0x9fe1a`.

### 4. Memory Address Calculation
The instruction `rbp-0x4` refers to a memory address that is 4 bytes below the current base pointer. In x86-64 architecture:
- The base pointer (RBP) points to the bottom of the current stack frame
- Subtracting from RBP moves toward local variables stored on the stack
- The offset `-0x4` represents a 32-bit (4-byte) value stored just below the base pointer

### 5. Hexadecimal to Decimal Conversion
The final step was converting the hexadecimal value `0x9fe1a` to its decimal equivalent:

To perform this conversion:
- `0x9fe1a` in hexadecimal needs to be converted to decimal
- Breaking it down: 9×16⁴ + 15×16³ + 14×16² + 1×16¹ + 10×16⁰
- This equals: 9×65536 + 15×4096 + 14×256 + 1×16 + 10×1
- Calculating: 589824 + 61440 + 3584 + 16 + 10 = 654874

Therefore, the value stored at memory location `rbp-0x4` is 654874 in decimal.

### 6. Verification and Solution
I verified my conversion by double-checking the hexadecimal-to-decimal calculation and confirming that the memory addressing was correctly interpreted. The value `0x9fe1a` indeed converts to 654874, which provided the answer for the flag format.

This challenge effectively demonstrated the importance of understanding stack frame operations and memory addressing in assembly language, concepts that are crucial for more advanced reverse engineering tasks.

## Flag:
```picoCTF{654874}```
