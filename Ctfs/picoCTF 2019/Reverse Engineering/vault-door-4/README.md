# Writeup for picoCTF 2019 : vault-door-4

## Tools:
- Java source code analysis
- Text editor for code examination
- Java compiler (javac)
- Byte array to string conversion

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Java source file that appeared to implement the fourth iteration of the vault door series. The challenge title "vault-door-4" suggested that this would build upon the concepts from the previous vault door challenges, likely with increased complexity in the password validation mechanism.

Unlike binary reverse engineering challenges, having access to the Java source code allowed me to directly examine the validation logic and understand exactly what password the program was expecting.

### 2. Examining the Java Source Code Structure
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My analysis revealed that the program contained a `checkPassword` function that implemented validation logic different from the previous vault door challenges.

The code structure showed:
- A byte array named `myBytes` containing hardcoded values
- A validation mechanism that compared user input against these byte values
- More complex data handling compared to previous iterations

### 3. Understanding the Byte Array Approach
Upon examining the `checkPassword` function, I found that it contained a predefined byte array called `myBytes`. This array appeared to store the expected password in byte format rather than as a direct string comparison like in previous challenges.

The key insight was recognizing that:
- The password was stored as a sequence of byte values
- These byte values represented ASCII characters of the actual password
- I needed to convert these bytes back to their character equivalents to reveal the flag

### 4. Analyzing the Validation Logic
The original validation logic was designed to compare user input against the byte array values. However, rather than trying to reverse-engineer the exact validation process, I realized that I could directly extract the password by converting the byte array to its string representation.

### 5. Developing the Extraction Strategy
My approach was to modify the `checkPassword` function to extract and display the password directly from the `myBytes` array. This strategy involved:

- Replacing the existing validation logic with a conversion loop
- Iterating through each byte in the array
- Converting each byte to its corresponding character
- Building the complete password string

### 6. Implementing the Byte-to-String Conversion
I modified the Java code to include a conversion mechanism that would reveal the password:

```java
// ...existing code...
StringBuilder result = new StringBuilder();
for (byte b : myBytes) {
    result.append((char) b);
}

String myString = result.toString();
System.out.println(myString);
```

This code works by:
- Creating a StringBuilder to efficiently build the result string
- Iterating through each byte in the `myBytes` array
- Casting each byte to a char to get its ASCII character representation
- Appending each character to build the complete string
- Printing the final result

### 7. Executing the Modified Code
After implementing the conversion logic, I compiled and executed the modified Java program. The program successfully processed the byte array and displayed the password that was encoded within it.

### 8. Flag Discovery and Verification
When I executed the modified program, it revealed the complete password string that corresponded to the flag. The output followed the expected picoCTF flag format, confirming that my byte-to-string conversion approach was correct.

### 9. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **Byte array analysis**: Understanding how data can be stored in byte format within programs
- **ASCII conversion**: Converting byte values to their character representations
- **Code modification techniques**: Modifying existing validation logic to extract hidden information
- **Data encoding patterns**: Recognizing how sensitive information can be encoded in different formats

The challenge showed how flags can be hidden in various data formats and reinforced the importance of understanding different data representation methods in reverse engineering.

## Flag:
```picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}```
