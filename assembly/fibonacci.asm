A small program that calculates and prints terms of the Fibonacci series

; fibo.asm
; assemble using nasm:   
; nasm -o fibo.com -f bin fibo.asm
;
;****************************************************************************
; Alterable Constant
;****************************************************************************
 
	maxTerms    equ 15000	; number of terms of the series to calculate

;****************************************************************************


; digits = terms * log(phi) + log(sqrt(5))/log(phi)

        digits	    equ (maxTerms*209+1673)/1000	


        org     100h            ; this is a DOS com file
;****************************************************************************
;****************************************************************************
main:	
; initializes the two numbers and the counter.  Note that this assumes
; that the counter and num1 and num2 areas are contiguous!
;
	mov	ax,'00'		; initialize to all ASCII zeroes
	mov	di,counter		; including the counter
	mov	cx,digits+cntDigits/2	; two bytes at a time
	cld			; initialize from low to high memory
	rep	stosw		; write the data
	inc	ax		; make sure ASCII zero is in al
	mov	[num1 + digits - 1],al ; last digit is one
	mov	[num2 + digits - 1],al ; 
	mov	[counter + cntDigits - 1],al

	jmp	.bottom		; done with initialization, so begin

.top
	; add num1 to num2
	mov	di,num1+digits-1
	mov	si,num2+digits-1
	mov	cx,digits	; 
	call	AddNumbers	; num2 += num1
	mov	bp,num2		;
	call	PrintLine	;
	dec	dword [term]	; decrement loop counter
	jz	.done		;

	; add num2 to num1
	mov	di,num2+digits-1
	mov	si,num1+digits-1
	mov	cx,digits	;
	call	AddNumbers	; num1 += num2
.bottom
	mov	bp,num1		;
	call	PrintLine	;
	dec	dword [term]	; decrement loop counter
	jnz	.top		;
.done
	call	CRLF		; finish off with CRLF
	mov	ax,4c00h	; terminate
	int	21h		;


;****************************************************************************
;
; PrintLine
; prints a single line of output containing one term of the 
; Fibonacci sequence.  The first few lines look like this:
;
; Fibonacci(1): 1
; Fibonacci(2): 1
; Fibonacci(3): 2
; Fibonacci(4): 3
;
; INPUT:     ds:bp ==> number string, cx = max string length
; OUTPUT:    CF set on error, AX = error code if carry set
; DESTROYED: ax, bx, cx, dx, di
;
;****************************************************************************
PrintLine:
	mov	dx,eol		; print combined CRLF and msg1
	mov	cx,msg1len+eollen   ; 
	call	PrintString	;

	mov	di,counter	; print counter
	mov	cx,cntDigits	;
	call	PrintNumericString

	call	IncrementCount	; also increment the counter

	mov	dx,msg2		; print msg2
	mov	cx,msg2len	;
	call	PrintString	;
	
	mov	di,bp		; recall address of number
	mov	cx,digits	;
	; deliberately fall through to PrintNumericString

;****************************************************************************
;
; PrintNumericString 
; prints the numeric string at DS:DI, suppressing leading zeroes
; max length is CX
;
; INPUT:     ds:di ==> number string, cx = max string length
; OUTPUT:    CF set on error, AX = error code if carry set
; DESTROYED: ax, bx, cx, dx, di
;
;****************************************************************************
PrintNumericString:
	; first scan for the first non-zero byte
	mov	al,'0'		; look for ASCII zero
	cld			; scan from MSD to LSD
	repe	scasb		;
	mov	dx,di		; points to one byte after
	dec	dx		; back up one character
	inc	cx		;
	; deliberately fall through to PrintString

;****************************************************************************
; 
; PrintString 
; prints the string at DS:DX with length CX to stdout
;
; INPUT:     ds:dx ==> string, cx = string length
; OUTPUT:    CF set on error, AX = error code if carry set
; DESTROYED: ax, bx
;
;****************************************************************************
PrintString:
	mov	bx, 1		; write to stdout
	mov     ah, 040h        ; write to file handle
	int	21h		; ignore return value
	ret			;

;****************************************************************************
;
; AddNumbers
; add number 2 at ds:si to number 1 at es:di of width cx
; 
;
; INPUT:     es:di ==> number1, ds:si ==> number2, cx= max width
; OUTPUT:    CF set on overflow
; DESTROYED: ax, si, di
;
;****************************************************************************
AddNumbers:
	std			; go from LSB to MSB
	clc			;
	pushf			; save carry flag
.top
	mov	ax,0f0fh	; convert from ASCII BCD to BCD
	and  	al,[si]		; get next digit of number2 in al
	and	ah,[di]		; get next digit of number1 in ah
	popf			; recall carry flag
	adc	al,ah		; add these digits
	aaa			; convert to BCD
	pushf			;
	add	al,'0'		; convert back to ASCII BCD digit
	stosb			; save it and increment both counters
	dec	si		;
	loop	.top		; keep going until we've got them all
	popf			; recall carry flag
	ret			;

;****************************************************************************
; 
; IncrementCount
; increments a multidigit term counter by one
;
; INPUT:     none
; OUTPUT:    CF set on overflow
; DESTROYED: ax, cx, di
;
;****************************************************************************
IncrementCount:
	mov	cx,cntDigits	;
	mov	di,counter+cntDigits-1
	std			; go from LSB to MSB
	stc			; this is our increment
	pushf			; save carry flag
.top
	mov	ax,000fh	; convert from ASCII BCD to BCD
	and	al,[di]		; get next digit of counter in al
	popf			; recall carry flag
	adc	al,ah		; add these digits
	aaa			; convert to BCD
	pushf			;
	add	al,'0'		; convert back to ASCII BCD digit
	stosb			; save and increment counter
	loop	.top		;
	popf			; recall carry flag
	ret			;
	
;****************************************************************************
;
; CRLF
; prints carriage return, line feed pair to stdout
;
; INPUT:     none
; OUTPUT:    CF set on error, AX = error code if carry set
; DESTROYED: ax, bx, cx, dx
;
;****************************************************************************
CRLF:	mov	dx,eol		;
	mov	cx,eollen	;
	jmp	PrintString	;

;****************************************************************************
; static data
;****************************************************************************
eol	db  13,10		; DOS-style end of line
eollen	equ $ - eol

msg1	db  'Fibonacci('	;
msg1len	equ $ - msg1

msg2	db  '): '		;
msg2len	equ $ - msg2
;****************************************************************************
; initialized data
;****************************************************************************
term dd maxTerms		;
;****************************************************************************
; unallocated data
; 
;
;****************************************************************************
; static data
counter:			;
num1 equ counter+cntDigits	;
num2 equ num1+digits		;
		
