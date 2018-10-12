# Generated from Grammar/Gramatica.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#gramatica.
    def enterGramatica(self, ctx:GramaticaParser.GramaticaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#gramatica.
    def exitGramatica(self, ctx:GramaticaParser.GramaticaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line.
    def enterLine(self, ctx:GramaticaParser.LineContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line.
    def exitLine(self, ctx:GramaticaParser.LineContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_i_3operandos.
    def enterLine_i_3operandos(self, ctx:GramaticaParser.Line_i_3operandosContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_i_3operandos.
    def exitLine_i_3operandos(self, ctx:GramaticaParser.Line_i_3operandosContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_extra_memoria.
    def enterLine_extra_memoria(self, ctx:GramaticaParser.Line_extra_memoriaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_extra_memoria.
    def exitLine_extra_memoria(self, ctx:GramaticaParser.Line_extra_memoriaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_r_3operandos.
    def enterLine_r_3operandos(self, ctx:GramaticaParser.Line_r_3operandosContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_r_3operandos.
    def exitLine_r_3operandos(self, ctx:GramaticaParser.Line_r_3operandosContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_r_2operandos_1inmediato.
    def enterLine_r_2operandos_1inmediato(self, ctx:GramaticaParser.Line_r_2operandos_1inmediatoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_r_2operandos_1inmediato.
    def exitLine_r_2operandos_1inmediato(self, ctx:GramaticaParser.Line_r_2operandos_1inmediatoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_branch.
    def enterLine_branch(self, ctx:GramaticaParser.Line_branchContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_branch.
    def exitLine_branch(self, ctx:GramaticaParser.Line_branchContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_jump.
    def enterLine_jump(self, ctx:GramaticaParser.Line_jumpContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_jump.
    def exitLine_jump(self, ctx:GramaticaParser.Line_jumpContext):
        pass


    # Enter a parse tree produced by GramaticaParser#line_label.
    def enterLine_label(self, ctx:GramaticaParser.Line_labelContext):
        pass

    # Exit a parse tree produced by GramaticaParser#line_label.
    def exitLine_label(self, ctx:GramaticaParser.Line_labelContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion_r.
    def enterInstruccion_r(self, ctx:GramaticaParser.Instruccion_rContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion_r.
    def exitInstruccion_r(self, ctx:GramaticaParser.Instruccion_rContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion_i.
    def enterInstruccion_i(self, ctx:GramaticaParser.Instruccion_iContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion_i.
    def exitInstruccion_i(self, ctx:GramaticaParser.Instruccion_iContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion_j.
    def enterInstruccion_j(self, ctx:GramaticaParser.Instruccion_jContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion_j.
    def exitInstruccion_j(self, ctx:GramaticaParser.Instruccion_jContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion_extra.
    def enterInstruccion_extra(self, ctx:GramaticaParser.Instruccion_extraContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion_extra.
    def exitInstruccion_extra(self, ctx:GramaticaParser.Instruccion_extraContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion_logic.
    def enterInstruccion_logic(self, ctx:GramaticaParser.Instruccion_logicContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion_logic.
    def exitInstruccion_logic(self, ctx:GramaticaParser.Instruccion_logicContext):
        pass


    # Enter a parse tree produced by GramaticaParser#jump_reg.
    def enterJump_reg(self, ctx:GramaticaParser.Jump_regContext):
        pass

    # Exit a parse tree produced by GramaticaParser#jump_reg.
    def exitJump_reg(self, ctx:GramaticaParser.Jump_regContext):
        pass


    # Enter a parse tree produced by GramaticaParser#inmediate.
    def enterInmediate(self, ctx:GramaticaParser.InmediateContext):
        pass

    # Exit a parse tree produced by GramaticaParser#inmediate.
    def exitInmediate(self, ctx:GramaticaParser.InmediateContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion_branch.
    def enterInstruccion_branch(self, ctx:GramaticaParser.Instruccion_branchContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion_branch.
    def exitInstruccion_branch(self, ctx:GramaticaParser.Instruccion_branchContext):
        pass


    # Enter a parse tree produced by GramaticaParser#number.
    def enterNumber(self, ctx:GramaticaParser.NumberContext):
        pass

    # Exit a parse tree produced by GramaticaParser#number.
    def exitNumber(self, ctx:GramaticaParser.NumberContext):
        pass


    # Enter a parse tree produced by GramaticaParser#regs.
    def enterRegs(self, ctx:GramaticaParser.RegsContext):
        pass

    # Exit a parse tree produced by GramaticaParser#regs.
    def exitRegs(self, ctx:GramaticaParser.RegsContext):
        pass


