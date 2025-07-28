# Writeup for picoCTF 2019 : vault-door-6

## Tools:
- Java source code analysis
- Text editor for code examination
- Java compiler (javac)
- XOR cipher understanding

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Java source file that appeared to implement the sixth iteration of the vault door series. The challenge title "vault-door-6" suggested that this would build upon the concepts from the previous vault door challenges, likely introducing more sophisticated cryptographic operations.

Unlike simple character mapping or string manipulation seen in earlier challenges, this one required understanding bitwise operations and reversible cryptographic functions.

### 2. Examining the Java Source Code Structure
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My analysis revealed that the program contained a `checkPassword` function that implemented a more complex validation mechanism than previous challenges.

The code structure showed:
- A byte array named `myBytes` containing hardcoded encrypted values
- A validation process involving XOR operations and byte manipulation
- Mathematical operations that needed to be understood and reversed

### 3. Understanding the XOR-Based Validation Logic
Upon examining the `checkPassword` function, I discovered that it implemented a XOR-based cipher for password validation. The validation process worked as follows:

1. **Input Processing**: The user's password was converted to a byte array (`passBytes`)
2. **XOR Operation**: Each byte of the password was XORed with the constant `0x55`
3. **Comparison Logic**: The XORed result was compared against corresponding bytes in `myBytes`
4. **Validation Check**: If any comparison failed (non-zero result), the password was rejected

The critical insight was recognizing that this was implementing the equation:
```
(passBytes[i] ^ 0x55) - myBytes[i] == 0
```

### 4. Analyzing the Reversible Nature of XOR
The key to solving this challenge was understanding that XOR operations are mathematically reversible. The fundamental property of XOR that makes this possible is:

**XOR Reversibility**: If `A ^ B = C`, then `C ^ B = A`

Applied to this challenge:
- If `passBytes[i] ^ 0x55 = myBytes[i]`
- Then `myBytes[i] ^ 0x55 = passBytes[i]`

This meant I could recover the original password by XORing each byte in `myBytes` with `0x55`.

### 5. Developing the Decryption Strategy
My approach was to create a Java program that would reverse the encryption process by:

1. **Iterating through myBytes**: Process each encrypted byte in the array
2. **Applying reverse XOR**: XOR each byte with `0x55` to decrypt it  
3. **Character conversion**: Convert the decrypted bytes back to ASCII characters
4. **Flag reconstruction**: Combine all characters to form the complete password

### 6. Implementing the Decryption Code
I wrote Java code to implement the reverse operation:

```java
char[] passChars = new char[myBytes.length];

for (int i = 0; i < myBytes.length; i++) {
    passChars[i] = (char) (myBytes[i] ^ 0x55);
}

String flag = new String(passChars);
System.out.println("The password is: " + flag);
```

This code systematically:
- Creates a character array to store the decrypted result
- Loops through each byte in the encrypted `myBytes` array
- Applies the reverse XOR operation with `0x55`
- Converts each decrypted byte to its corresponding ASCII character
- Constructs the final password string

### 7. Testing the Decryption
To verify the decryption worked correctly, I modified the original program to include my decryption code and ran it. The program successfully decrypted the password and displayed it:

```
java VaultDoor6
Enter vault password: 12341234123412341234123412341234
The password is: n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919
Access granted.
```

Note that while I entered a dummy 32-character password to satisfy the program's input requirements, the actual decryption revealed the true password.

### 8. Learning Outcomes
This challenge effectively demonstrated several important cryptographic and reverse engineering concepts:

- **XOR cipher fundamentals**: Understanding how XOR operations work in cryptographic contexts
- **Reversible operations**: Recognizing mathematical operations that can be undone
- **Bitwise manipulation**: Working with individual bytes and bitwise operations in programming
- **Static analysis techniques**: Extracting encrypted data from source code for analysis

The challenge provided practical experience with one of the most fundamental concepts in cryptography - the reversible nature of XOR operations and how they can be exploited when the key is known.

## Flag:
```picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_3ce2919}```
