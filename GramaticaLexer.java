// Generated from Gramatica.g4 by ANTLR 4.5.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GramaticaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.5.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		REG=1, INSTR_R=2, INSTR_I=3, INSTR_J=4, LABEL=5, DIGIT=6, COLON=7, COMMA=8, 
		WHITESPACE=9, PAREN_OPEN=10, PAREN_CLOSE=11, NEWLINE=12;
	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"LOWERCASE", "UPPERCASE", "REG", "INSTR_R", "INSTR_I", "INSTR_J", "LABEL", 
		"DIGIT", "COLON", "COMMA", "WHITESPACE", "PAREN_OPEN", "PAREN_CLOSE", 
		"NEWLINE"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "REG", "INSTR_R", "INSTR_I", "INSTR_J", "LABEL", "DIGIT", "COLON", 
		"COMMA", "WHITESPACE", "PAREN_OPEN", "PAREN_CLOSE", "NEWLINE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public GramaticaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Gramatica.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16\u00ac\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4h\n\4\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5{\n\5"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008c"+
		"\n\6\3\7\3\7\3\b\3\b\6\b\u0092\n\b\r\b\16\b\u0093\3\b\5\b\u0097\n\b\3"+
		"\t\6\t\u009a\n\t\r\t\16\t\u009b\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16"+
		"\3\16\3\17\6\17\u00a9\n\17\r\17\16\17\u00aa\2\2\20\3\2\5\2\7\3\t\4\13"+
		"\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\3\2\6\3\2c|\3\2C\\\3"+
		"\2\62;\4\2\f\f\17\17\u00cf\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3"+
		"\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2"+
		"\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7g\3"+
		"\2\2\2\tz\3\2\2\2\13\u008b\3\2\2\2\r\u008d\3\2\2\2\17\u0091\3\2\2\2\21"+
		"\u0099\3\2\2\2\23\u009d\3\2\2\2\25\u009f\3\2\2\2\27\u00a1\3\2\2\2\31\u00a3"+
		"\3\2\2\2\33\u00a5\3\2\2\2\35\u00a8\3\2\2\2\37 \t\2\2\2 \4\3\2\2\2!\"\t"+
		"\3\2\2\"\6\3\2\2\2#$\7&\2\2$h\7\62\2\2%&\7&\2\2&h\7\63\2\2\'(\7&\2\2("+
		"h\7\64\2\2)*\7&\2\2*h\7\65\2\2+,\7&\2\2,h\7\66\2\2-.\7&\2\2.h\7\67\2\2"+
		"/\60\7&\2\2\60h\78\2\2\61\62\7&\2\2\62h\79\2\2\63\64\7&\2\2\64h\7:\2\2"+
		"\65\66\7&\2\2\66h\7;\2\2\678\7&\2\289\7\63\2\29h\7\62\2\2:;\7&\2\2;<\7"+
		"\63\2\2<h\7\63\2\2=>\7&\2\2>?\7\63\2\2?h\7\64\2\2@A\7&\2\2AB\7\63\2\2"+
		"Bh\7\65\2\2CD\7&\2\2DE\7\63\2\2Eh\7\66\2\2FG\7&\2\2GH\7\63\2\2Hh\7\67"+
		"\2\2IJ\7&\2\2JK\7\63\2\2Kh\78\2\2LM\7&\2\2MN\7\63\2\2Nh\79\2\2OP\7&\2"+
		"\2PQ\7\63\2\2Qh\7:\2\2RS\7&\2\2ST\7\63\2\2Th\7;\2\2UV\7&\2\2VW\7\64\2"+
		"\2Wh\7\62\2\2XY\7&\2\2YZ\7\64\2\2Zh\7\63\2\2[\\\7&\2\2\\]\7\64\2\2]h\7"+
		"\64\2\2^_\7&\2\2_`\7\64\2\2`h\7\65\2\2ab\7&\2\2bc\7\64\2\2ch\7\66\2\2"+
		"de\7&\2\2ef\7\64\2\2fh\7\67\2\2g#\3\2\2\2g%\3\2\2\2g\'\3\2\2\2g)\3\2\2"+
		"\2g+\3\2\2\2g-\3\2\2\2g/\3\2\2\2g\61\3\2\2\2g\63\3\2\2\2g\65\3\2\2\2g"+
		"\67\3\2\2\2g:\3\2\2\2g=\3\2\2\2g@\3\2\2\2gC\3\2\2\2gF\3\2\2\2gI\3\2\2"+
		"\2gL\3\2\2\2gO\3\2\2\2gR\3\2\2\2gU\3\2\2\2gX\3\2\2\2g[\3\2\2\2g^\3\2\2"+
		"\2ga\3\2\2\2gd\3\2\2\2h\b\3\2\2\2ij\7c\2\2jk\7f\2\2k{\7f\2\2lm\7u\2\2"+
		"mn\7w\2\2n{\7d\2\2op\7o\2\2pq\7w\2\2qr\7n\2\2r{\7v\2\2st\7u\2\2t{\7d\2"+
		"\2uv\7n\2\2v{\7d\2\2wx\7o\2\2xy\7q\2\2y{\7x\2\2zi\3\2\2\2zl\3\2\2\2zo"+
		"\3\2\2\2zs\3\2\2\2zu\3\2\2\2zw\3\2\2\2{\n\3\2\2\2|}\7c\2\2}~\7f\2\2~\177"+
		"\7f\2\2\177\u008c\7k\2\2\u0080\u0081\7u\2\2\u0081\u0082\7w\2\2\u0082\u0083"+
		"\7d\2\2\u0083\u008c\7k\2\2\u0084\u0085\7d\2\2\u0085\u0086\7g\2\2\u0086"+
		"\u008c\7s\2\2\u0087\u0088\7o\2\2\u0088\u0089\7q\2\2\u0089\u008a\7x\2\2"+
		"\u008a\u008c\7k\2\2\u008b|\3\2\2\2\u008b\u0080\3\2\2\2\u008b\u0084\3\2"+
		"\2\2\u008b\u0087\3\2\2\2\u008c\f\3\2\2\2\u008d\u008e\7l\2\2\u008e\16\3"+
		"\2\2\2\u008f\u0092\5\3\2\2\u0090\u0092\5\5\3\2\u0091\u008f\3\2\2\2\u0091"+
		"\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2"+
		"\2\2\u0094\u0096\3\2\2\2\u0095\u0097\5\21\t\2\u0096\u0095\3\2\2\2\u0096"+
		"\u0097\3\2\2\2\u0097\20\3\2\2\2\u0098\u009a\t\4\2\2\u0099\u0098\3\2\2"+
		"\2\u009a\u009b\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\22"+
		"\3\2\2\2\u009d\u009e\7<\2\2\u009e\24\3\2\2\2\u009f\u00a0\7.\2\2\u00a0"+
		"\26\3\2\2\2\u00a1\u00a2\7\"\2\2\u00a2\30\3\2\2\2\u00a3\u00a4\7*\2\2\u00a4"+
		"\32\3\2\2\2\u00a5\u00a6\7+\2\2\u00a6\34\3\2\2\2\u00a7\u00a9\t\5\2\2\u00a8"+
		"\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2"+
		"\2\2\u00ab\36\3\2\2\2\13\2gz\u008b\u0091\u0093\u0096\u009b\u00aa\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}