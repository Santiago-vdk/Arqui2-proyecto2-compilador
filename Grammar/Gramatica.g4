grammar Gramatica;

/*
 * Parser Rules
 */

gramatica                : line+ EOF ;

line		    		: 	blank (COMMENT | line_extra_memoria | line_r_3operandos |
								line_r_2operandos_1inmediato | line_i_3Operandos_inmediate |
								line_i_3operandos | line_branch | line_jump |
								line_label ) NEWLINE? SPACES?;



line_i_3operandos		:	instruccion_i WHITESPACE regs COMMA WHITESPACE regs COMMA 
							WHITESPACE inmediate (WHITESPACE+)? COMMENT?;

line_i_3Operandos_inmediate : 	instruccion_i WHITESPACE regs COMMA
							WHITESPACE number PAREN_OPEN regs PAREN_CLOSE
							(WHITESPACE+)? COMMENT?;


line_extra_memoria		:	instruccion_extra WHITESPACE regs COMMA
							WHITESPACE number PAREN_OPEN regs PAREN_CLOSE
							(WHITESPACE+)? COMMENT?;
							
line_r_3operandos		:	instruccion_r WHITESPACE regs COMMA
							WHITESPACE regs COMMA
							WHITESPACE regs 
							(WHITESPACE+)? COMMENT?;

line_r_2operandos_1inmediato		:	instruccion_r WHITESPACE regs COMMA
										WHITESPACE regs COMMA
										WHITESPACE number WHITESPACE
										(WHITESPACE+)? COMMENT?;

line_branch				:	instruccion_branch WHITESPACE regs
							COMMA WHITESPACE regs COMMA WHITESPACE LABEL
							(WHITESPACE+)? COMMENT?;

line_jump				:	instruccion_j WHITESPACE LABEL
							(WHITESPACE+)? COMMENT?;

line_label				:	LABEL COLON
							(WHITESPACE+)? COMMENT?;

instruccion_r              : (INSTR_R  | INSTR_R_CAPS | instruccion_logic)  ;

instruccion_i              : (INSTR_I | INSTR_I_CAPS) ;

instruccion_j				: (INSTR_J | INSTR_J_CAPS) ;

instruccion_extra			: (INSTR_EXTRA | INSTR_EXTRA_CAPS);

instruccion_logic			: (INSTR_LOGIC | INSTR_LOGIC_CAPS);

jump_reg					: PAREN_OPEN? WHITESPACE? (regs) WHITESPACE? PAREN_CLOSE?;

inmediate					: PAREN_OPEN? DIGIT+ PAREN_CLOSE?;

instruccion_branch			: (INSTR_BRANCH | INSTR_BRANCH_CAPS);

number 						: DIGIT+  ;

regs						: (CONSTANT_REG | V_REG | A_REG | T_REG | S_REG | K_REG |
POINTER_REG | NUMBER_REG);

blank						: (SPACES+)? ;

/*
 * Lexer Rules
 */

fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

NUMBER_REG : ('$0' | '$1' | '$2' | '$3' | '$4' | '$5' | '$6' | '$7' | '$8' |
'$9') ;

CONSTANT_REG : ('$zero' | '$at')  ;

V_REG : ('$v0' | '$v1')  ;

A_REG : ('$a0' | '$a1' | '$a2' | '$a3') ;

T_REG : ('$t0' | '$t1' | '$t2' | '$t3' | '$t4' | '$t5' | '$t6' | '$t7' | '$t8' |
'$t9') ;

S_REG : ('$s0' | '$s1' | '$s2' | '$s3' | '$s4' | '$s5' | '$s6' | '$s7' ) ;

K_REG : ('$k0' | '$k1')  ;

POINTER_REG : ('$gp' | '$sp' | '$fp' | '$ra' ) ;

INSTR_R				:	('sra' | 'add' | 'addu' |  'and' | 'jr' | 'nor' 
						| 'or'   | 'slt' | 'sltu' | 'sll' | 'srl' 
						| 'sub' | 'subu' | 'vadd' | 'vsub' | 'vxor' | 'vand') ;

INSTR_R_CAPS		:	('SRA' | 'ADD' | 'ADDU' |  'AND' | 'JR' | 'NOR' 
						| 'OR'   | 'SLT' | 'SLTU' | 'SLL' | 'SRL' 
						| 'SUB' | 'SUBU' | 'VADD' | 'VSUB' | 'VXOR' | 'VAAND') ;

INSTR_I				:	('addi' | 'addiu' | 'andi'
						 | 'lhu' | 'll' | 'lui' | 'lw' | 'ori'
						| 'slti' | 'sltiu' | 'sc' | 'sh' | 'sw'
						| 'vaddi' | 'vsll' | 'vsrl' | 'vrotl' | 'vrotr'
						| 'vsb' | 'vlbu' | 'vmov' | 'show') ;

INSTR_I_CAPS 		: ('ADDI' | 'ADDIU' | 'ANDI'
						 | 'LHU' | 'LL' | 'LUI' | 'LW' | 'ORI'
						| 'SLTI' | 'SLTIU' | 'SC' | 'SH' | 'SW'
						| 'VADDI' | 'VSLL' | 'VSRL' | 'VROTL' | 'VROTR'
						| 'VSB' | 'VLBU' | 'VMOV' | 'SHOW');
						
INSTR_J			:  ('j' | 'jal')	;

INSTR_J_CAPS	:  ('J' | 'JAL')	;

INSTR_LOGIC			: ('and' | 'or' | 'xor' | 'not') ;

INSTR_LOGIC_CAPS			: ('AND' | 'OR' | 'XOR' | 'NOT') ;

INSTR_EXTRA			:  ('sb'| 'lbu')	;

INSTR_EXTRA_CAPS	:  ('SB'| 'LBU')	;
						
INSTR_BRANCH				:	('bne' | 'beq') ;

INSTR_BRANCH_CAPS			:	('BNE' | 'BEQ') ;

LABEL                :  (LOWERCASE | UPPERCASE)+ DIGIT? ;

DIGIT				: [0-9]+ ;

COLON				: (':') ;

COMMA: 				(',') ;

WHITESPACE         : (' ') ;

PAREN_OPEN			: ('(') ;

PAREN_CLOSE			: (')') ;

NEWLINE             : ('\n' | '\r')+ ;

COMMENT				: '/*' .*? '*/' -> skip;

LINE_COMMENT		: ('//' | '#') ~[\r\n]* -> skip;

SPACES				: [\t\r\n]+ -> skip;

TAB					: ('\t') ;
