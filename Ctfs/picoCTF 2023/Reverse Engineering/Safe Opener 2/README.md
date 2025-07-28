# Writeup for picoCTF 2023 : Safe Opener 2

## Tools:
- Terminal/Command line
- Vim text editor
- String search utilities
- Java bytecode analysis

## Steps:

### 1. Initial Challenge Analysis
This challenge presented me with a `.class` file, which immediately indicated that I was dealing with compiled Java bytecode. The `.class` file format contains the compiled version of Java source code, and while it's not human-readable in its binary form, it often contains string literals and other data that can be extracted through various analysis methods.

The challenge title "Safe Opener 2" suggested this was a sequel to a previous challenge, likely with a similar approach but potentially with some additional complexity or variation in the analysis required.

### 2. Understanding Java Class File Structure
Before diving into the analysis, I needed to understand that `.class` files are compiled Java bytecode that contain:
- Compiled method instructions
- String constants and literals
- Class metadata
- Field and method definitions
- Constant pool information

While these files are primarily binary, they often contain readable string data that can be extracted using text-based analysis tools, making them accessible for basic flag extraction in CTF contexts.

### 3. Choosing the Analysis Approach
For this challenge, I decided to use a straightforward text-based analysis approach rather than specialized Java decompilation tools. This method is effective because:
- String literals in Java bytecode are often stored in readable form
- Simple text editors can reveal embedded strings
- The approach is quick and doesn't require specialized tools
- It's sufficient for basic flag extraction scenarios

### 4. Opening the Class File for Analysis
I used Vim as my text editor to examine the contents of the `.class` file:

```bash
vim SafeOpener2.class
```

While opening a binary file in a text editor typically results in mostly unreadable content, Java `.class` files often contain embedded string literals that remain visible as plain text within the binary data.

### 5. Performing Targeted String Search
Instead of manually scrolling through the potentially large and mostly unreadable file content, I used Vim's built-in search functionality to look for the flag pattern. Since picoCTF flags always begin with "picoCTF{", I searched for the substring "pico" to quickly locate any flag-related content:

```
/pico
```

This search strategy was effective because:
- It targeted the most distinctive part of the flag format
- It avoided having to read through irrelevant bytecode content
- It provided immediate results if a flag was present in the file

### 6. Flag Discovery and Extraction
The search successfully located the flag string embedded within the Java bytecode. The flag appeared as a readable string literal within the compiled class file, indicating that it was likely stored as a constant or used in string operations within the original Java source code.

### 7. Verification and Solution
Once I found the flag string, I verified that it followed the expected picoCTF format and contained reasonable content. The flag structure confirmed that this was indeed the correct solution and that the simple text-based analysis approach was sufficient for this challenge.

### 8. Learning Outcomes
This challenge effectively demonstrated:
- The accessibility of string data within compiled Java bytecode
- The effectiveness of simple text-based analysis for basic reverse engineering tasks
- How flags can be embedded as string constants in compiled code
- The utility of targeted search strategies over manual file examination

The straightforward nature of this challenge made it an excellent introduction to Java bytecode analysis and reinforced that sometimes the simplest approaches are the most effective for CTF challenges.

## Flag:
```picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}```
