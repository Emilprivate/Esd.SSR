# Writeup for picoCTF 2022 : patchme.py

## Tools:
- Text editor
- Python interpreter
- Source code analysis
- Password extraction techniques

## Steps:

### 1. Initial Challenge Analysis
This challenge provided me with a Python file named `patchme.py`, which immediately suggested that I was dealing with a script that required some form of modification or understanding to reveal the flag. The title "patchme" hinted that the solution might involve analyzing the code to understand its requirements rather than actually modifying it.

The challenge required me to examine the Python source code to understand how the program validates input and what specific input would trigger the flag disclosure.

### 2. Examining the Python Source Code
I began by opening the Python file in a text editor to analyze its structure and functionality. Unlike binary reverse engineering challenges, having access to the source code allowed me to directly read and understand the program's logic.

During my examination, I focused on identifying:
- The program's main execution flow
- Any password validation mechanisms
- Hardcoded passwords or keys within the code
- The conditions required to display the flag

### 3. Identifying the Password Validation Logic
Through careful analysis of the Python code, I discovered that the program contained password validation logic with a hardcoded password value. The code structure revealed:

- A prompt asking for user input (password)
- A comparison operation that checked the user's input against a predefined value
- A conditional statement that would display the flag if the correct password was provided

The password was clearly visible within the source code, eliminating the need for brute force attacks or complex reverse engineering techniques.

### 4. Extracting the Correct Password
By examining the validation logic in the source code, I was able to identify the exact password that the program expected. The password was stored as a string literal within the code, making it easily discoverable through simple code reading.

This discovery demonstrated a common security vulnerability where sensitive information (like passwords) is hardcoded directly into the source code, making it accessible to anyone who can read the program.

### 5. Executing the Program with the Correct Password
With the correct password identified from the source code analysis, I proceeded to run the Python script:

```bash
python patchme.py
```

When prompted for the password, I entered the value I had discovered in the source code. The program validated the input, confirmed it was correct, and immediately displayed the flag.

### 6. Verification and Solution
The program successfully accepted the hardcoded password and revealed the flag, confirming that my source code analysis was accurate. The straightforward nature of this challenge demonstrated how security through obscurity fails when source code is available for inspection.

### 7. Learning Outcomes
This challenge effectively demonstrated several important security concepts:
- The dangers of hardcoding sensitive information in source code
- How source code analysis can reveal security vulnerabilities
- The importance of proper secret management in software development
- Basic techniques for analyzing Python scripts for security flaws

The simplicity of this challenge made it an excellent introduction to source code analysis and highlighted why proper security practices are essential in software development.

## Flag:
```picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}```
