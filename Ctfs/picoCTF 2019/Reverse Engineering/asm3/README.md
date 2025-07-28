# Writeup for picoCTF 2019 : asm3

## Tools:
- nasm (Netwide Assembler)
- Ghidra (NSA reverse engineering framework)
- C compiler (gcc)
- Assembly code analysis

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with assembly code that I needed to analyze to determine what value would be returned given specific input parameters. The challenge represents the third installment in the "asm" series, suggesting increased complexity compared to the previous challenges.

Rather than manually tracing through the assembly instructions, I decided to take a unique approach by compiling the assembly code and then reverse engineering it using modern tools to better understand its functionality.

### 2. Developing the Compilation Strategy
I recognized that while manual assembly analysis is valuable, leveraging modern reverse engineering tools could provide clearer insights into the program's logic. My approach involved:

- Compiling the assembly code into an object file
- Using Ghidra to decompile and analyze the compiled code
- Extracting and cleaning up the pseudocode
- Creating a testable C implementation
- Executing the function with the provided challenge parameters

This methodology combines traditional reverse engineering with modern tooling to achieve accurate results.

### 3. Assembly Compilation Process
I began by compiling the provided assembly code into an object file using nasm (Netwide Assembler):

```bash
nasm -f elf32 test-cleaned.S -o test-cleaned.o
```

This command:
- Uses the ELF32 format appropriate for 32-bit x86 architecture
- Compiles the cleaned assembly source file
- Produces an object file suitable for analysis in Ghidra

The compilation step was crucial for making the assembly code accessible to modern reverse engineering tools.

### 4. Ghidra Analysis and Decompilation
After successfully compiling the object file, I loaded it into Ghidra for comprehensive analysis. Ghidra's decompilation engine generated the following pseudocode:

```C
ushort asm3(undefined4 param_1,undefined4 param_2,undefined4 param_3)
{
  return CONCAT11((undefined)param_2,-param_2._1_1_) ^ param_3._2_2_;
}
```

While this pseudocode captured the essential logic, it contained Ghidra-specific notation that needed to be translated into standard C code for better understanding and testing.

### 5. Pseudocode Cleanup and Translation
The raw Ghidra output required significant cleanup to create readable and executable C code. Through careful analysis of the Ghidra pseudocode and understanding of the underlying assembly operations, I translated it into the following clean C implementation:

```C
uint16_t asm3(uint32_t param_1, uint32_t param_2, uint32_t param_3) {
    uint8_t byte1 = (uint8_t)param_2;
    uint8_t byte2 = -(param_2 >> 8);
    uint16_t result = (byte1 << 8) | byte2;
    return result ^ (param_3 >> 16);
}
```

This cleaned version clearly shows the function's logic:
- Extracts the lower byte of param_2
- Negates the second byte of param_2
- Combines these bytes into a 16-bit value
- XORs the result with the upper 16 bits of param_3

### 6. Creating the Test Implementation
To verify the function's behavior and calculate the flag, I created a complete C program that included the cleaned function and a main routine to test it with the challenge parameters:

```C
#include <stdint.h>
#include <stdio.h>

uint16_t asm3(uint32_t param_1, uint32_t param_2, uint32_t param_3) {
    uint8_t byte1 = (uint8_t)param_2;
    uint8_t byte2 = -(param_2 >> 8);
    uint16_t result = (byte1 << 8) | byte2;
    return result ^ (param_3 >> 16);
}

int main(int argc, char* argv[])
{
    printf("0x%x\n", asm3(0xba6c5a02,0xd101e3dd,0xbb86a173));
    return 0;
}
```

### 7. Execution and Flag Extraction
When I compiled and executed the test program, it produced the following output:

```
❯ ./main                                                       │
0x669b
```

This result represents the hexadecimal value returned by the assembly function when called with the challenge parameters.

### 8. Methodology Reflection and Learning Outcomes
While this approach may not represent the traditional method for solving assembly challenges, it demonstrates several important concepts:

- **Tool Integration**: Combining multiple reverse engineering tools for comprehensive analysis
- **Modern Approach**: Leveraging contemporary tools to solve traditional problems
- **Verification**: Creating testable implementations to validate understanding
- **Practical Problem-Solving**: Focusing on achieving accurate results through available resources

The challenge reinforced that in CTF competitions, the quality of the solution often matters less than arriving at the correct answer, and creative approaches using available tools are perfectly valid.

All supporting files can be found in the workfolder for reference and reproducibility.

## Flag:
```0x669b```
