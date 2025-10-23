	.file	"output.c"
	.section .rdata,"dr"
LC0:
	.ascii "%d\12\0"
	.text
	.p2align 4,,15
	.globl	_count
	.def	_count;	.scl	2;	.type	32;	.endef
_count:
LFB30:
	.cfi_startproc
	pushl	%ebx
	.cfi_def_cfa_offset 8
	.cfi_offset 3, -8
	subl	$24, %esp
	.cfi_def_cfa_offset 32
	movl	32(%esp), %ebx
	testl	%ebx, %ebx
	js	L3
	.p2align 4,,10
L7:
	movl	%ebx, 4(%esp)
	movl	$LC0, (%esp)
	subl	$1, %ebx
	call	_printf
	cmpl	$-1, %ebx
	jne	L7
L3:
	addl	$24, %esp
	.cfi_def_cfa_offset 8
	xorl	%eax, %eax
	popl	%ebx
	.cfi_restore 3
	.cfi_def_cfa_offset 4
	ret
	.cfi_endproc
LFE30:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section	.text.startup,"x"
	.p2align 4,,15
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB31:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	.cfi_offset 3, -12
	movl	$10, %ebx
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$10, _num
	.p2align 4,,10
L13:
	movl	%ebx, 4(%esp)
	movl	$LC0, (%esp)
	subl	$1, %ebx
	call	_printf
	cmpl	$-1, %ebx
	jne	L13
L14:
	xorl	%eax, %eax
	movl	-4(%ebp), %ebx
	leave
	.cfi_restore 5
	.cfi_restore 3
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE31:
	.comm	_num, 4, 2
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
