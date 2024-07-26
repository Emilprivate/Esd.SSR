# My Pwndbg Notes
A collection of my Pwndbg notes for reverse engineering and binary exploitation. 

## References
- [Pwndbg Github](https://github.com/pwndbg/pwndbg)
- [Pwndbg Docs](https://browserpwndbg.readthedocs.io/en/docs/)

## Commands
- ```file <file>``` to load the binary and read its symbols.
- ```info functions``` to list all functions in the binary. Optionally add the name of the function after to isolate the one you're after.
- ```disassemble <function name>``` to disassemble the function.
- ```lay asm``` lays out the entire asm of the application presumably.
- ```break <address>``` sets a breakpoint at the address
- ```run``` runs the binary
- ```jump <address>``` jumps to the addressi.
