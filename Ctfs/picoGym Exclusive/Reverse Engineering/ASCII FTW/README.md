# Writeup for picoGym Exclusive : ASCII FTW

## Tools:
- Disassembler/Debugger (for binary analysis)
- Python (for hex-to-ASCII conversion)
- Hex value extraction

## Steps:

### 1. Initial Binary Analysis
When I first approached this challenge, the title "ASCII FTW" immediately suggested that the solution would involve converting some form of encoded data into ASCII characters. This gave me a strong indication that I needed to look for hexadecimal values or other encoded data within the binary that could be converted to readable ASCII text.

### 2. Examining the Main Function
I began by analyzing the binary using a disassembler to examine the program's structure. My focus was on the main function, as this is typically where the core logic and data would be located in simple reverse engineering challenges.

During my analysis of the main function, I discovered a series of hexadecimal values that appeared to be systematically arranged. The pattern and quantity of these hex values strongly suggested they were meant to be converted to ASCII characters to reveal the flag.

### 3. Extracting Hexadecimal Values
Through careful examination of the disassembled code, I identified and extracted the following sequence of hexadecimal values from the main function:

```
0x70, 0x69, 0x63, 0x6f, 0x43, 0x54, 0x46, 0x7b,
0x41, 0x53, 0x43, 0x49, 0x49, 0x5f, 0x49, 0x53,
0x5f, 0x45, 0x41, 0x53, 0x59, 0x5f, 0x33, 0x43,
0x46, 0x34, 0x42, 0x46, 0x41, 0x44, 0x7d
```

The arrangement and count of these values (31 hex values total) aligned perfectly with what I would expect for a picoCTF flag format.

### 4. Creating the Conversion Script
To efficiently convert these hexadecimal values to their corresponding ASCII characters, I developed a Python script. This approach was chosen because:
- Python provides built-in functions for hex-to-ASCII conversion
- It allows for easy verification and modification if needed
- The script can be reused for similar challenges

## Python script:
```python
corrected_hex_values = [
    0x70, 0x69, 0x63, 0x6f, 0x43, 0x54, 0x46, 0x7b,
    0x41, 0x53, 0x43, 0x49, 0x49, 0x5f, 0x49, 0x53,
    0x5f, 0x45, 0x41, 0x53, 0x59, 0x5f, 0x33, 0x43,
    0x46, 0x34, 0x42, 0x46, 0x41, 0x44, 0x7d
]

corrected_ascii_chars = ''.join(chr(value) for value in corrected_hex_values)
corrected_ascii_chars
```

### 5. Script Execution and Flag Recovery
When I executed the Python script, it successfully converted each hexadecimal value to its corresponding ASCII character using the `chr()` function. The `join()` method then concatenated all the individual characters into a single string, revealing the complete flag.

The conversion process worked flawlessly, and the resulting string followed the expected picoCTF flag format, confirming that my analysis and approach were correct.

This challenge served as an excellent introduction to basic reverse engineering concepts, particularly the common technique of storing flag data as hexadecimal values within binary executables.

## Flag:
```picoCTF{ASCII_IS_EASY_3CF4BFAD}```
