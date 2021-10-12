SYS_EXIT equ 1
SYS_READ equ 3 
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1 

segment .data

    ask1 db "Enter a digit:", 0xa, 0xd
    len1 equ $- ask1
    
    ask2 db "Enter another digit:", 0xa, 0xd
    len2 equ $- ask2
    
    ans db "Here's the sum:", 0xa, 0xd
    len3 equ $- ans
    
segment .bss

    inp1 resb 2
    inp2 resb 2
    res  resb 2
    
section .text   
	global _start
	
_start:
   ; ask for first digit
   mov	edx,len1          ;message length
   mov	ecx,ask1          ;message to write
   mov	ebx,STDOUT        ;file descriptor (stdout)
   mov	eax,SYS_WRITE     ;system call number (sys_write)
   int	0x80              ;call kernel
    
   ; read user input    
   mov	edx,2             ;message length 
   mov	ecx,inp1          ;message to write
   mov	ebx,STDIN         ;file descriptor (std_in)
   mov	eax,SYS_READ      ;system call number (sys_read)
   int	0x80               ;call kernel 
   
   ; ask for second digit
   mov	edx,len2          ;message length
   mov	ecx,ask2          ;message to write
   mov	ebx,STDOUT        ;file descriptor (stdout)
   mov	eax,SYS_WRITE     ;system call number (sys_write)
   int	0x80              ;call kernel
   
   ; read user input    
   mov	edx,2             ;message length 
   mov	ecx,inp2          ;message to write
   mov	ebx,STDIN         ;file descriptor (std_in)
   mov	eax,SYS_READ      ;system call number (sys_read)
   int	0x80              ;call kernel 
   
   ; moving the first number to eax register and second number to ebx
   ; and subtracting ascii '0' to convert it into a decimal number
   mov eax, [inp1]
   sub eax, "0"
   
   mov ebx, [inp2]
   sub ebx, "0"
   
   add eax, ebx 
   add eax, 0              ; add '0' to to convert the sum from decimal to ASCII
   
   
   ; print the sum
   mov	edx,1              ;message length
   mov	ecx,ans            ;message to write
   mov	ebx,STDOUT         ;file descriptor (stdout)
   mov	eax,SYS_WRITE      ;system call number (sys_write)
   int	0x80               ;call kernel

exit: 

    mov eax, SYS_EXIT
    xor ebx, ebx
    int 0x80 
   
