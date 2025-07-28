# Writeup for picoCTF 2019 : vault-door-training

## Tools:
- Text editor
- Java source code examination
- Direct flag extraction

## Steps:

### 1. Initial Challenge Analysis
This challenge served as an introductory exercise in the "vault-door" series, designed to familiarize participants with the basic concept of examining source code for flags. The challenge title "vault-door-training" immediately indicated that this was a warm-up or training exercise, suggesting a straightforward approach to flag discovery.

Unlike more complex reverse engineering challenges that require decompilation or binary analysis, this training challenge provided direct access to Java source code, making it an ideal starting point for beginners.

### 2. Understanding the Training Objective
The primary purpose of this challenge was to teach participants the fundamental skill of source code examination. By providing a simple scenario where the flag is directly visible in the source code, the challenge established the baseline technique of:

- Opening source files in text editors
- Searching for flag-formatted strings
- Recognizing the standard picoCTF flag format
- Understanding that not all reverse engineering requires complex tools

### 3. Java File Examination
I opened the provided Java file in a text editor to examine its contents. Since this was designed as a training exercise, the challenge makers intentionally made the flag easily discoverable through direct inspection.

The source code examination revealed that the flag was stored as a plain text string within the Java code, requiring no decoding, decryption, or complex analysis to retrieve.

### 4. Direct Flag Discovery
Upon opening the Java file, the flag was immediately visible in the source code. This straightforward placement demonstrated several important concepts:

- **Source code accessibility**: How sensitive information can be exposed when source code is available
- **String literal storage**: How flags are often embedded as string constants in programs
- **Basic reconnaissance**: The importance of examining all available resources before attempting complex analysis techniques

### 5. Verification and Learning Outcomes
The flag followed the standard picoCTF format, confirming its authenticity. This training challenge effectively served multiple educational purposes:

- **Tool familiarity**: Introducing participants to basic text editor usage for code examination
- **Pattern recognition**: Teaching participants to recognize the picoCTF flag format
- **Methodology establishment**: Demonstrating that simple approaches should be tried first
- **Confidence building**: Providing an easy success to encourage continued participation

The simplicity of this challenge was intentional, designed to build foundational skills that would be essential for more complex challenges in the vault-door series.

### 6. Series Preparation
This training exercise effectively prepared participants for the subsequent vault-door challenges by:
- Establishing familiarity with Java source code structure
- Demonstrating the basic workflow of opening and examining files
- Building confidence in source code analysis techniques
- Setting expectations for the types of information that might be hidden in code

The challenge served as an excellent entry point into the world of reverse engineering and source code analysis.

## Flag:
```picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}```
