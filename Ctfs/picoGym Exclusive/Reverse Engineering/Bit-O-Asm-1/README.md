# Writeup for picoGym Exclusive : Bit-O-Asm-1

## Tools:
- Assembly code analysis
- Hexadecimal to decimal conversion
- x86 register understanding

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a text file containing assembly code that I needed to analyze. The "Bit-O-Asm" series is designed to introduce fundamental assembly language concepts, starting with basic register operations and value assignments.

The challenge required me to understand what value would be stored in a specific register after the execution of the given assembly instructions.

### 2. Examining the Assembly Code
Upon opening the provided text file, I found a simple assembly instruction that demonstrated a basic move operation. The instruction was straightforward and involved moving a hexadecimal value into the EAX register.

The key instruction I needed to analyze was:
```assembly
mov eax, 0x30
```

This instruction uses the `mov` (move) operation, which is one of the most fundamental assembly instructions. It copies the source operand (in this case, the hexadecimal value `0x30`) into the destination operand (the EAX register).

### 3. Understanding the EAX Register
The EAX register is a 32-bit general-purpose register in x86 architecture. It's commonly used for:
- Storing function return values
- Performing arithmetic operations
- Holding temporary data during computations

In this challenge, the EAX register serves as the destination for our hexadecimal value, and understanding its final contents was the key to solving the problem.

### 4. Hexadecimal to Decimal Conversion
The critical step in solving this challenge was converting the hexadecimal value `0x30` to its decimal equivalent. 

To perform this conversion:
- The hexadecimal number `0x30` represents 3 × 16¹ + 0 × 16⁰
- This equals 3 × 16 + 0 × 1 = 48 + 0 = 48

Therefore, after the execution of the `mov eax, 0x30` instruction, the EAX register contains the decimal value 48.

### 5. Verification and Solution
I verified my conversion by double-checking the hexadecimal-to-decimal calculation and confirming that `0x30` indeed equals 48 in decimal notation. This straightforward conversion gave me the answer needed for the flag format.

This challenge served as an excellent introduction to basic assembly language concepts, particularly register operations and number base conversions, which are fundamental skills in reverse engineering and low-level programming.

## Flag:
```picoCTF{48}```
