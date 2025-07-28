# Writeup for picoCTF 2023 : timer

## Tools:
- Terminal/Command line
- File archiver (for ZIP manipulation)
- String search utilities (grep)
- APK analysis techniques

## Steps:

### 1. Initial Challenge Analysis
This challenge provided me with a `timer.apk` file, which immediately indicated that I was dealing with an Android application package. APK files are essentially ZIP archives containing the compiled code, resources, and metadata for Android applications.

The challenge required me to perform reverse engineering on this Android application to extract the hidden flag, suggesting that the flag was embedded somewhere within the application's structure or code.

### 2. Understanding APK File Structure
Before diving into the analysis, I needed to understand that APK files are fundamentally ZIP archives with a specific structure. This means they can be manipulated using standard archive tools, allowing access to the internal components without requiring specialized Android reverse engineering tools.

Key components of an APK typically include:
- `.dex` files (Dalvik Executable files containing compiled Java code)
- Resource files
- Manifest files
- Native libraries
- Asset files

### 3. Converting APK to ZIP Format
My first step was to convert the APK file to a standard ZIP format to enable easy extraction and analysis. This conversion is straightforward since APK files are already ZIP archives:

```bash
mv timer.apk timer.zip
```

This simple rename operation allowed me to treat the file as a standard ZIP archive, making it accessible to common archive manipulation tools.

### 4. Extracting the APK Contents
Once I had the file in ZIP format, I proceeded to extract all its contents to examine the internal structure:

```bash
unzip timer.zip
```

This extraction revealed the complete directory structure of the Android application, including all the compiled code files, resources, and metadata that make up the application.

### 5. Identifying Target Files for Analysis
After extraction, I examined the directory structure to identify the most promising files for flag discovery. The `.dex` files were particularly interesting because:

- They contain the compiled application logic
- String literals and constants are often stored within these files
- Flags in CTF challenges are frequently embedded as string constants

### 6. Performing String Search Analysis
With the `.dex` files identified as the primary targets, I performed a comprehensive string search to locate any occurrences of the flag format. I used the search term "pico" since picoCTF flags typically begin with "picoCTF{":

```bash
grep -r "pico" *.dex
```

This search strategy was effective because:
- It targeted the most likely location for embedded strings
- The search term "pico" would match the beginning of any picoCTF flag
- The recursive search ensured coverage of all relevant files

### 7. Flag Discovery and Extraction
The string search successfully located the flag within one of the `.dex` files. The flag was embedded as a string constant within the compiled application code, indicating that it was likely part of the application's logic or data.

### 8. Verification and Solution
Once I found the flag string, I verified that it followed the expected picoCTF format and contained reasonable content. The flag structure and content confirmed that this was indeed the correct solution.

This challenge effectively demonstrated:
- The relationship between APK files and ZIP archives
- Basic Android application reverse engineering techniques
- The importance of string analysis in reverse engineering
- How flags can be embedded within compiled application code

The straightforward nature of this challenge made it an excellent introduction to mobile application reverse engineering concepts.

## Flag:
```picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}```


