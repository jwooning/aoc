	.file	"part2.c"
	.text
	.p2align 4,,15
	.globl	gravity
	.type	gravity, @function
gravity:
.LFB34:
	.cfi_startproc
	movl	(%rsi), %eax
	cmpl	%eax, (%rdi)
	jle	.L2
	subl	$1, 12(%rdi)
	addl	$1, 12(%rsi)
.L3:
	movl	4(%rsi), %eax
	cmpl	%eax, 4(%rdi)
	jle	.L4
.L9:
	subl	$1, 16(%rdi)
	addl	$1, 16(%rsi)
.L5:
	movl	8(%rsi), %eax
	cmpl	%eax, 8(%rdi)
	jle	.L6
.L10:
	subl	$1, 20(%rdi)
	addl	$1, 20(%rsi)
	ret
	.p2align 4,,10
	.p2align 3
.L2:
	jge	.L3
	addl	$1, 12(%rdi)
	movl	4(%rsi), %eax
	subl	$1, 12(%rsi)
	cmpl	%eax, 4(%rdi)
	jg	.L9
.L4:
	jge	.L5
	addl	$1, 16(%rdi)
	movl	8(%rsi), %eax
	subl	$1, 16(%rsi)
	cmpl	%eax, 8(%rdi)
	jg	.L10
.L6:
	jge	.L1
	addl	$1, 20(%rdi)
	subl	$1, 20(%rsi)
.L1:
	ret
	.cfi_endproc
.LFE34:
	.size	gravity, .-gravity
	.p2align 4,,15
	.globl	velocity
	.type	velocity, @function
velocity:
.LFB35:
	.cfi_startproc
	movl	12(%rdi), %eax
	addl	%eax, (%rdi)
	movl	16(%rdi), %eax
	addl	%eax, 4(%rdi)
	movl	20(%rdi), %eax
	addl	%eax, 8(%rdi)
	ret
	.cfi_endproc
.LFE35:
	.size	velocity, .-velocity
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%lu\n"
.LC1:
	.string	"Found reoccurence at %lu\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB36:
	.cfi_startproc
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	xorl	%r14d, %r14d
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$296, %rsp
	.cfi_def_cfa_offset 352
	movq	%fs:40, %rax
	movq	%rax, 280(%rsp)
	xorl	%eax, %eax
	movabsq	$51539607556, %rax
	movq	$0, 44(%rsp)
	movl	$0, 52(%rsp)
	movq	%rax, 32(%rsp)
	movabsq	$64424509431, %rax
	movl	$13, 40(%rsp)
	movq	%rax, 64(%rsp)
	movabsq	$77309411317, %rax
	movq	$0, 76(%rsp)
	movq	%rax, 128(%rsp)
	movq	48(%rsp), %rax
	leaq	64(%rsp), %rbx
	movdqa	32(%rsp), %xmm0
	leaq	32(%rsp), %r15
	movl	$0, 84(%rsp)
	movl	$-3, 72(%rsp)
	leaq	96(%rsp), %rbp
	movq	%rax, 176(%rsp)
	movq	80(%rsp), %rax
	leaq	128(%rsp), %r12
	movaps	%xmm0, 160(%rsp)
	movq	$0, 108(%rsp)
	movq	$-7, 96(%rsp)
	leaq	160(%rsp), %r13
	movdqa	64(%rsp), %xmm0
	movl	$2, 104(%rsp)
	movq	%rax, 208(%rsp)
	movl	$0, 116(%rsp)
	movq	$0, 140(%rsp)
	movl	$0, 148(%rsp)
	movl	$-1, 136(%rsp)
	movaps	%xmm0, 192(%rsp)
	movdqa	96(%rsp), %xmm0
	movq	112(%rsp), %rax
	movaps	%xmm0, 224(%rsp)
	movq	%rax, 240(%rsp)
	movq	144(%rsp), %rax
	movdqa	128(%rsp), %xmm0
	movq	%rax, 272(%rsp)
	leaq	192(%rsp), %rax
	movaps	%xmm0, 256(%rsp)
	movq	%rax, 8(%rsp)
	leaq	224(%rsp), %rax
	movq	%rax, 16(%rsp)
	leaq	256(%rsp), %rax
	movq	%rax, 24(%rsp)
	.p2align 4,,10
	.p2align 3
.L13:
	movq	%r15, %rdi
	movq	%rbx, %rsi
	addq	$1, %r14
	call	gravity
	movq	%rbp, %rsi
	call	gravity
	movq	%r12, %rsi
	call	gravity
	movq	%rbx, %rdi
	movq	%rbp, %rsi
	call	gravity
	movq	%r12, %rsi
	call	gravity
	movq	%rbp, %rdi
	call	gravity
	movl	44(%rsp), %eax
	addl	%eax, 32(%rsp)
	movl	48(%rsp), %eax
	addl	%eax, 36(%rsp)
	movl	52(%rsp), %eax
	addl	%eax, 40(%rsp)
	movl	76(%rsp), %eax
	addl	%eax, 64(%rsp)
	movl	80(%rsp), %eax
	addl	%eax, 68(%rsp)
	movl	84(%rsp), %eax
	addl	%eax, 72(%rsp)
	movl	108(%rsp), %eax
	addl	%eax, 96(%rsp)
	movl	112(%rsp), %eax
	addl	%eax, 100(%rsp)
	movl	116(%rsp), %eax
	addl	%eax, 104(%rsp)
	movl	140(%rsp), %eax
	addl	%eax, 128(%rsp)
	movl	144(%rsp), %eax
	addl	%eax, 132(%rsp)
	movl	148(%rsp), %eax
	addl	%eax, 136(%rsp)
	movabsq	$4835703278458516699, %rax
	mulq	%r14
	shrq	$18, %rdx
	imulq	$1000000, %rdx, %rdx
	cmpq	%rdx, %r14
	je	.L26
.L14:
	movq	(%r15), %rax
	movq	8(%r15), %rdx
	xorq	0(%r13), %rax
	xorq	8(%r13), %rdx
	orq	%rax, %rdx
	jne	.L13
	movq	16(%r13), %rax
	cmpq	%rax, 16(%r15)
	jne	.L13
	movq	8(%rsp), %rcx
	movq	(%rbx), %rax
	movq	8(%rbx), %rdx
	xorq	(%rcx), %rax
	xorq	8(%rcx), %rdx
	orq	%rax, %rdx
	jne	.L13
	movq	16(%rcx), %rax
	cmpq	%rax, 16(%rbx)
	jne	.L13
	movq	16(%rsp), %rcx
	movq	0(%rbp), %rax
	movq	8(%rbp), %rdx
	xorq	(%rcx), %rax
	xorq	8(%rcx), %rdx
	orq	%rax, %rdx
	jne	.L13
	movq	16(%rcx), %rax
	cmpq	%rax, 16(%rbp)
	jne	.L13
	movq	24(%rsp), %rcx
	movq	(%r12), %rax
	movq	8(%r12), %rdx
	xorq	(%rcx), %rax
	xorq	8(%rcx), %rdx
	orq	%rax, %rdx
	jne	.L13
	movq	16(%rcx), %rax
	cmpq	%rax, 16(%r12)
	jne	.L13
	leaq	.LC1(%rip), %rsi
	xorl	%eax, %eax
	movq	%r14, %rdx
	movl	$1, %edi
	call	__printf_chk@PLT
	movq	280(%rsp), %rbx
	xorq	%fs:40, %rbx
	movl	$1, %eax
	jne	.L27
	addq	$296, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L26:
	.cfi_restore_state
	leaq	.LC0(%rip), %rsi
	movq	%r14, %rdx
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	jmp	.L14
.L27:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE36:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
