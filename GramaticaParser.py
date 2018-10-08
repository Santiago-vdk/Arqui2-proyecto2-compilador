# Generated from Gramatica.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3.\n\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\39\n\3\3\3\5\3<\n\3\3\3\5\3?\n\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\3\n\5\nS\n\n\3\n\6\nV\n\n\r\n\16\nW\3\n\5\n[")
        buf.write("\n\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2_\2\25\3\2\2\2")
        buf.write("\4;\3\2\2\2\6@\3\2\2\2\bC\3\2\2\2\nF\3\2\2\2\fI\3\2\2")
        buf.write("\2\16M\3\2\2\2\20O\3\2\2\2\22R\3\2\2\2\24\26\5\4\3\2\25")
        buf.write("\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\34\5\6\4")
        buf.write("\2\34\35\5\f\7\2\35\36\5\16\b\2\36\37\7\n\2\2\37 \7\13")
        buf.write("\2\2 !\5\20\t\2!<\3\2\2\2\"#\5\6\4\2#$\5\f\7\2$%\5\16")
        buf.write("\b\2%<\3\2\2\2&\'\5\b\5\2\'(\5\f\7\2()\5\16\b\2)*\7\n")
        buf.write("\2\2*-\7\13\2\2+.\5\22\n\2,.\7\7\2\2-+\3\2\2\2-,\3\2\2")
        buf.write("\2.<\3\2\2\2/\60\5\b\5\2\60\61\5\f\7\2\61\62\5\22\n\2")
        buf.write("\62<\3\2\2\2\63\64\5\n\6\2\64\65\7\7\2\2\65<\3\2\2\2\66")
        buf.write("8\7\7\2\2\679\7\b\2\28\67\3\2\2\289\3\2\2\29:\3\2\2\2")
        buf.write(":<\7\t\2\2;\33\3\2\2\2;\"\3\2\2\2;&\3\2\2\2;/\3\2\2\2")
        buf.write(";\63\3\2\2\2;\66\3\2\2\2<>\3\2\2\2=?\7\16\2\2>=\3\2\2")
        buf.write("\2>?\3\2\2\2?\5\3\2\2\2@A\7\4\2\2AB\7\13\2\2B\7\3\2\2")
        buf.write("\2CD\7\5\2\2DE\7\13\2\2E\t\3\2\2\2FG\7\6\2\2GH\7\13\2")
        buf.write("\2H\13\3\2\2\2IJ\7\3\2\2JK\7\n\2\2KL\7\13\2\2L\r\3\2\2")
        buf.write("\2MN\7\3\2\2N\17\3\2\2\2OP\7\3\2\2P\21\3\2\2\2QS\7\f\2")
        buf.write("\2RQ\3\2\2\2RS\3\2\2\2SU\3\2\2\2TV\7\b\2\2UT\3\2\2\2V")
        buf.write("W\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2Y[\7\r\2\2ZY\3")
        buf.write("\2\2\2Z[\3\2\2\2[\23\3\2\2\2\n\27-8;>RWZ")
        return buf.getvalue()


class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "REG", "INSTR_R", "INSTR_I", "INSTR_J", 
                      "LABEL", "DIGIT", "COLON", "COMMA", "WHITESPACE", 
                      "PAREN_OPEN", "PAREN_CLOSE", "NEWLINE" ]

    RULE_gramatica = 0
    RULE_line = 1
    RULE_instruccion_r = 2
    RULE_instruccion_i = 3
    RULE_instruccion_j = 4
    RULE_ra = 5
    RULE_rb = 6
    RULE_rc = 7
    RULE_inm = 8

    ruleNames =  [ "gramatica", "line", "instruccion_r", "instruccion_i", 
                   "instruccion_j", "ra", "rb", "rc", "inm" ]

    EOF = Token.EOF
    REG=1
    INSTR_R=2
    INSTR_I=3
    INSTR_J=4
    LABEL=5
    DIGIT=6
    COLON=7
    COMMA=8
    WHITESPACE=9
    PAREN_OPEN=10
    PAREN_CLOSE=11
    NEWLINE=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class GramaticaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GramaticaParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.LineContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.LineContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_gramatica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGramatica" ):
                listener.enterGramatica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGramatica" ):
                listener.exitGramatica(self)




    def gramatica(self):

        localctx = GramaticaParser.GramaticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gramatica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.line()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GramaticaParser.INSTR_R) | (1 << GramaticaParser.INSTR_I) | (1 << GramaticaParser.INSTR_J) | (1 << GramaticaParser.LABEL))) != 0)):
                    break

            self.state = 23
            self.match(GramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(GramaticaParser.NEWLINE, 0)

        def instruccion_r(self):
            return self.getTypedRuleContext(GramaticaParser.Instruccion_rContext,0)


        def ra(self):
            return self.getTypedRuleContext(GramaticaParser.RaContext,0)


        def rb(self):
            return self.getTypedRuleContext(GramaticaParser.RbContext,0)


        def COMMA(self):
            return self.getToken(GramaticaParser.COMMA, 0)

        def WHITESPACE(self):
            return self.getToken(GramaticaParser.WHITESPACE, 0)

        def rc(self):
            return self.getTypedRuleContext(GramaticaParser.RcContext,0)


        def instruccion_i(self):
            return self.getTypedRuleContext(GramaticaParser.Instruccion_iContext,0)


        def inm(self):
            return self.getTypedRuleContext(GramaticaParser.InmContext,0)


        def instruccion_j(self):
            return self.getTypedRuleContext(GramaticaParser.Instruccion_jContext,0)


        def LABEL(self):
            return self.getToken(GramaticaParser.LABEL, 0)

        def COLON(self):
            return self.getToken(GramaticaParser.COLON, 0)

        def DIGIT(self):
            return self.getToken(GramaticaParser.DIGIT, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = GramaticaParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 25
                self.instruccion_r()
                self.state = 26
                self.ra()
                self.state = 27
                self.rb()
                self.state = 28
                self.match(GramaticaParser.COMMA)
                self.state = 29
                self.match(GramaticaParser.WHITESPACE)
                self.state = 30
                self.rc()
                pass

            elif la_ == 2:
                self.state = 32
                self.instruccion_r()
                self.state = 33
                self.ra()
                self.state = 34
                self.rb()
                pass

            elif la_ == 3:
                self.state = 36
                self.instruccion_i()
                self.state = 37
                self.ra()
                self.state = 38
                self.rb()
                self.state = 39
                self.match(GramaticaParser.COMMA)
                self.state = 40
                self.match(GramaticaParser.WHITESPACE)
                self.state = 43
                token = self._input.LA(1)
                if token in [GramaticaParser.DIGIT, GramaticaParser.PAREN_OPEN]:
                    self.state = 41
                    self.inm()

                elif token in [GramaticaParser.LABEL]:
                    self.state = 42
                    self.match(GramaticaParser.LABEL)

                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 4:
                self.state = 45
                self.instruccion_i()
                self.state = 46
                self.ra()
                self.state = 47
                self.inm()
                pass

            elif la_ == 5:
                self.state = 49
                self.instruccion_j()
                self.state = 50
                self.match(GramaticaParser.LABEL)
                pass

            elif la_ == 6:
                self.state = 52
                self.match(GramaticaParser.LABEL)
                self.state = 54
                _la = self._input.LA(1)
                if _la==GramaticaParser.DIGIT:
                    self.state = 53
                    self.match(GramaticaParser.DIGIT)


                self.state = 56
                self.match(GramaticaParser.COLON)
                pass


            self.state = 60
            _la = self._input.LA(1)
            if _la==GramaticaParser.NEWLINE:
                self.state = 59
                self.match(GramaticaParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instruccion_rContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTR_R(self):
            return self.getToken(GramaticaParser.INSTR_R, 0)

        def WHITESPACE(self):
            return self.getToken(GramaticaParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_instruccion_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion_r" ):
                listener.enterInstruccion_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion_r" ):
                listener.exitInstruccion_r(self)




    def instruccion_r(self):

        localctx = GramaticaParser.Instruccion_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(GramaticaParser.INSTR_R)
            self.state = 63
            self.match(GramaticaParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instruccion_iContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTR_I(self):
            return self.getToken(GramaticaParser.INSTR_I, 0)

        def WHITESPACE(self):
            return self.getToken(GramaticaParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_instruccion_i

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion_i" ):
                listener.enterInstruccion_i(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion_i" ):
                listener.exitInstruccion_i(self)




    def instruccion_i(self):

        localctx = GramaticaParser.Instruccion_iContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruccion_i)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(GramaticaParser.INSTR_I)
            self.state = 66
            self.match(GramaticaParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Instruccion_jContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTR_J(self):
            return self.getToken(GramaticaParser.INSTR_J, 0)

        def WHITESPACE(self):
            return self.getToken(GramaticaParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_instruccion_j

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion_j" ):
                listener.enterInstruccion_j(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion_j" ):
                listener.exitInstruccion_j(self)




    def instruccion_j(self):

        localctx = GramaticaParser.Instruccion_jContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruccion_j)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(GramaticaParser.INSTR_J)
            self.state = 69
            self.match(GramaticaParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self):
            return self.getToken(GramaticaParser.REG, 0)

        def COMMA(self):
            return self.getToken(GramaticaParser.COMMA, 0)

        def WHITESPACE(self):
            return self.getToken(GramaticaParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_ra

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRa" ):
                listener.enterRa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRa" ):
                listener.exitRa(self)




    def ra(self):

        localctx = GramaticaParser.RaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GramaticaParser.REG)
            self.state = 72
            self.match(GramaticaParser.COMMA)
            self.state = 73
            self.match(GramaticaParser.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RbContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self):
            return self.getToken(GramaticaParser.REG, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_rb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRb" ):
                listener.enterRb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRb" ):
                listener.exitRb(self)




    def rb(self):

        localctx = GramaticaParser.RbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GramaticaParser.REG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self):
            return self.getToken(GramaticaParser.REG, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_rc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRc" ):
                listener.enterRc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRc" ):
                listener.exitRc(self)




    def rc(self):

        localctx = GramaticaParser.RcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(GramaticaParser.REG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_OPEN(self):
            return self.getToken(GramaticaParser.PAREN_OPEN, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.DIGIT)
            else:
                return self.getToken(GramaticaParser.DIGIT, i)

        def PAREN_CLOSE(self):
            return self.getToken(GramaticaParser.PAREN_CLOSE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_inm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInm" ):
                listener.enterInm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInm" ):
                listener.exitInm(self)




    def inm(self):

        localctx = GramaticaParser.InmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_inm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if _la==GramaticaParser.PAREN_OPEN:
                self.state = 79
                self.match(GramaticaParser.PAREN_OPEN)


            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.match(GramaticaParser.DIGIT)
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GramaticaParser.DIGIT):
                    break

            self.state = 88
            _la = self._input.LA(1)
            if _la==GramaticaParser.PAREN_CLOSE:
                self.state = 87
                self.match(GramaticaParser.PAREN_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





