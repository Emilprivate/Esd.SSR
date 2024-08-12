section .text
    global asm4

asm4:
    push    ebp
    mov     ebp, esp
    push    ebx
    sub     esp, 0x10
    mov     DWORD [ebp-0x10], 0x27a
    mov     DWORD [ebp-0x0c], 0x0

jmp_loop:
    jmp     check_condition

loop_start:
    add     DWORD [ebp-0x0c], 0x1

check_condition:
    mov     edx, DWORD [ebp-0x0c]
    mov     eax, DWORD [ebp+0x8]
    add     eax, edx
    movzx   eax, BYTE [eax]
    test    al, al
    jne     loop_start

    mov     DWORD [ebp-0x08], 0x1
    jmp     outer_loop_end

inner_loop_start:
    mov     edx, DWORD [ebp-0x08]
    mov     eax, DWORD [ebp+0x8]
    add     eax, edx
    movzx   eax, BYTE [eax]
    movsx   edx, al
    mov     eax, DWORD [ebp-0x08]
    lea     ecx, [eax-0x1]
    mov     eax, DWORD [ebp+0x8]
    add     eax, ecx
    movzx   eax, BYTE [eax]
    movsx   eax, al
    sub     edx, eax
    mov     eax, edx
    mov     edx, eax
    mov     eax, DWORD [ebp-0x10]
    lea     ebx, [edx+eax*1]
    mov     eax, DWORD [ebp-0x08]
    lea     edx, [eax+0x1]
    mov     eax, DWORD [ebp+0x8]
    add     eax, edx
    movzx   eax, BYTE [eax]
    movsx   edx, al
    mov     ecx, DWORD [ebp-0x08]
    mov     eax, DWORD [ebp+0x8]
    add     eax, ecx
    movzx   eax, BYTE [eax]
    movsx   eax, al
    sub     edx, eax
    mov     eax, edx
    add     eax, ebx
    mov     DWORD [ebp-0x10], eax
    add     DWORD [ebp-0x08], 0x1

outer_loop_end:
    mov     eax, DWORD [ebp-0xc]
    sub     eax, 0x1
    cmp     DWORD [ebp-0x08], eax
    jl      inner_loop_start

    mov     eax, DWORD [ebp-0x10]
    add     esp, 0x10
    pop     ebx
    pop     ebp
    ret

