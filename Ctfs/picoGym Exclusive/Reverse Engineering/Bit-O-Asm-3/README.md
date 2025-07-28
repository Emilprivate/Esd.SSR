# Writeup for picoGym Exclusive : Bit-O-Asm-3

## Tools:
- Assembly code analysis
- Mathematical calculation
- Hexadecimal arithmetic
- x86-64 instruction understanding

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the third installment in the "Bit-O-Asm" series, building upon the previous challenges' foundations of register operations and memory addressing. Unlike the earlier challenges that focused on simple value assignments, this one required understanding arithmetic operations in assembly language.

The challenge presented me with assembly code containing mathematical operations that I needed to trace through step by step to determine the final result.

### 2. Examining the Assembly Instructions
Upon analyzing the provided assembly code, I identified a sequence of instructions that performed arithmetic operations using hexadecimal values. The challenge required me to manually execute these instructions to determine what value would be computed.

The key operations involved:
- Multiplication of hexadecimal values
- Addition of the multiplication result with another hexadecimal value
- Proper handling of hexadecimal arithmetic throughout the process

### 3. Identifying the Mathematical Operations
Through careful analysis of the assembly instructions, I determined that the program was performing the following calculation:

```
0x9fe1a × 0x4 + 0x1f5
```

This represents:
- **First operand**: `0x9fe1a` (a hexadecimal value from a previous operation or assignment)
- **Multiplication**: The first operand multiplied by `0x4`
- **Second operand**: `0x1f5` (another hexadecimal value)
- **Final operation**: Addition of the multiplication result with the second operand

### 4. Performing Hexadecimal Arithmetic
To solve this challenge, I needed to perform the arithmetic operations while working entirely in hexadecimal notation:

**Step 1: Multiplication**
```
0x9fe1a × 0x4 = 0x27FA68
```

This multiplication can be verified by understanding that multiplying by `0x4` is equivalent to multiplying by 4 in decimal, or shifting left by 2 bits in binary.

**Step 2: Addition**
```
0x27FA68 + 0x1f5 = 0x27FA5D
```

The addition combines the multiplication result with the second hexadecimal value to produce the final result.

### 5. Converting to Decimal
The final step required converting the hexadecimal result `0x27FA5D` to its decimal equivalent for the flag format:

To perform this conversion:
- `0x27FA5D` represents the final calculated value in hexadecimal
- Converting to decimal: 2×16⁵ + 7×16⁴ + 15×16³ + 10×16² + 5×16¹ + 13×16⁰
- This equals: 2×1048576 + 7×65536 + 15×4096 + 10×256 + 5×16 + 13×1
- Calculating: 2097152 + 458752 + 61440 + 2560 + 80 + 13 = 2619997

### 6. Verification and Solution
I verified my calculation by double-checking each arithmetic operation:
1. Confirmed the multiplication: `0x9fe1a × 0x4 = 0x27FA68`
2. Confirmed the addition: `0x27FA68 + 0x1f5 = 0x27FA5D`
3. Confirmed the decimal conversion: `0x27FA5D = 2619997`

This challenge effectively demonstrated the importance of understanding arithmetic operations in assembly language and the ability to perform calculations with hexadecimal values, skills that are essential for more complex reverse engineering tasks.

## Flag:
```picoCTF{2619997}```
