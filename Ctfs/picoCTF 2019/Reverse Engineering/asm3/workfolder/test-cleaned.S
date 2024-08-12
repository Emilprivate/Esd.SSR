section .text
    global asm3  ; Make the function globally accessible

asm3:
    push   ebp              ; Save the base pointer
    mov    ebp, esp         ; Set the base pointer to the current stack pointer
    xor    eax, eax         ; Clear the eax register
    mov    ah, BYTE [ebp+0xb]  ; Move the byte at [ebp+0xb] into the high byte of ax (ah)
    shl    ax, 16           ; Shift ax left by 16 bits
    sub    al, BYTE [ebp+0xd]  ; Subtract the byte at [ebp+0xd] from the low byte of ax (al)
    add    ah, BYTE [ebp+0xc]  ; Add the byte at [ebp+0xc] to the high byte of ax (ah)
    xor    ax, WORD [ebp+0x12] ; XOR ax with the word at [ebp+0x12]
    pop    ebp              ; Restore the base pointer
    ret                     ; Return from the function

