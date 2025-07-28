# Writeup for picoCTF 2022 : unpackme.py

## Tools:
- Python interpreter
- Text editor
- Code analysis techniques
- Dynamic execution interception

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Python file named `unpackme.py`, which immediately suggested that I was dealing with some form of packed or obfuscated Python code that needed to be "unpacked" or decoded to reveal its true contents.

The filename itself provided a strong hint about the nature of the challenge - it indicated that the Python file contained encrypted or encoded data that would be decrypted and executed at runtime, requiring me to intercept this process to extract the hidden information.

### 2. Examining the Python File Structure
When I opened the Python file in a text editor, I was able to examine its structure and understand the general approach being used. The code analysis revealed several key components:

- **Encrypted payload**: The file contained what appeared to be encrypted or encoded data
- **Decryption logic**: There was code responsible for decrypting the payload
- **Execution mechanism**: The decrypted payload was designed to be executed after decryption

This structure is common in malware and obfuscated scripts where the actual functionality is hidden through encryption and only revealed at runtime.

### 3. Understanding the Encryption-Execution Flow
Through careful analysis of the Python code, I identified the program's execution flow:

1. **Payload Storage**: The encrypted payload was stored as a variable or data structure within the file
2. **Decryption Process**: A decryption function or algorithm was used to convert the encrypted data back to executable Python code
3. **Dynamic Execution**: The decrypted code was executed using Python's dynamic execution capabilities (likely `exec()` or `eval()`)

The critical insight was that the decryption happens just before execution, creating a brief moment where the decrypted payload exists in memory in its readable form.

### 4. Developing the Interception Strategy
My approach was to modify the execution flow to intercept and display the decrypted payload before it gets executed. This strategy involved:

- **Locating the execution point**: Finding where in the code the decrypted payload gets executed
- **Intercepting the payload**: Capturing the decrypted content before execution
- **Printing the content**: Displaying the decrypted payload to examine its contents

This approach allows me to see exactly what code would be executed without actually running potentially malicious or complex code.

### 5. Implementing the Payload Extraction
I modified the Python file to print the decrypted payload instead of (or in addition to) executing it. This typically involved:

- Finding the variable that contains the decrypted payload
- Adding a `print()` statement to display its contents
- Commenting out or modifying the execution command

The exact implementation depended on the specific structure of the code, but the general principle was to reveal the hidden content that would normally only exist temporarily during execution.

### 6. Executing the Modified Script
When I ran the modified Python script, it successfully decrypted the payload and displayed its contents instead of executing it. This revealed the actual Python code that was hidden within the encrypted payload.

### 7. Flag Discovery and Extraction
The decrypted payload contained the flag information, which was now visible in readable format. The flag appeared as part of the decrypted Python code, likely as a string variable or print statement that would have been executed if the original program had run normally.

### 8. Verification and Solution
Once I extracted the flag from the decrypted payload, I verified that it followed the expected picoCTF format and contained reasonable content. The successful decryption and flag extraction confirmed that my interception approach was effective.

### 9. Learning Outcomes
This challenge effectively demonstrated:
- How Python code can be obfuscated through encryption and dynamic execution
- The importance of understanding program execution flow in reverse engineering
- Techniques for intercepting and analyzing dynamically generated code
- The value of modifying execution paths to reveal hidden information

The challenge provided practical experience with a common obfuscation technique used in both legitimate software protection and malicious code hiding.

## Flag:
```picoCTF{175_chr157m45_cd82f94c}```
