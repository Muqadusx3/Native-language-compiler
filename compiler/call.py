
from lexical_analyzer import *
from rdp import SymbolTable,Number,Interpreter,Context,Parser



stm = SymbolTable()
stm.set("NULL" , Number(0))
stm.set("FALSE", Number(0))
stm.set("TRUE" , Number(1))

def run(fn, text):
  # Generate tokens
  lexer = Lexer(fn, text)
  tokens, error = lexer.make_tokens()
  if error:
    return None, error, None, None,None
  global va
  # Generate AST
  parser = Parser(tokens)
  ast = parser.parse()
  va= False
  if ast.error:
    return None, ast.error, None, None,None
  else:
    va = True
  
  # Run program
  interpreter = Interpreter()
  interpreter.parser_list=[]
  context = Context('<program>')
  context.symbol_table = stm
  result = interpreter.visit(ast.node, context)

  return result.value, result.error, tokens, interpreter.parser_list,stm.symbols

def valid():
  return va