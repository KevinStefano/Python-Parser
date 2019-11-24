# Tubes_TBFO
IF2124 - Teori Bahasa Formal dan Otomata

## Terminals
- Identifiers (Variables, Functions, Classes) (lowercase, uppercase, digits, underscore)
- Values
  - Strings (''; ""; ''' '''; """ """)
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
  - NonZeroDigit -> 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
  - Digit -> 0 | NonZeroDigit
  - NaturalNumber -> Digit | Digit NaturalNumber | Boolean  // MASIH BELOM BENER
  - Integer -> NaturalNumber | -NaturalNumber
  - Decimal -> Integer . | Integer . NaturalNumber
  - Boolean -> 'True' | 'False' | ComparisonOperation | LogicalOperation
  - Number -> Integer | Decimal | Decimal E Integer | ArithmeticOperation
  - String -> 
  - Literal -> Numbers | Strings
  - Identifier ->
  - Iterable ->
  - Atom -> Identifier | Literal
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
  
## Variables (CNF)


## REFERENCES
https://www.quackit.com/python/reference/python_3_string_operators.cfm
https://python.swaroopch.com/op_exp.html
https://docs.python.org/3/reference/index.html
