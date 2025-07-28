# Writeup for picoGym Exclusive : GDB baby step 3

## Tools:
- GDB (GNU Debugger)
- Memory examination commands
- Breakpoint management
- Stack pointer analysis

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the third step in the "GDB baby step" series, building upon the debugging skills developed in the previous challenges. Unlike the earlier challenges that focused on register values, this one required understanding memory examination techniques and stack-based data storage.

The challenge instructions provided specific guidance on using GDB memory examination commands, making this an excellent opportunity to learn about inspecting memory contents at specific addresses relative to stack pointers.

### 2. Loading the Binary and Setting Initial Breakpoint
I began by launching GDB with the target binary and setting up the debugging environment. Following the challenge instructions, my first step was to establish a breakpoint at the main function to pause execution at the program's entry point:

```bash
(gdb) b *main
```

This initial breakpoint allowed me to start the program under controlled conditions and examine its behavior from the beginning.

### 3. Starting Program Execution
With the breakpoint set, I initiated program execution using the run command:

```bash
(gdb) r
```

The program started and immediately paused at the main function breakpoint, giving me the opportunity to analyze the code and identify where the relevant memory operations would occur.

### 4. Analyzing Memory Loading Operations
During my examination of the program execution, I observed that at memory address `0x401115`, there was a significant memory loading operation taking place. This address appeared to be loading data that would be crucial for solving the challenge.

The challenge instructions specifically mentioned this address, confirming that this was where the important memory operation occurred. Understanding this loading operation was key to determining where to place my next breakpoint.

### 5. Strategic Breakpoint Placement
Based on the analysis of the memory loading operation at `0x401115`, I calculated that I needed to set a breakpoint 22 bytes after the main function to capture the memory state after the loading operation completed:

```bash
(gdb) b *main+22
```

This strategic placement ensured that I would pause execution after all relevant memory operations had finished, allowing me to examine the final state of the data that had been loaded.

### 6. Continuing to the Target Breakpoint
With the second breakpoint set, I continued program execution:

```bash
(gdb) c
```

The program executed through the memory loading operations and paused at my strategically placed breakpoint, positioning me perfectly to examine the memory contents that had been loaded.

### 7. Memory Examination Using GDB Commands
The challenge provided a specific GDB command for examining the memory contents at the target location. I used the memory examination command to inspect 4 bytes in hexadecimal format at the stack location `$rbp-0x4`:

```bash
(gdb) x/4xb $rbp-0x4
```

This command breaks down as follows:
- `x` - examine memory command
- `/4/` - format specifier (4 bytes)
- `x` - output in hexadecimal
- `$rbp-0x4` - memory address (4 bytes below the base pointer)

### 8. Extracting the Memory Contents
The memory examination revealed the following byte sequence:
```
0x6b   0xc9   0x62   0x22
```

These four bytes represented the data that had been loaded into memory at the specified stack location. The values were displayed in the order they appeared in memory, providing the exact hexadecimal representation needed for the flag.

### 9. Constructing the Final Flag
The challenge required me to combine these hexadecimal values into a single flag format. By concatenating the four bytes in the order they appeared, I obtained:

`0x6bc96222`

This challenge effectively demonstrated the importance of memory examination techniques in debugging and reverse engineering, showing how to use GDB's memory inspection capabilities to extract data from specific stack locations.

## Flag:
```picoCTF{0x6bc96222}```
