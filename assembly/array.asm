SYS_EXIT equ 1
SYS_READ equ 3 
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1 

section .data
    global x
    x:
        db 2
        db 4
        db 3
    
    sum:
        db 0

section .text
    global _start 
    
_start:
    mov eax, 3     ;number bytes to be summed
    mov ebx,0      ;EBX will store the sum
    mov ecx, x     ;ECX will point to the current element to be summed
    
top: 
    add ebx, [ecx]
    add ecx,1      ;move pointer to next element
    dec eax        ;decrement counter
    jnz top        ;if not zero, jump to top (and loop again)
    
end:
    add ebx, "0"
    mov [sum], ebx ;when finished and store the result in sum
    
display:
    mov edx, 1     ;message length
    mov ecx, sum   ;message to write
    mov ebx, STDOUT
    mov eax, SYS_WRITE
    int 0x80       ;call kernel
    
    mov edx, SYS_EXIT
    int 0x80
