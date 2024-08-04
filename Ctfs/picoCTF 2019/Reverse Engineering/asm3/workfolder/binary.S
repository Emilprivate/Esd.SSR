global _start

section .text

main:
    push   rbp
    mov    rbp,rsp
    xor    rax,rax
    mov    ah,BYTE [rbp+0xb]
    shl    ax,0x10
    sub    al,BYTE [rbp+0xd]
    add    ah,BYTE [rbp+0xc]
    xor    ax,WORD [rbp+0x12]
    nop
    pop    rbp
    ret 
