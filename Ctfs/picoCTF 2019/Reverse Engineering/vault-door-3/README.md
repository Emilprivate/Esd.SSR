# Writeup for picoCTF 2019 : vault-door-3

## Tools:
- Java source code analysis
- Text editor for code examination
- Java compiler (javac)
- Java runtime environment
- String manipulation understanding

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Java source file that appeared to implement the third iteration of the vault door series. The challenge title "vault-door-3" suggested that this would build upon the concepts from the previous vault door challenges, likely with increased complexity in the password validation mechanism.

Unlike binary reverse engineering challenges, having access to the Java source code allowed me to directly examine the validation logic and understand exactly what password the program was expecting.

### 2. Examining the Java Source Code Structure
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My analysis revealed that the program contained a `checkPassword` function that implemented more sophisticated validation logic compared to the previous vault door challenges.

The code structure showed:
- A more complex `checkPassword` function with string manipulation operations
- Input processing that extracted content between `picoCTF{` and `}`
- String transformation algorithms that modified the input before validation

### 3. Understanding the Input Processing Flow
Through examination of the main function, I discovered how the program processed user input:

```java
String input = userInput.substring("picoCTF{".length(), userInput.length()-1);
```

This line revealed that:
- The program expected input in the standard picoCTF flag format
- It extracted only the content between the curly braces for processing
- The extracted content would then be passed to the validation function

### 4. Analyzing the Password Validation Logic
Upon examining the `checkPassword` function, I found that it contained string manipulation algorithms that transformed the input before comparing it against expected values. Rather than attempting to reverse-engineer the complete transformation logic, I decided to take a more direct approach by observing the program's behavior.

### 5. Implementing a Debug Strategy
To understand what the program was doing with the input, I modified the source code to reveal intermediate processing steps. I added a debug print statement to display the transformed string:

```java
System.out.println(s);
```

This modification would allow me to see exactly how the program was transforming the input string during the validation process.

### 6. Compiling and Testing the Program
With the debug modification in place, I compiled the Java program:

```bash
javac VaultDoor3.java
```

Then executed it to test the behavior:

```bash
java VaultDoor3
```

### 7. Discovering the String Transformation
When I provided the test input `picoCTF{jU5t_a_sna_3lpm12g94c_u_4_m7ra41}`, the program's debug output revealed the transformation result:

```
❯ java VaultDoor3
Enter vault password: picoCTF{jU5t_a_sna_3lpm12g94c_u_4_m7ra41}
jU5t_a_s1mpl3_an4gr4m_4_u_c79a21
Access denied!
```

This output showed that the program was performing some form of character rearrangement or anagram operation on the input string.

### 8. Understanding the Anagram Logic
The debug output revealed that the program was implementing an anagram algorithm that rearranged the characters of the input string. The transformation from `jU5t_a_sna_3lpm12g94c_u_4_m7ra41` to `jU5t_a_s1mpl3_an4gr4m_4_u_c79a21` showed a systematic rearrangement of characters.

The transformed result `jU5t_a_s1mpl3_an4gr4m_4_u_c79a21` appeared to be the actual flag content that the program was expecting to validate against.

### 9. Verification and Solution
The debug output provided the correctly formatted flag content. By examining the transformation, I could see that the program was essentially solving an anagram puzzle, rearranging the characters of the input to produce the expected flag format.

The final flag was constructed by wrapping the transformed result in the standard picoCTF format.

### 10. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **String manipulation algorithms**: Understanding how programs can rearrange character data
- **Anagram solving techniques**: Recognizing patterns in character rearrangement
- **Debug-driven analysis**: Using program output to understand internal processing
- **Iterative problem solving**: Building upon previous vault door challenge concepts

The challenge showed how adding simple debug statements can reveal complex internal processing that would be difficult to understand through static analysis alone.

## Flag:
```picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}```