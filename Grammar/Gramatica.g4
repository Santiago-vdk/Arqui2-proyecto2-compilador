grammar Gramatica;

/*
 * Parser Rules
 */

gramatica                : line+ EOF ;

line		    		 : ((instruccion_r ra rb COMMA WHITESPACE rc ) | 	
						   (instruccion_r ra rb ) | 			  
						   (instruccion_i ra rb COMMA WHITESPACE (inm | LABEL) ) | 
						   (instruccion_i ra inm ) | 
						   (instruccion_j LABEL ) |
						   (LABEL DIGIT? COLON)
						   
						   ) NEWLINE?;

instruccion_r              : INSTR_R WHITESPACE ;

instruccion_i              : INSTR_I WHITESPACE ;

instruccion_j              : INSTR_J WHITESPACE ;

ra	      				   : REG COMMA WHITESPACE;

rb							: REG  ;

rc							: REG ;

inm							: PAREN_OPEN? DIGIT+ PAREN_CLOSE?;

/*
 * Lexer Rules
 */

 fragment LOWERCASE  : [a-z] ;
 fragment UPPERCASE  : [A-Z] ;

 REG : ('$0' | '$1' | '$2' | '$3' | '$4' | '$5' | '$6' | '$7' | '$8' | '$9' | '$10' | 
	    '$11' | '$12' | '$13' | '$14' | '$15' | '$16' | '$17' | '$18' | '$19' | '$20' | 
		'$21' | '$22' | '$23' | '$24' | '$25' | '$26' | '$27' | '$28' | '$29' | '$30' | '$31') ;

INSTR_R				:	('add' | 'addu' |  'and' | 'jr' | 'nor' 
						| 'or'   | 'slt' | 'sltu' | 'sll' | 'srl' 
						| 'sub' | 'subu' | 'vadd' | 'vsub' | 'vxor' | 'vand') ;

INSTR_I				:	('addi' | 'addiu' | 'andi' | 'beq' | 'bne'
						| 'lbu' | 'lhu' | 'll' | 'lui' | 'lw' | 'ori'
						| 'slti' | 'sltiu' | 'sb' | 'sc' | 'sh' | 'sw'
						| 'vaddi' | 'vsll' | 'vsrl' | 'vrotl' | 'vrotr'
						| 'vsb' | 'vlbu' | 'vmov' | 'show') ;

INSTR_J				:	('j' | 'jal') ;

LABEL                :  (LOWERCASE | UPPERCASE)+ DIGIT? ;

DIGIT				: [0-9]+ ;

COLON				: (':') ;

COMMA: 				(',') ;

WHITESPACE         : (' ') ;

PAREN_OPEN			: ('(') ;

PAREN_CLOSE			: (')') ;

NEWLINE             : ('\n' | '\r')+ ;