# Writeup for picoCTF 2019 : reverse_cipher

## Tools:
- Ghidra (NSA reverse engineering framework)
- Python (for decoding script)
- Binary analysis techniques
- Cipher algorithm understanding

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a binary that appeared to implement some form of cipher or encoding algorithm. The challenge title "reverse_cipher" immediately suggested that I would need to understand how the cipher works and then reverse its operations to recover the original flag.

The challenge required me to perform reverse engineering on the binary to understand the encoding algorithm and then implement a decoding process to retrieve the flag.

### 2. Binary Analysis with Ghidra
I loaded the binary into Ghidra to perform comprehensive static analysis and understand the program's functionality. Ghidra's decompilation capabilities allowed me to examine the program's logic in a more readable format than raw assembly code.

Through careful analysis of the decompiled code, I was able to understand the complete algorithm that the program uses to process the flag data.

### 3. Understanding the Program's File Operations
The decompiled code revealed that the program performs the following file operations:
- Opens and reads from a file named `flag.txt` containing the original flag
- Creates and writes to an output file named `rev_this` containing the encoded result
- Processes exactly 24 bytes of data from the input file

This information was crucial for understanding the data flow and the scope of the encoding operation.

### 4. Analyzing the Encoding Algorithm
Through detailed analysis of the decompiled main function, I discovered that the program implements a position-based encoding scheme that treats different byte positions differently:

**Algorithm Structure:**
- **First 8 bytes (positions 0-7)**: Written directly without modification
- **Middle 15 bytes (positions 8-22)**: Modified based on position parity
- **Last byte (position 23)**: Written directly without modification

**Position-Based Modifications:**
- **Even indices** (relative to position 8): Add 5 to the ASCII value
- **Odd indices** (relative to position 8): Subtract 2 from the ASCII value

### 5. Reconstructing the Complete Algorithm
Based on my analysis, I was able to reconstruct the complete encoding process as implemented in the original program:

## Reversed `main` function:
```c
#include <stdio.h>
#include <stdlib.h>

void main(void) {
    size_t bytesRead;
    char flagBuffer[24];  // Buffer to store the content of flag.txt
    char tempChar;
    int byteIndex;
    FILE *flagFile;
    FILE *outputFile;
    unsigned int modifiedIndex;
    int status;
    
    // Open "flag.txt" for reading
    flagFile = fopen("flag.txt", "r");
    
    // Open "rev_this" for appending
    outputFile = fopen("rev_this", "a");
    
    // Check if "flag.txt" was opened successfully
    if (flagFile == NULL) {
        puts("No flag found, please make sure this is run on the server");
    }
    
    // Check if "rev_this" was opened successfully
    if (outputFile == NULL) {
        puts("Please run this on the server");
    }
    
    // Read up to 24 bytes from the flag file into flagBuffer
    bytesRead = fread(flagBuffer, 24, 1, flagFile);
    
    // Cast the bytesRead to an integer for further processing
    status = (int)bytesRead;
    
    // If nothing was read, exit the program
    if (status < 1) {
        exit(0);
    }
    
    // Write the first 8 bytes directly to the output file
    for (byteIndex = 0; byteIndex < 8; byteIndex++) {
        tempChar = flagBuffer[byteIndex];
        fputc((int)tempChar, outputFile);
    }
    
    // Process and write the next 15 bytes with specific modifications
    for (modifiedIndex = 8; (int)modifiedIndex < 23; modifiedIndex++) {
        if ((modifiedIndex & 1) == 0) {  // Even index
            tempChar = flagBuffer[(int)modifiedIndex] + 5;
        } else {  // Odd index
            tempChar = flagBuffer[(int)modifiedIndex] - 2;
        }
        fputc((int)tempChar, outputFile);
    }
    
    // Write the final character (local_41) to the output file
    tempChar = flagBuffer[23];
    fputc((int)tempChar, outputFile);
    
    // Close the files
    fclose(outputFile);
    fclose(flagFile);
    
    return;
}
```

The decompiled code showed the exact logic flow, including file handling, buffer management, and the specific arithmetic operations applied to each byte position.

### 6. Developing the Decoding Strategy
With a complete understanding of the encoding algorithm, I developed a reverse decoding strategy:

**Decoding Logic:**
1. **First 8 bytes**: Copy directly (no modification needed)
2. **Middle 15 bytes**: Apply inverse operations based on position
   - Even indices: Subtract 5 (reverse of adding 5)
   - Odd indices: Add 2 (reverse of subtracting 2)
3. **Last byte**: Copy directly (no modification needed)

### 7. Implementing the Python Decoding Script
I created a Python script that implements the inverse operations to recover the original flag from the encoded data:

## The Python script used to decode the flag:
```python
def decode(encoded_data):
    decoded_data = []

    # First 8 bytes are directly copied
    for i in range(8):
        decoded_data.append(encoded_data[i])

    # Next 15 bytes need to be processed with inverse operations
    for i in range(8, 23):
        if (i & 1) == 0:  # Even index relative to 8th byte
            decoded_data.append(chr(ord(encoded_data[i]) - 5))
        else:  # Odd index relative to 8th byte
            decoded_data.append(chr(ord(encoded_data[i]) + 2))

    # Last byte is directly copied
    decoded_data.append(encoded_data[23])

    return ''.join(decoded_data)

# Example usage:
# Assume `encoded_data` is the string read from the output file "rev_this"
decoded_flag = decode(encoded_data)
print(decoded_flag)
```

### 8. Verification and Solution
When I executed the decoding script with the encoded data from the `rev_this` file, it successfully reversed all the encoding operations and revealed the original flag. The recovered flag followed the expected picoCTF format, confirming that my analysis and implementation were correct.

### 9. Learning Outcomes
This challenge effectively demonstrated several important reverse engineering concepts:
- **Algorithm reconstruction**: Understanding complex encoding schemes through static analysis
- **Position-based ciphers**: Recognizing patterns in how different data positions are processed
- **Inverse operation design**: Developing decoding algorithms that reverse encoding processes
- **File-based data processing**: Understanding how programs manipulate data between files

The challenge provided practical experience with cipher analysis and highlighted the importance of systematic reverse engineering approaches for understanding complex algorithms.

## Flag:
```picoCTF{r3v3rs312528e05}```
