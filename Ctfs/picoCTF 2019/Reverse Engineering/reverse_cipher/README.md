# Writeup for picoCTF 2019 : reverse_cipher
## Steps:
The program reads 24 bytes from a file named `flag.txt` and performs specific operations on these bytes before writing them to another file named `rev_this`.

   - **First 8 bytes**: These bytes are written directly to the output file without any modification.
   - **Next 15 bytes**: These bytes are modified based on their position:
     - For bytes at **even indices** (starting from the 8th byte), the program adds 5 to the ASCII value of the byte.
     - For bytes at **odd indices** (starting from the 8th byte), the program subtracts 2 from the ASCII value of the byte.
   - **Last byte**: The final byte is written directly to the output file without any modification.

   The C code for the `main` function, as reversed from the binary using Ghidra, is as follows:

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

To retrieve the original flag, a Python script was used to reverse the operations applied in the main function:

    - First 8 bytes: These are directly read from the encoded output.
    - Next 15 bytes:
        - For bytes at even indices: Subtract 5 from the ASCII value to revert to the original character.
        - For bytes at odd indices: Add 2 to the ASCII value to revert to the original character.
    - Last byte: This byte is directly read from the encoded output.

The Python script used to decode the flag is:

```python
def decode(encoded_data):
    decoded_data = []

    # First 8 bytes are directly copied
    for i in range(8):
        decoded_data.append(encoded_data[i])

    # Next 15 bytes need to be processed
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

```
## Flag:
``` picoCTF{r3v3rs312528e05} ```
