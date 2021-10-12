section .data 
	userMsg db "enter a number:"
	lenUserMsg equ $-userMsg    ;get message length
	dispMsg db "You have entered: "
	lenDispMsg equ $-dispMsg

section .bss    ;(uninitialized data)
	num resb 5
	
section .text   ;code segment
	global _start
	
_start:
   ; prompt user	
   mov	edx,lenUserMsg   ;message length
   mov	ecx,userMsg      ;message to write
   mov	ebx,1            ;file descriptor (stdout)
   mov	eax,4            ;system call number (sys_write)
   int	80h             ;call kernel
   
   ; read user input
   mov	edx,5            ;message length (5 bytes)
   mov	ecx,num          ;message to write
   mov	ebx,2            ;file descriptor (stdout)
   mov	eax,3            ;system call number (sys_read)
   int	80h             ;call kernel
   
   ;output the message
   mov	edx,lenDispMsg   ;message length
   mov	ecx, dispMsg     ;message to write
   mov	ebx,1            ;file descriptor (stdout)
   mov	eax,4            ;system call number (sys_write)
   int	80h 
   
   ;output the number entered
   mov	edx, 5           ;message length
   mov	ecx, num         ;message to write
   mov	ebx,1            ;file descriptor (stdout)
   mov	eax,4            ;system call number (sys_write)
   int	80h 
   
   ;exit code
   mov eax, 1
   mov ebx, 0
   int 80h
