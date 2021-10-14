section .bss
    num resb 1

section .text
    global _start
    
_start:
    mov ecx, 10
    mov eax, "1"
    
loop_one:
    mov [num], eax
    mov eax, 4 
    mov ebx, 1
    push ecx   ;add on top of stack
    
    mov ecx, num
    mov edx, 1
    int 0x80
    
    mov eax, [num]
    sub eax, "0"
    inc eax
    add eax, "0"
    pop ecx
    loop loop_one
    
    mov eax,1 
    int 0x80
