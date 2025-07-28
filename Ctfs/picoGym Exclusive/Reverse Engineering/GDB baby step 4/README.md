# Writeup for picoGym Exclusive : GDB baby step 4

## Tools:
- GDB (GNU Debugger)
- Function analysis
- Assembly instruction examination
- Register value inspection

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the fourth step in the "GDB baby step" series, continuing to build upon the debugging skills developed in the previous challenges. Unlike the earlier challenges that focused primarily on the main function, this one required analyzing a separate function and understanding arithmetic operations within that specific function.

The challenge instructions hinted that I needed to examine a particular function and identify a multiplication operation involving the EAX register, making this an exercise in targeted function analysis rather than general program exploration.

### 2. Loading the Binary and Function Discovery
I began by launching GDB with the target binary and performing initial reconnaissance to understand the program's function structure. My first step was to examine all available functions to identify the target function mentioned in the challenge.

Using the `info functions` command, I explored the binary's function layout:

```bash
(gdb) info functions
```

Through this command, I discovered the presence of a function named `func1`, which appeared to be the target function I needed to analyze based on the challenge context and naming convention.

### 3. Setting Up Function Analysis
With `func1` identified as the target function, I prepared to analyze its contents by setting a breakpoint directly at the function's entry point. This approach would allow me to examine the function's assembly instructions and register operations in detail.

I set the breakpoint using:

```bash
(gdb) b *func1
```

This breakpoint placement ensured that execution would pause at the beginning of `func1`, giving me the opportunity to examine the function's assembly code and trace through its operations.

### 4. Initiating Program Execution
With the breakpoint set at `func1`, I started the program execution:

```bash
(gdb) r
```

The program began running and paused when it reached the `func1` function, positioning me perfectly to analyze the function's internal operations and identify the specific arithmetic instruction mentioned in the challenge.

### 5. Analyzing the Function's Assembly Instructions
Once execution paused at the `func1` breakpoint, I was able to examine the function's assembly code without needing to disassemble the entire memory layout. The challenge specifically mentioned that there would be a multiplication operation involving the EAX register.

Through careful examination of the function's instructions, I identified the key operation that the challenge was referencing. The assembly code revealed a multiplication instruction that involved the hexadecimal value `0x3269` being processed with the EAX register.

### 6. Identifying the Target Value
The critical discovery was the hexadecimal value `0x3269` that appeared in the multiplication operation within `func1`. According to the challenge description, this value represented the answer I needed to extract.

The challenge design made it clear that I didn't need to trace through the entire execution or perform complex calculations - the value `0x3269` itself was the key information required for the solution.

### 7. Converting to Decimal Format
The final step involved converting the hexadecimal value `0x3269` to its decimal equivalent for the flag format:

**Conversion Process:**
- Hexadecimal value: `0x3269`
- Decimal calculation: 3×16³ + 2×16² + 6×16¹ + 9×16⁰
- This equals: 3×4096 + 2×256 + 6×16 + 9×1
- Calculating: 12288 + 512 + 96 + 9 = 12905

Therefore, the decimal equivalent of `0x3269` is 12905.

### 8. Verification and Solution
I verified the hexadecimal-to-decimal conversion to ensure accuracy, confirming that `0x3269` indeed equals 12905. This value matched the expected format for the challenge flag.

This challenge effectively demonstrated the importance of targeted function analysis in debugging scenarios and showed how GDB can be used to examine specific functions within a program without needing to analyze the entire binary structure.

## Flag:
```picoCTF{12905}```
