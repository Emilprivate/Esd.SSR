# Writeup for picoCTF 2019 : asm4

## Tools:
- nasm (Netwide Assembler)
- Ghidra (NSA reverse engineering framework)
- C compiler (gcc)
- Assembly code analysis

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with assembly code that I needed to analyze to determine what value would be returned given a specific input parameter. The challenge represents the fourth installment in the "asm" series, suggesting increased complexity compared to the previous challenges.

Building upon my successful approach from asm3, I decided to use the same methodology of compiling the assembly code and then reverse engineering it using modern tools to better understand its functionality.

### 2. Assembly Compilation Strategy
Following the proven approach from the previous challenge, I decided to compile the assembly code into an object file and then use Ghidra's powerful decompilation capabilities to understand the program's logic.

This methodology combines traditional reverse engineering with modern tooling to achieve accurate results, particularly effective for more complex assembly programs that involve loops and string processing.

### 3. Assembly Compilation Process
I began by compiling the provided assembly code into an object file using nasm (Netwide Assembler):

```bash
nasm -f elf32 test_cleaned.S -o test_cleaned.o
```

This command:
- Uses the ELF32 format appropriate for 32-bit x86 architecture
- Compiles the cleaned assembly source file
- Produces an object file suitable for analysis in Ghidra

The compilation step was crucial for making the assembly code accessible to modern reverse engineering tools.

### 4. Ghidra Analysis and Decompilation
After successfully compiling the object file, I loaded it into Ghidra for comprehensive analysis. Ghidra's decompilation engine generated readable pseudocode that revealed the program's underlying logic.

The decompiled `asm4` function showed:

```C
int asm4(const char *param_1)
{
    int local_14;
    int local_10;
    int local_c;
  
    local_14 = 0x27a;
    for (local_10 = 0; param_1[local_10] != '\0'; local_10 = local_10 + 1) {
    }
    for (local_c = 1; local_c < local_10 - 1; local_c = local_c + 1) {
        local_14 = ((int)param_1[local_c + 1] - (int)param_1[local_c]) +
                   ((int)param_1[local_c] - (int)param_1[local_c - 1]) +
                   local_14;
    }
    return local_14;
}
```

### 5. Algorithm Analysis and Understanding
The decompiled code revealed a sophisticated string processing algorithm with several key components:

**Initialization Phase:**
- `local_14` is initialized to `0x27a` (634 in decimal) as an accumulator
- The function takes a string parameter (`param_1`)

**String Length Calculation:**
- The first loop iterates through the string to find its length
- `local_10` stores the final string length after the loop completes

**Character Difference Processing:**
- The second loop processes characters from index 1 to length-2
- For each character position, it calculates differences between adjacent characters
- The algorithm computes: `(next_char - current_char) + (current_char - previous_char)`
- These differences are accumulated in `local_14`

This represents a form of second-order difference calculation on ASCII values.

### 6. Creating the Test Implementation
To verify the function's behavior and calculate the flag, I created a complete C program that included the cleaned function and a main routine to test it with the challenge parameters:

```C
#include <stdio.h>

int asm4(const char *param_1)
{
    // ...existing code...
}

int main(void){
    printf("0x%x\n", asm4("picoCTF_f97bb"));
    return 0;
}
```

The challenge provided the specific input string `"picoCTF_f97bb"` that needed to be processed by the algorithm.

### 7. Execution and Flag Extraction
When I compiled and executed the test program, it produced the following output:

```
> ./main
0x265
```

This result represents the hexadecimal value returned by the assembly function when called with the challenge parameter.

### 8. Algorithm Verification
The algorithm processes the string `"picoCTF_f97bb"` by:
1. Starting with an initial value of `0x27a`
2. Calculating character differences for each internal character
3. Accumulating these differences to produce the final result `0x265`

### 9. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **String processing algorithms**: Understanding how assembly can implement complex text analysis
- **Character arithmetic**: Working with ASCII values and their differences
- **Accumulator patterns**: Recognizing common assembly programming techniques
- **Tool integration**: Leveraging modern tools to understand legacy code

The challenge showed how assembly programs can implement sophisticated algorithms that become much clearer when viewed through decompilation tools.

## Flag:
```0x265```
