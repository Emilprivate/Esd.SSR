# Writeup for picoCTF 2023 : Reverse

## Tools:
- Terminal/Command line
- File permissions management (chmod)
- Vim text editor
- String search utilities

## Steps:

### 1. Initial Challenge Analysis
This challenge provided me with an executable file that I needed to analyze to extract the hidden flag. The challenge title "Reverse" immediately suggested that I would need to perform reverse engineering techniques to understand the program's functionality and locate the flag.

The approach required understanding how executable files store string data and how to extract that information without necessarily understanding the complete program logic.

### 2. Making the File Executable
The first step was to ensure that the provided file had the proper permissions to be executed. I used the `chmod` command to add execute permissions:

```bash
chmod +x ret
```

This command modified the file permissions to allow execution, which was necessary for testing the program's behavior and understanding its requirements.

### 3. Initial Program Execution and Behavior Analysis
With the file now executable, I ran it to observe its behavior and understand what type of interaction it expected:

```bash
./ret
```

The program execution revealed that it was prompting for a password input. This behavior indicated that:
- The program likely contains password validation logic
- The correct password might be stored somewhere within the executable
- The flag could be revealed upon entering the correct password

### 4. Choosing the Analysis Approach
Rather than attempting to reverse engineer the entire password validation algorithm or trying to guess the password through brute force, I decided to examine the executable file directly for embedded strings. This approach is effective because:

- Executable files often contain readable string literals
- Passwords and flags are frequently stored as plain text strings within binaries
- Simple text-based analysis can reveal important information quickly
- It avoids the complexity of understanding the complete program logic

### 5. String Analysis Using Vim
I opened the executable file in Vim to examine its contents for readable strings:

```bash
vim ret
```

While executable files are primarily binary data, they often contain embedded ASCII strings that remain readable when viewed in a text editor. These strings can include:
- User prompts and messages
- Error messages
- Hardcoded passwords or keys
- Flag data

### 6. Targeted String Search
Instead of manually scrolling through the potentially large file, I used Vim's search functionality to look for flag-related content. Since picoCTF flags always begin with "picoCTF{", I searched for the substring "pico":

```
/pico
```

This targeted search strategy was effective because:
- It focused on the most distinctive part of the flag format
- It avoided having to read through irrelevant binary data
- It provided immediate results if a flag was embedded in the file

### 7. Flag Discovery and Extraction
The search successfully located the flag string embedded within the executable file. The flag appeared as a readable string literal, indicating that it was likely used in the program's output or validation logic.

### 8. Verification and Solution
Once I found the flag string, I verified that it followed the expected picoCTF format and contained reasonable content. The flag structure confirmed that this was indeed the correct solution and that the simple string-based analysis approach was sufficient for this challenge.

### 9. Learning Outcomes
This challenge effectively demonstrated:
- The accessibility of string data within compiled executables
- The effectiveness of simple text-based analysis for basic reverse engineering
- How flags can be embedded as string constants in binary files
- The utility of targeted search strategies in file analysis

The straightforward nature of this challenge made it an excellent introduction to executable file analysis and reinforced that sometimes the most direct approaches are the most effective in CTF scenarios.

## Flag:
```picoCTF{3lf_r3v3r5ing_succe55ful_1de05085}```
