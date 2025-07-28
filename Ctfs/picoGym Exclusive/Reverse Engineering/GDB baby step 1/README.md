# Writeup for picoGym Exclusive : GDB baby step 1

## Tools:
- GDB (GNU Debugger)
- Assembly code analysis
- Function examination
- Register value inspection

## Steps:

### 1. Initial Challenge Analysis
This challenge serves as an introduction to using GDB (GNU Debugger) for reverse engineering tasks. The "GDB baby step" series is designed to teach fundamental debugging concepts and techniques that are essential for analyzing binary executables.

The challenge required me to use GDB to examine a binary and extract specific information from its assembly code, particularly focusing on register values within the main function.

### 2. Loading the Binary in GDB
I began by launching GDB with the target binary to start my analysis. The first step in any GDB debugging session is to load the executable and familiarize myself with its structure.

Once GDB was running with the binary loaded, I needed to explore the available functions to understand the program's organization and identify where the relevant information might be located.

### 3. Exploring Available Functions
To get an overview of the program's structure, I used the `info functions` command in GDB. This command displays a comprehensive list of all functions present in the binary, including their names and memory addresses.

```bash
(gdb) info functions
```

Through this command, I confirmed the presence of a `main` function, which is typically the entry point for most C/C++ programs and often contains the core logic or the information needed for CTF challenges.

### 4. Analyzing the Main Function Assembly
With the main function identified, I proceeded to examine its assembly code to understand what operations it performs. To view the assembly layout of the main function, I used GDB's disassembly capabilities.

The assembly analysis revealed the instructions within the main function, including operations involving various registers. My focus was on identifying any operations that would place a specific value into the EAX register, as this is commonly where return values or important data are stored.

### 5. Identifying the EAX Register Value
Through careful examination of the main function's assembly code, I located the instruction that loads a value into the EAX register. The EAX register is particularly significant because:

- It's commonly used to store function return values
- It often contains the final result of calculations
- In CTF challenges, it frequently holds flag-related information

The assembly analysis revealed that the EAX register contained the decimal value 549698, which corresponded to the flag format expected for this challenge.

### 6. Verification and Solution
I verified my findings by double-checking the assembly instruction that sets the EAX register value. The consistent result confirmed that 549698 was indeed the correct value stored in EAX during the execution of the main function.

This challenge provided an excellent introduction to basic GDB usage, including function exploration, assembly code examination, and register value analysis - all fundamental skills for reverse engineering and binary analysis.

## Flag:
```picoCTF{549698}```
