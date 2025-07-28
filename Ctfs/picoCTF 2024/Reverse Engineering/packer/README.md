# Writeup for picoCTF 2023 : packer

## Tools:
- upx (Ultimate Packer for eXecutables)
- IDA Pro (Interactive Disassembler)
- dencode.com (Online encoding/decoding service)

## Steps:

### 1. Initial Analysis and Following the Hints
When I first examined this challenge, I started by carefully reading the hint provided by picoCTF, which suggested that the binary might have been compressed using some form of packing algorithm. This was my first clue that I wasn't dealing with a standard executable file.

Initially, I struggled to identify which specific compression or packing method had been used on the binary. I tried various approaches to determine the packer type, but without success. At this point, I decided to research existing writeups for similar challenges to understand common packing techniques used in CTF competitions. Through this research, I discovered that UPX (Ultimate Packer for eXecutables) is a frequently used tool for binary packing challenges.

### 2. Learning UPX and Unpacking the Binary
After identifying UPX as the likely packing method, I proceeded to install it in my tools directory. Since I hadn't used UPX before, I spent some time familiarizing myself with its command-line parameters and functionality. 

The learning curve involved understanding how UPX compression works and, more importantly for this challenge, how to reverse the process. After experimenting with various command options and reading the documentation, I successfully decompressed the packed binary using the following command:

```bash
upx -d out -o ori
```

This command decompressed the original packed file (`out`) and saved the unpacked version as `ori`, restoring it to its original, uncompressed state.

### 3. Static Analysis with IDA Pro
With the unpacked binary in hand, I loaded it into IDA Pro for static analysis. My strategy was to search for any obvious string references that might contain or lead to the flag. I performed a string search for "flag" within the disassembled code.

This approach proved successful - I located a section of the binary that contained what appeared to be flag-related data:

![Flag in IdaPro](workfolder/idaproflag.png)

### 4. Decoding the Flag
The string I found in IDA Pro didn't immediately look like a readable flag format. Upon closer examination, it appeared to be encoded in hexadecimal format. To decode this, I used dencode.com, an online encoding/decoding service that can automatically detect and convert various encoding schemes.

When I input the hex string into dencode.com, it automatically recognized the encoding type and provided the decoded result, revealing the final flag:

## Flag:

```
picoCTF{U9X_UnP4ck1N6_B1n4Ri3S_6ff964ef}
```
