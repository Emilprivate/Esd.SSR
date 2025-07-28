# Writeup for picoCTF 2022 : GDB Test Drive

## Tools:
- GDB (GNU Debugger)
- Terminal/Command line
- Instruction following methodology

## Steps:

### 1. Initial Challenge Analysis
This challenge served as an introductory exercise designed to familiarize participants with GDB (GNU Debugger) usage. The title "GDB Test Drive" immediately indicated that this was a hands-on tutorial for learning basic GDB commands and debugging techniques.

The challenge was structured as a guided exercise where the task description itself provided step-by-step instructions that needed to be followed using GDB to reveal the flag.

### 2. Understanding the Challenge Format
Unlike typical reverse engineering challenges that require independent analysis and problem-solving, this challenge adopted a tutorial approach where:

- The task description contained explicit instructions for GDB usage
- Each step was designed to teach specific GDB commands and concepts
- Following the instructions sequentially would lead to flag discovery
- The challenge served as both a learning exercise and a flag retrieval task

This format made it an excellent introduction to GDB for participants who might be new to debugging tools.

### 3. Following the Provided Instructions
The challenge instructions guided me through a series of GDB commands and operations. The step-by-step approach included:

- **Loading the binary**: Instructions on how to start GDB with the target executable
- **Basic navigation**: Commands for exploring the program structure
- **Execution control**: Techniques for running and controlling program execution
- **Information gathering**: Methods for extracting relevant data from the debugging session

Each instruction was designed to demonstrate fundamental GDB capabilities while progressing toward the ultimate goal of flag extraction.

### 4. Executing GDB Commands
Following the provided guidance, I executed the specified GDB commands in sequence. The instructions were clear and detailed, making it straightforward to:

- Launch GDB with the appropriate parameters
- Navigate through the program's structure
- Execute the necessary debugging operations
- Observe the results of each command

The tutorial nature of the challenge ensured that each step built upon the previous ones, creating a comprehensive learning experience.

### 5. Flag Discovery Through Guided Process
By carefully following each instruction provided in the task description, the debugging process systematically revealed information about the program. The guided approach led me through the exact sequence of operations needed to:

- Access the relevant program components
- Execute the appropriate analysis commands
- Extract the flag information from the debugging session

The instructions were designed to ensure success when followed correctly, making this an educational rather than exploratory challenge.

### 6. Learning Outcomes
This challenge effectively served multiple purposes:
- **GDB introduction**: Provided hands-on experience with basic GDB commands
- **Debugging concepts**: Introduced fundamental debugging methodologies
- **Tool familiarity**: Built confidence in using command-line debugging tools
- **Foundation building**: Established skills needed for more advanced reverse engineering challenges

The tutorial approach made complex debugging concepts accessible to beginners while still providing value to participants seeking to reinforce their GDB knowledge.

### 7. Verification and Solution
Following the complete sequence of instructions provided in the task description successfully revealed the flag. The guided nature of the challenge ensured that correct execution of the steps would lead to the intended result, confirming both the learning objectives and the flag discovery process.

This challenge exemplified how educational CTF problems can effectively combine skill-building with practical application, providing participants with both knowledge and achievement.

## Flag:
```picoCTF{d3bugg3r_dr1v3_72bd8355}```
