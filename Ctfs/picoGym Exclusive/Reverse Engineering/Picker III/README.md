# Writeup for picoGym Exclusive : Picker III

## Tools:
- Python code analysis
- Source code examination
- Function pointer manipulation
- Dynamic function overwriting

## Steps:

### 1. Initial Challenge Analysis
This challenge represents the third installment in the "Picker" series, building upon the concepts and techniques learned from the previous challenges. Unlike Picker I and II, which had different approaches to accessing the flag, Picker III introduced more sophisticated access controls and required a deeper understanding of function manipulation.

The challenge provided Python source code that implemented additional security measures, making it more challenging to directly access the win function through conventional means.

### 2. Examining the Enhanced Security Model
Upon analyzing the Python source code, I discovered that this version had implemented more restrictive controls over which functions could be called. The program structure showed:

- Enhanced validation of user input
- Restricted access to certain functions
- Additional layers of protection around the win function
- A more complex program flow that required careful analysis

This increased complexity meant that the straightforward approaches used in previous Picker challenges would not be sufficient for this iteration.

### 3. Identifying Available Functions
Through careful examination of the code, I identified several key functions within the program:

- **`win` function**: Contains the flag (target function)
- **`getRandomNumber` function**: A utility function that appeared to be part of the program's normal operation
- **`overwrite` function**: A potentially exploitable function that could modify program behavior

The presence of the `overwrite` function was particularly interesting, as it suggested a mechanism for modifying the program's execution flow.

### 4. Understanding the Overwrite Mechanism
The critical discovery was the `overwrite` function, which provided the capability to modify function references within the program. This function appeared to allow:

- Replacement of one function with another
- Dynamic modification of the program's function table
- Redirection of function calls to different targets

This mechanism presented an opportunity to manipulate the program's execution flow to gain access to the restricted `win` function.

### 5. Developing the Exploitation Strategy
My approach involved using the `overwrite` function to replace a commonly called function with the `win` function. The strategy was:

1. **Identify a target function**: Find a function that would be called during normal program execution
2. **Use the overwrite mechanism**: Employ the `overwrite` function to replace the target function with `win`
3. **Trigger execution**: Execute the program flow that would normally call the target function

The `getRandomNumber` function was an ideal candidate because it appeared to be called during the program's normal operation.

### 6. Implementing the Function Replacement
I utilized the `overwrite` function to replace `getRandomNumber` with `win`:

```python
overwrite('getRandomNumber', win)
```

This operation effectively redirected any calls to `getRandomNumber` to execute the `win` function instead, providing a pathway to access the flag without directly calling the restricted function.

### 7. Executing the Modified Program Flow
Once the function replacement was in place, I proceeded to execute the normal program flow that would trigger a call to `getRandomNumber`. Since this function had been overwritten to point to `win`, the program executed the `win` function and revealed the flag.

### 8. Success and Learning Outcomes
The exploitation was successful, demonstrating the power of function pointer manipulation in bypassing access controls. This challenge effectively illustrated:

- The importance of understanding program control flow
- How function pointer vulnerabilities can be exploited
- The need for proper validation of function references
- Creative approaches to accessing restricted functionality

This challenge served as an excellent example of how seemingly innocuous functions like `overwrite` can become powerful tools for exploitation when combined with creative thinking and thorough code analysis.

## Flag:
```picoCTF{7h15_15_wh47_w3_g37_w17h_u53r5_1n_ch4rg3_c20f5222}```
