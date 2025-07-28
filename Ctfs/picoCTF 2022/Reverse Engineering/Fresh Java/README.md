# Writeup for picoCTF 2022 : Fresh Java

## Tools:
- Java decompiler (JD-GUI, Fernflower, or similar)
- Java class file analysis
- Source code examination

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with Java class files that needed to be analyzed to extract the hidden flag. The title "Fresh Java" suggested that I was dealing with recently compiled Java bytecode that required decompilation to understand its functionality.

Unlike challenges that provide source code directly, this one required me to reverse engineer compiled Java bytecode back into readable source code to locate the flag information.

### 2. Understanding Java Class Files
Before beginning the analysis, I recognized that Java class files contain compiled bytecode that can be decompiled back into readable Java source code. This process is generally more straightforward than reverse engineering native binaries because:

- Java bytecode retains much of the original program structure
- Variable names and method signatures are often preserved
- String literals and constants remain easily accessible
- Decompilation tools can produce highly readable output

### 3. Selecting the Appropriate Decompilation Tool
For this challenge, I chose to use a Java decompiler to convert the compiled class files back into readable source code. Popular Java decompilers include:

- **JD-GUI**: A standalone graphical decompiler with an intuitive interface
- **Fernflower**: A powerful analytical decompiler with excellent output quality
- **CFR**: A modern decompiler with good handling of recent Java features
- **Procyon**: Another reliable option for Java decompilation

The choice of decompiler can affect the readability of the output, but most modern tools produce sufficiently clear results for CTF analysis.

### 4. Decompiling the Java Classes
I loaded the provided Java class files into the decompiler, which automatically processed the bytecode and generated readable Java source code. The decompilation process revealed:

- The overall program structure and class hierarchy
- Method implementations and logic flow
- String constants and variable declarations
- Any hardcoded values or flag-related data

### 5. Analyzing the Decompiled Source Code
Once I had the decompiled source code, I systematically examined it to locate flag-related information. My analysis focused on:

- **String literals**: Looking for any hardcoded strings that might contain the flag
- **Method logic**: Understanding how the program processes data
- **Variable assignments**: Identifying where flag data might be stored
- **Output statements**: Finding where the flag would be displayed or used

### 6. Flag Discovery and Extraction
Through careful examination of the decompiled source code, I successfully located the flag embedded within the program. The flag was likely stored as a string constant or constructed through string operations within the Java code.

The decompilation process made it straightforward to identify and extract the flag without needing to understand complex program logic or execution flow.

### 7. Verification and Solution
Once I found the flag in the decompiled source code, I verified that it followed the expected picoCTF format and contained reasonable content. The successful decompilation and flag extraction confirmed that the straightforward approach of using Java decompilation tools was effective for this challenge.

### 8. Learning Outcomes
This challenge effectively demonstrated:
- The accessibility of Java bytecode through decompilation
- How compiled Java programs can be easily reverse engineered
- The importance of code obfuscation in protecting sensitive information
- Basic techniques for analyzing Java applications in CTF contexts

The straightforward nature of this challenge made it an excellent introduction to Java reverse engineering and highlighted why additional protection measures are often necessary when deploying Java applications.

## Flag:
```picoCTF{700l1ng_r3qu1r3d_9332a6be}```
