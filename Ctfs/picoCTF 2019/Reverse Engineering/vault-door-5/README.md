# Writeup for picoCTF 2019 : vault-door-5

## Tools:
- Java source code analysis
- Text editor for code examination
- Java compiler (javac)
- Custom decoder implementation

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a Java source file that appeared to implement the fifth iteration of the vault door series. The challenge title "vault-door-5" suggested that this would build upon the concepts from the previous vault door challenges, likely with increased complexity in the password validation and encoding mechanisms.

The challenge required me to understand multiple layers of encoding that had been applied to the flag data and develop appropriate decoders to reverse the process.

### 2. Examining the Java Source Code Structure
I began by carefully reading through the provided Java source code to understand the program's structure and functionality. My analysis revealed that the program contained a `checkPassword` function that implemented a more sophisticated validation system compared to the previous vault door challenges.

The code structure showed:
- Multiple encoding methods implemented within the same program
- A complex validation process involving layered encoding schemes
- Custom implementations of both URL encoding and Base64 encoding algorithms

### 3. Understanding the Multi-Layer Encoding System
Upon examining the `checkPassword` function, I discovered that the expected password string had been processed through multiple encoding layers. The analysis revealed that the flag data had been subjected to:

- **URL encoding**: A custom implementation that converted certain characters to their percent-encoded equivalents
- **Base64 encoding**: Another custom implementation that encoded the data using Base64 algorithm
- **Layered application**: These encodings were applied in a specific sequence that needed to be reversed

### 4. Analyzing the Custom Encoding Implementations
The challenge included custom implementations of both encoding methods rather than using standard library functions. This meant that I needed to:

- Understand the specific logic of each custom encoder
- Identify any variations from standard encoding implementations
- Determine the exact sequence in which the encodings were applied
- Develop corresponding decoder functions that could reverse each encoding step

### 5. Identifying the Encoding Sequence
Through careful analysis of the `checkPassword` function, I determined that the `expected` string had been encoded using both the custom URL encoder and Base64 encoder. The key insight was understanding the order in which these encodings were applied, as this would determine the reverse order needed for decoding.

### 6. Developing Custom Decoders
To reverse the encoding process, I needed to implement custom decoder functions that could undo each encoding step:

**URL Decoder**: Created a function that could reverse the custom URL encoding by:
- Converting percent-encoded characters back to their original form
- Handling any special cases or variations in the custom implementation

**Base64 Decoder**: Implemented a decoder that could reverse the custom Base64 encoding by:
- Converting Base64 encoded strings back to their original byte representation
- Properly handling padding and character set variations

### 7. Implementing the Reverse Decoding Process
With both decoders implemented, I applied them to the `expected` string in reverse order of the original encoding process. This systematic approach ensured that each encoding layer was properly reversed:

1. First, reverse the last encoding that was applied
2. Then, reverse the previous encoding layer
3. Continue until all encoding layers had been reversed

### 8. Flag Discovery and Verification
When I executed the complete reverse decoding process on the `expected` string, it successfully revealed the original flag data. The systematic reversal of the encoding layers produced a string that followed the expected picoCTF flag format, confirming that my analysis and implementation were correct.

### 9. Learning Outcomes
This challenge effectively demonstrated several important concepts:
- **Multi-layer encoding analysis**: Understanding how multiple encoding schemes can be combined
- **Custom implementation analysis**: Recognizing variations in standard encoding algorithms
- **Reverse engineering methodology**: Developing systematic approaches to undo complex transformations
- **Decoder implementation**: Creating custom functions to reverse proprietary encoding schemes

The challenge showed how encoding complexity can increase significantly when multiple layers are applied, and reinforced the importance of understanding the exact sequence and implementation details of each encoding step.

## Flag:
```picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095}```
