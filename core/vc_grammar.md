program -> ( func-decl | var-decl )*
// declarations
func-decl -> type identifier para-list compound-stmt
var-decl -> type init-declarator-list ";"
init-declarator-list-> init-declarator ( "," init-declarator )*
init-declarator -> declarator ( "=" initialiser )?
declarator -> identifier
| identifier "[" INTLITERAL? "]"
initialiser -> expr
| "{" expr ( "," expr )* "}"
// primitive types
type -> void | boolean | int | float
// identifiers
identifier -> ID
// statements
compound-stmt -> "{" var-decl* stmt* "}"
stmt -> compound-stmt
| if-stmt
| for-stmt
| while-stmt
| break-stmt
| continue-stmt
| return-stmt
| expr-stmt
if-stmt -> if "(" expr ")" stmt ( else stmt )?for-stmt -> for "(" expr? ";" expr? ";" expr? ")" stmt
while-stmt -> while "(" expr ")" stmt
break-stmt -> break ";"
continue-stmt -> continue ";"
return-stmt -> return expr? ";"
expr-stmt -> expr? ";"
// expressions
expr -> assignment-expr
assignment-expr -> ( cond-or-expr "=" )* cond-or-expr
cond-or-expr -> cond-and-expr
| cond-or-expr "||" cond-and-expr
cond-and-expr -> equality-expr
| cond-and-expr "&&" equality-expr
equality-expr -> rel-expr
| equality-expr "==" rel-expr
| equality-expr "!=" rel-expr
rel-expr -> additive-expr
| rel-expr "<" additive-expr
| rel-expr "<=" additive-expr
| rel-expr ">" additive-expr
| rel-expr ">=" additive-expr
additive-expr -> multiplicative-expr
| additive-expr "+" multiplicative-expr
| additive-expr "-" multiplicative-expr
multiplicative-expr -> unary-expr
| multiplicative-expr "*" unary-expr
| multiplicative-expr "/" unary-expr
unary-expr -> "+" unary-expr
| "-" unary-expr
| "!" unary-expr
| primary-expr
primary-expr -> identifier arg-list?
| identifier "[" expr "]"
| "(" expr ")"
| INTLITERAL
| FLOATLITERAL
| BOOLLITERAL
| STRINGLITERAL
// parameters
para-list -> "(" proper-para-list? ")"
proper-para-list -> para-decl ( "," para-decl )*
para-decl -> type declarator
arg-list -> "(" proper-arg-list? ")"
proper-arg-list -> arg ( "," arg )*
arg -> expr