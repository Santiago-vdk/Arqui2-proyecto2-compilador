import sys
from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(msg + " line: " + str(line) + " column: " + str(column))
        print("SYNTAX ERROR, exiting...")
        sys.exit()
