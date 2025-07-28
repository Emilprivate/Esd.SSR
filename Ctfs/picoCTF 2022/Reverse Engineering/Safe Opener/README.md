# Writeup for picoCTF 2022 : Safe Opener

## Tools:
- Java source code analysis
- dencode.com (Base64 decoding service)
- Text editor for code examination

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Java application that appeared to be some form of safe-opening program. The challenge title "Safe Opener" suggested that I needed to find a way to "unlock" or "open" the safe, likely by discovering a hidden key or password within the program's code.

Unlike binary reverse engineering challenges, this one provided access to Java source code, making it more straightforward to analyze the program's logic and identify where sensitive information might be stored.

### 2. Examining the Java Source Code
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My analysis focused on:

- Understanding the overall program flow and logic
- Identifying any hardcoded values, keys, or passwords
- Looking for encoding or obfuscation techniques used to hide sensitive data
- Searching for any obvious flag-related content or validation mechanisms

### 3. Discovering the Encoded Key
During my examination of the Java source code, I identified a Base64 encoded string that appeared to be a key or password. The presence of Base64 encoding was evident from the characteristic format of the string, which contained:

- Alphanumeric characters
- Plus signs (+) and forward slashes (/)
- Potential padding with equal signs (=)
- A length that suggested it was encoded data rather than plain text

This encoded string was likely the key needed to "open the safe" and reveal the flag.

### 4. Understanding Base64 Encoding
Base64 encoding is a common method used to encode binary data into ASCII characters, making it safe for transmission and storage in text-based systems. In CTF challenges, Base64 is frequently used to:

- Obfuscate sensitive information like passwords or keys
- Encode flag data to make it less obvious
- Store binary data within source code or configuration files

Recognizing Base64 encoding was crucial for understanding how to decode the hidden information.

### 5. Decoding the Base64 String
To decode the Base64 encoded key, I used dencode.com, an online encoding/decoding service that supports multiple encoding formats. The decoding process involved:

1. **Copying the encoded string**: Extracting the Base64 string from the Java source code
2. **Selecting Base64 decoding**: Choosing the appropriate decoding method on dencode.com
3. **Processing the string**: Allowing the service to decode the Base64 data
4. **Analyzing the result**: Examining the decoded output for meaningful content

The decoding process successfully revealed the hidden key:
```
pl3as3_l3t_m3_1nt0_th3_saf3
```

### 6. Analyzing the Decoded Result
The decoded string appeared to be a password or key phrase written in "leet speak" (a form of text substitution where letters are replaced with numbers or symbols). The phrase "please let me into the safe" was clearly recognizable despite the character substitutions:

- "pl3as3" = "please"
- "l3t" = "let" 
- "m3" = "me"
- "1nt0" = "into"
- "th3" = "the"
- "saf3" = "safe"

This confirmed that I had found the correct key for the safe-opening challenge.

### 7. Flag Formation and Verification
While the decoded string provided the core content of the flag, I needed to format it according to the standard picoCTF flag format. The decoded result was the flag content without the typical "picoCTF{}" wrapper.

Following the standard picoCTF flag format, I constructed the final flag by wrapping the decoded content in the appropriate format structure.

### 8. Learning Outcomes
This challenge effectively demonstrated:
- The importance of examining source code thoroughly for hardcoded secrets
- How Base64 encoding is commonly used to obfuscate sensitive information
- The prevalence of "leet speak" in CTF challenge content
- Basic techniques for identifying and decoding common encoding schemes

The straightforward nature of this challenge made it an excellent introduction to source code analysis and basic encoding/decoding concepts in cybersecurity.

## Flag:
```picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}```
