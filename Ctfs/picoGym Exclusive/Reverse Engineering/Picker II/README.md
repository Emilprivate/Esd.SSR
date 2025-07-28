# Writeup for picoGym Exclusive : Picker II

## Tools:
- Python code analysis
- Source code examination
- Direct file system access
- Alternative solution methodology

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the second installment in the "Picker" series, building upon the concepts introduced in Picker I. Like its predecessor, this challenge provided direct access to Python source code, allowing me to analyze the program's structure and functionality without the need for binary reverse engineering.

The challenge required me to understand the program's logic and find an efficient way to obtain the flag, potentially bypassing the intended execution flow.

### 2. Examining the Python Source Code
I began by thoroughly analyzing the provided Python source code to understand the program's structure and identify all available functions. During my examination, I focused on:

- The main program flow and user interaction mechanisms
- The presence and functionality of any "win" functions
- How the flag data was stored and processed
- Alternative methods to access the flag information

### 3. Understanding the Win Function Approach
Through my code analysis, I discovered that there was indeed a `win` function similar to the one in Picker I. However, upon closer examination of this function, I realized that it performed several unnecessary operations:

- The function contained additional processing steps
- It involved hexadecimal encoding/decoding operations
- The execution path included various validation and conversion routines

While this function would eventually provide the flag, it represented a more complex approach than necessary.

### 4. Identifying the Alternative Solution
During my analysis, I noticed that the challenge environment included a `flag.txt` file that contained the flag in plain text format. This discovery led me to realize that there was a much more direct approach to obtaining the flag than executing the intended win function.

The key insight was that I could bypass all the complex operations in the win function by directly accessing the flag file through Python's built-in file operations.

### 5. Implementing the Direct File Access Method
Instead of following the intended program flow through the win function with all its unnecessary processing, I developed a simple one-liner solution that directly reads the flag from the file system:

```python
print(open('flag.txt','r').read())
```

This elegant solution:
- Opens the `flag.txt` file in read mode
- Reads the entire contents of the file
- Prints the result directly to the console
- Bypasses all hexadecimal conversion and processing overhead

### 6. Advantages of the Alternative Approach
My chosen method offered several advantages over the traditional win function approach:

- **Simplicity**: No need to navigate through complex function calls
- **Efficiency**: Avoids unnecessary hexadecimal-to-ASCII conversions
- **Directness**: Provides immediate access to the flag data
- **Clarity**: The solution is straightforward and easy to understand

### 7. Verification and Solution
When I executed the direct file access command, it immediately displayed the flag in its proper format without any additional processing or conversion steps. This confirmed that the flag was stored in plain text within the `flag.txt` file and that my alternative approach was both valid and efficient.

This challenge effectively demonstrated the importance of thinking creatively about problem-solving approaches and showed that sometimes the most elegant solution involves bypassing the intended complexity in favor of a more direct method.

## Flag:
```picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}```
