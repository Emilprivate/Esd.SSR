# Writeup for picoCTF 2022 : file-run1

## Tools:
- Terminal/Command line
- File permissions management (chmod)

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a file that I needed to execute to obtain the flag. The challenge title "file-run1" immediately suggested that this was the first in a series of file execution challenges, focusing on the fundamental concept of making files executable in Unix-like systems.

The challenge required me to understand basic file permissions and how to modify them to allow program execution.

### 2. Understanding File Permissions in Unix Systems
When I first examined the provided file, I recognized that it likely didn't have the proper execution permissions set by default. In Unix-like operating systems, files have three types of permissions for three categories of users:

- **Read (r)**: Permission to view the file contents
- **Write (w)**: Permission to modify the file
- **Execute (x)**: Permission to run the file as a program

These permissions are set separately for:
- **Owner**: The user who owns the file
- **Group**: Users who belong to the file's group
- **Others**: All other users on the system

### 3. Identifying the Permission Issue
The challenge's straightforward nature suggested that the primary obstacle was simply that the file lacked execute permissions. This is a common scenario in CTF challenges designed to teach basic system administration concepts.

Without execute permissions, the operating system treats the file as a regular data file rather than an executable program, preventing it from being run even if it contains valid executable code.

### 4. Applying the Solution with chmod
To resolve the permission issue, I used the `chmod` (change mode) command to add execute permissions to the file:

```bash
chmod +x run
```

This command breakdown:
- `chmod` - the command to change file permissions
- `+x` - adds execute permission for all user categories (owner, group, others)
- `run` - the target file to modify

The `+x` modifier is a convenient shorthand that grants execute permissions without needing to specify the exact permission bits or user categories.

### 5. Executing the File
Once I had granted execute permissions to the file, I was able to run it using:

```bash
./run
```

The `./` prefix is necessary to specify that I want to execute the file in the current directory, as opposed to looking for a command with that name in the system PATH.

### 6. Flag Retrieval and Verification
When executed with the proper permissions, the program successfully ran and displayed the flag. This confirmed that the only barrier to solving the challenge was understanding and applying basic file permission concepts.

### 7. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **File permissions**: Understanding how Unix-like systems control file access
- **chmod usage**: Learning to modify file permissions using command-line tools
- **Program execution**: Basic techniques for running executable files
- **System administration basics**: Fundamental skills needed for working with Unix-like systems

The simplicity of this challenge made it an excellent introduction to file permissions and served as a foundation for more complex challenges in the file-run series that might require additional parameters or more sophisticated execution techniques.

## Flag:
```picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}```
