# Tubes_TBFO
IF2124 - Teori Bahasa Formal dan Otomata

## Terminals
- Identifiers (Variables, Functions, Classes) (lowercase, uppercase, digits, underscore)
- Values
  - Strings (' Abjad; ""; ' Abjad' ' Abjad'; """ """)
  - Numbers (Integers, Decimals)
- Keywords
  - True (Boolean) 
  - False (Boolean)
  - None (Object)
  - and (Logical operator)
  - or (Logical operator)
  - not (Logical operator)
  - is (Identity operator)
  - class (Classes)
  - def (Functions)
  - return (Functions)
  - if (conditional)
  - elif (conditional)
  - else (conditional)
  - while (loops)
  - for (loops)
  - in (loops)
  - break (loops)
  - continue (loops)
  - import (libraries)
  - as (libraries)
  - from (libraries)
  - raise (error handling)
  - with (misc.)
  - pass (misc.)
- Brackets
  - "( )" Parentheses (tuples, order of operations, generator expressions, function calls and other syntax)
  - "[ ]" Square Brackets (mutable data types and for indexing/lookup/slicing)
  - "{ }" Curly Brackets (dictionaries and sets)
 - Operators
  - Arithmetic operators (+, -, *, /, %, **, //)
  - Assignment operators (=, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=)
  - Comparison operators (==, !=, <, >, <=, >=)
  - Logical operators (see keywords)
  - Identity operators (see keywords)
  - Membership operators (in - see keywords)
  - Bitwise operators (&, |, ^, <<, >>, ~)
 - Comments (#)
 - Newline (\n)
 - Indentation (\t)
 - Function output type (Bonus) (->)
 - Block of code indicator (:)
 - Dot operator (. - Access attributes and methods)

## Variables (CFG)
- Simple Values:
  - NonZeroDigit -> 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 1 'Digit' | 2 'Digit' | 3 'Digit' | 4 'Digit' | 5 'Digit' | 6 'Digit' | 7 'Digit' | 8 'Digit' | 9 'Digit'
  - Digit -> 0 | NonZeroDigit
  - NaturalNumber -> Digit | Digit NaturalNumber | Boolean  // MASIH BELOM BENER
  - Integer -> NaturalNumber | -NaturalNumber
  - Decimal -> Integer '.' | Integer '.' NaturalNumber
  - Boolean -> 'True' | 'False' | ComparisonOperation | LogicalOperation
  - NoneType -> 'None' | ComparisonOperation | LogicalOperation
  - Number -> Integer | Decimal | Decimal E Integer | ArithmeticOperation
  - AbjadLowerCase -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | 'a' Abjad | 'b' Abjad | 'c' Abjad | 'd' Abjad | 'e' Abjad | 'f' Abjad | 'g' Abjad | 'h' Abjad | 'i' Abjad | 'j' Abjad | 'k' Abjad | 'l' Abjad | 'm' Abjad | 'n' Abjad | 'o' Abjad | 'p' Abjad | 'q' Abjad | 'r' Abjad | 's' Abjad | 't' Abjad | 'u' Abjad | 'v' Abjad | 'w' Abjad | 'x' Abjad | 'y' Abjad | 'z' Abjad 
  - AbjadUpperCase -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z' | 'A' Abjad | 'B' Abjad | 'C' Abjad | 'D' Abjad | 'E' Abjad | 'F' Abjad | 'G' Abjad | 'H' Abjad | 'I' Abjad | 'J' Abjad | 'K' Abjad | 'L' Abjad | 'M' Abjad | 'N' Abjad | 'O' Abjad | 'P' Abjad | 'Q' Abjad | 'R' Abjad | 'S' Abjad | 'T' Abjad | 'U' Abjad | 'V' Abjad | 'W' Abjad | 'X' Abjad | 'Y' Abjad | 'Z' Abjad 
  - Abjad -> AbjadUpperCase | AbjadLowwerCase
  - AbjadNumber -> Abjad | Number | Abjad Number | Number Abjad
  - UnderScoreIdentifier -> '_' | Abjad '_' AbjadNumber | '_' AbjadNumber | Abjad '_'
  - Identifier -> Epsilon | UnderScoreIdentifier | Abjad
  - Anything -> 
  - String -> '"' Anything '"' | ''' Anything '''
  - Literal -> Numbers | Strings                                  //lowercase, uppercase, digits, underscore
  - Iterable -> 
  - Indentation -> '\t' | Indentation '\t'
  - Epsilon -> 'e'
  - StringLoop -> Epslion | StringLoop ',' String | String
  - NumberLoop -> Epslion | NumberLoop ',' Number | Number
  - AnyType -> List | Tuple | Number | String 
  - SomeType -> Number | String | Tuple
  - Dictionary -> Epsilon | Dictionary ',' SomeType ':' AnyType | SomeType ':' AnyType
  - List -> '[' StringLoop ']' | '[' NumberLoop ']' | '[' List ']' | '[' Tuple ']'
  - Tuple -> '(' StringLoop ')' | '(' NumberLoop ')' 
  - Curly -> '{' Dictionary '}' | '{' StringLoop '}'
  - Bracket -> List | Tuple | Curly

- Expressions:
  - ArithmeticOperator -> + | - | * | / | % | ** | //
  - ArithmeticOperation -> Number ArithmeticOperator Number
  - AssignmentOperator -> = | += | -= | *= | /= | %= | **= | //= | &= | |= | ^= | >>= | <<=
  - AssignmentOperation -> Idenifier AssignmentOperator Literal
  - ComparisonOperator -> == | != | < | > | <= | =>
  - ComparisonOperation -> Atom ComparisonOperator Atom
  - LogicalOperator -> 'and' | 'or' | 'not'
  - LogicalOperation -> Atom LogicalOperator Atom
  - IdentityOperation -> Atom is Atom
  - MembershipOperation -> Atom in Iterable
  - BitwiseOperator -> & | '|' | ^
  - BitwiseOperation -> Integer BitwiseOperator Integer
  - BitshiftOperator -> << | >>
  - BitshiftOperation -> Integer BitshiftOperator NaturalNumber
  - BinaryOperation -> BitwiseOperation | BitshiftOperation | ~BinaryOperation
  - Atom -> Identifier | Literal


- Conditional:
  - ConditionalOperator -> 'if' | 'elif' 
  - ConditionalOperation -> ConditionalOperator Expression ':' Indentation Code |  ConditionalOperator '(' Expression ')' ':' Indentation Code
  - ConditionalElseOperator -> 'else'
  - ConditionalElseOperation -> ConditionalOperator ':' Indentation Code
  - WhileOperator -> 'while'
  - WhileOperation -> WhileOperator Expression ':' Indentation Code |  WhileOperator '(' Expression ')' ':' Indentation Code

- Alias:
    - AsOperator -> 'as'
    - ImportOperator -> 'import'
    - AliasOperation -> ImportOperator Indentifier AsOperator Identifier | ImportOperator Indentifier 

- Code:
    - BreakOperator -> 'break'
    - BreakOperation -> Indentation BreakOperator
    - PassOperator -> 'pas'
    - PassOperration -> Indentation Pass
    - ClassOperation -> 'class' Indentifier ':' Indentation Code
    - InOperation ->  Identifier 'in' List | Number 'in' List | Identifier 'in' String |  Identifier 'in' Tuple | Number 'in' Tuple
    - ForOperation -> 'for' InOperation ':' Indentation Code
    - FromOperation -> 'from' Identifier AliasOperation
    - IsOperator -> Bracket | Boolean | None
    - IsOperation -> IsOperator 'is' IsOperator
    - RaiseOperation -> Indentation 'raise' Identifier '(' String ')'
    - ReturnOperation -> Indentation 'return' Identifier
    - WithOperation -> 'with' Identifier AsOperator Identifier ':' Indentation Code

    

## Variables (CNF)


## REFERENCES
https://www.quackit.com/python/reference/python_3_string_operators.cfm
https://python.swaroopch.com/op_exp.html
https://docs.python.org/3/reference/index.html
