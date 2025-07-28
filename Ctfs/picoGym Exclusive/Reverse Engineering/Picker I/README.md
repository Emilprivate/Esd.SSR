# Writeup for picoGym Exclusive : Picker I

## Tools:
- Python code analysis
- Source code examination
- Hexadecimal to ASCII conversion

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the first in the "Picker" series, which focuses on code analysis and understanding program functionality through source code examination. Unlike binary reverse engineering challenges that require disassemblers or debuggers, this challenge provided direct access to the Python source code.

The challenge required me to analyze the provided Python script to understand its structure and identify how to obtain the flag without necessarily executing the program through its normal flow.

### 2. Examining the Python Source Code
I began by carefully reading through the provided Python source code to understand the program's structure and functionality. The code analysis revealed the overall program logic and helped me identify the different functions available within the script.

During my examination, I focused on understanding:
- The main program flow and user interaction
- Available functions and their purposes
- Any functions that might contain flag-related information
- The format and encoding of any potential flag data

### 3. Identifying the Win Function
Through careful analysis of the Python code, I discovered a function named `win` that appeared to be the target function containing the flag information. This function was separate from the main program flow, suggesting it might not be easily accessible through normal program execution.

The `win` function stood out because:
- It was not part of the regular program flow
- Its name suggested it was a "winning" condition
- It contained data that appeared to be encoded flag information

### 4. Analyzing the Flag Data Format
Upon examining the `win` function, I found that it contained the flag data encoded in hexadecimal format. The function was designed to print out the flag, but the data was stored as hexadecimal values rather than readable ASCII text.

This discovery indicated that I needed to:
- Extract the hexadecimal values from the `win` function
- Convert these hexadecimal values to their ASCII equivalents
- Verify that the result followed the expected picoCTF flag format

### 5. Hexadecimal to ASCII Conversion
The critical step was converting the hexadecimal data found in the `win` function to readable ASCII characters. The hexadecimal values represented the individual bytes of the flag string encoded in hex format.

I performed the conversion by:
- Identifying each hexadecimal value in the function
- Converting each hex value to its corresponding ASCII character
- Concatenating the characters to form the complete flag string

### 6. Verification and Solution
After converting the hexadecimal data to ASCII, I obtained a string that followed the standard picoCTF flag format, confirming that my analysis and conversion were correct. The resulting flag contained the expected structure and appeared to be a valid solution.

This challenge effectively demonstrated the importance of thorough source code analysis and showed how flags can be hidden within functions that aren't part of the normal program execution flow. It also reinforced the common technique of storing flag data in encoded formats that require additional processing to reveal.

## Flag:
```picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}```

