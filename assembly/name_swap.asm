section .data 
	Name db "Mary Bros", 0xa  ;instruction for a new line
	lenName equ $-Name    ;get message length

section .text             ;code segment
	global _start
	
_start:
   ; print  the name	
   mov	edx,lenName      ;message length
   mov	ecx,Name         ;message to write
   mov	ebx,1            ;file descriptor (stdout)
   mov	eax,4            ;system call number (sys_write)
   int	0x80             ;call kernel
   
   
   mov [Name], dword "Luis" 
   
   ; print  the new name	
   mov	edx,lenName      ;message length
   mov	ecx,Name         ;message to write
   mov	ebx,1            ;file descriptor (stdout)
   mov	eax,4            ;system call number (sys_write)
   int	0x80             ;call kernel
  
   
   ;exit code
   mov eax, 1
   int 0x80
