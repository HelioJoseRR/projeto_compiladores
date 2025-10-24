	.file	"output.c"
	.section .rdata,"dr"
LC0:
	.ascii "%d\12\0"
	.text
	.p2align 4,,15
	.globl	_soma
	.def	_soma;	.scl	2;	.type	32;	.endef
_soma:
LFB30:
	.cfi_startproc
	pushl	%ebx
	.cfi_def_cfa_offset 8
	.cfi_offset 3, -8
	subl	$24, %esp
	.cfi_def_cfa_offset 32
	movl	_a, %edx
	movl	36(%esp), %ebx
	addl	32(%esp), %ebx
	jmp	L2
	.p2align 4,,10
L10:
	addl	$1, %edx
	movl	$LC0, (%esp)
	movl	%edx, 4(%esp)
	movl	%edx, _a
	call	_printf
	movl	_a, %edx
	cmpl	$15, %edx
	je	L5
L2:
L3:
	cmpl	$19, %edx
	jle	L10
L5:
	addl	$24, %esp
	.cfi_def_cfa_offset 8
	leal	10(%ebx), %eax
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
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$1, _b
	movl	$10, %eax
	.p2align 4,,10
L12:
	addl	$1, %eax
	movl	$LC0, (%esp)
	movl	%eax, 4(%esp)
	movl	%eax, _a
	call	_printf
	movl	_a, %eax
	cmpl	$15, %eax
	je	L15
L13:
L14:
	cmpl	$19, %eax
	jle	L12
L15:
	movl	$15, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	xorl	%eax, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE31:
	.comm	_b, 4, 2
	.comm	_a, 4, 2
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
