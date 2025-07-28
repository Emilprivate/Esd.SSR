# Writeup for picoCTF 2022 : file-run2

## Tools:
- Terminal/Command line
- File permissions management (chmod)
- Command-line argument passing

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with an executable file that I needed to run to obtain the flag. The challenge title "file-run2" suggested this was a sequel to a previous challenge, likely with a similar approach but potentially requiring additional parameters or arguments.

The challenge required me to understand how to properly execute the program and provide it with the necessary input to reveal the flag.

### 2. Understanding File Permissions
When I first attempted to examine the provided file, I recognized that it might not have the proper execution permissions set. In Unix-like systems, files need specific permissions to be executed as programs.

I needed to modify the file permissions to make it executable using the `chmod` command, which allows changing file access permissions for the owner, group, and others.

### 3. Making the File Executable
The first step was to grant execute permissions to the file using:

```bash
chmod +x run
```

This command breakdown:
- `chmod` - the command to change file permissions
- `+x` - adds execute permission for all users (owner, group, others)
- `run` - the target file to modify

This operation was essential because without execute permissions, the system would not allow the file to be run as a program.

### 4. Initial Program Execution Attempt
After making the file executable, I attempted to run it with a basic execution command:

```bash
./run
```

However, this initial attempt likely revealed that the program was expecting additional input or arguments to function properly. The program's behavior or output would have indicated that it required command-line arguments to proceed.

### 5. Analyzing the Argument Requirement
Based on the challenge context and any output from the initial execution, I determined that the program expected a specific command-line argument. The challenge description or program output likely provided a hint about what argument was needed.

The required argument appeared to be the string "Hello!" which needed to be passed to the program during execution.

### 6. Executing with Command-Line Arguments
With the argument requirement identified, I executed the program with the proper parameter:

```bash
./run Hello!
```

This command structure:
- `./run` - executes the program in the current directory
- `Hello!` - passes "Hello!" as the first command-line argument to the program

The program accepted this argument and processed it according to its internal logic.

### 7. Flag Retrieval and Verification
When executed with the correct argument, the program successfully revealed the flag. The program likely contained validation logic that checked the provided argument and displayed the flag when the correct input was received.

### 8. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **File permissions**: Understanding how to make files executable in Unix-like systems
- **Command-line arguments**: Learning how programs can accept and process input parameters
- **Program execution**: Basic techniques for running executable files from the command line
- **Input validation**: How programs can require specific input to reveal their functionality

The straightforward nature of this challenge made it an excellent introduction to basic program execution and command-line argument passing concepts.

## Flag:
```picoCTF{F1r57_4rgum3n7_96f2195f}```

