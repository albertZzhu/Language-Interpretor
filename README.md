# Language Interpretor
 This project is a language interpreter for the language created by The Ohio State University called Quandary. Quandary is an object oriented language with grammar similar to some other high level languages like Python and Java.
### This is the example code for quandary language:
 
```
program
	add(ref a, b) begin
		a = a+b;
		ref n;
		b = share n;
	endfunc
begin
	ref x;
	x = new class;
	x = 1;
	ref y;
	y = new class;
	y = 1+x;
	begin add(x, y);
	output x;
end
```

### This segment of code would have the following as input:

```
0 1 2 3 4 5 6 7 8 9
```

### And It would have the following output:

```
3
```

### To start use this interpreter, you would need the following command:

```
python Main.py #Yourcode.code #Yourdata.data
```

### This is the parse structure of Quandary language:

```
<prog> ::= program <decl-seq> begin <stmt-seq> end | program begin <stmt-seq> end <decl-seq> ::= <decl> | <decl><decl-seq> | <func-decl> | <func-decl><decl-seq> <stmt-seq> ::= <stmt> | <stmt><stmt-seq>
<decl> ::= <decl-int> | <decl-class>
<decl-int> ::= int <id-list> ;
<decl-class> ::= ref <id-list> ;
<id-list> ::= id | id , <id-list>
<func-decl> ::= id ( ref <formals> ) begin <stmt-seq> endfunc <formals> ::= id | id , <formals>
<stmt> ::= <assign> | <if> | <loop> | <in> | <out> | <decl> | <func-call> <func-call> ::= begin id ( <formals> ) ;
<assign> ::= id = <expr> ; | id = new class; | id = share id ;
<in> ::= input id ;
<out> ::= output <expr> ;
<if> ::= if <cond> then <stmt-seq> endif
| if <cond> then <stmt-seq> else <stmt-seq> endif <loop> ::= while <cond> begin <stmt-seq> endwhile <cond> ::= <cmpr> | ! ( <cond> )
| <cmpr> or <cond>
<cmpr> ::= <expr> == <expr> | <expr> < <expr>
| <expr> <= <expr>
<expr> ::= <term> | <term> + <expr> | <term> – <expr> <term> ::= <factor> | <factor> * <term>
<factor> ::= id | const | ( <expr> )
```
