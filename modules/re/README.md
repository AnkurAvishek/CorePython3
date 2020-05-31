# Lib/re.py

* Pattern and string (support) : Unicode string or 8-bit string
    * cannot be mixed
    * when subsituting : both pattern and search string, same type(Unicode/8-bit)

* Regex use \ to indicate special forms.
    * \ can be searched using \\

* invalid escape sequence generate *DepricatedWaring*, in future *SyntaxError*

    * solution: use raw string
    * **str(r'rawstring')**
    * ex: r"\n"

# Regular Expression Syntax

A regular expression specifies a set of string that matches it.

Funcition checks if a particular string matches a given regular expression
* Simple character match
    * ex. 'A', 'a', '0', 'test' etc. -> exact match

* All Metacharacters
[ . ^ $ * + ? { } [ ] \ | ( )]

* . -> any character except new line;
    * to match .  use '\.'
    * if DOTALL flag -> matches new line also 
* ^ -> negate or beginning of string
    * MULTILINE mode -> matches immediately after new line
* $ -> end of string
    * MULTILINE -> before newline
* \* -> 0 or more repetition
* \+ ->  1 or more repetition
* { } -> exact Number {3}, {3,4},-> range of character repetition
    * a{3-5} -> 'aaaaa'
    * a{3-5}? -> 'aaa' -> ? -> match few repetions
* [ ] -> character set
    * [(+*)] -> sepecial character looses special meaning inside set.
* \ -> escape sequence ('\.', '\*', '\?')
* [^] -> negate character
* | -> either or 
* ( ) -> group
    * (...) -> whatever regex is inside parenthsis
    * (?...) -> does not create a new group
    * (?:...) -> non capturing 
    * (?#...) -> A comment
* \d -> [0-9]
* \D -> [^0-9]
* \w -> ([a-z],[A-Z],[0-9], _)
* \W -> (^[a-z],^[A-Z],^[0-9], ^_)
* \s -> white space(space, tab, newline)
* \S -> not white space
* \b -> word boundry r'ha haha' -> \bha\b -> matches **ha** haha
* \B -> not a word boundry 
* \Z -> matchs only at end of string

* greedy qualifiers
    * '*', '+', '?' -> match as much text as possible
* Repetition Qualifiers
    * ex. (*, +, ?, {m,n})
    * cannot be directly nested.
    * avoids ambiguity with non-greedy modifier suffix ?
    * (?:a{6})* matches nay mutiple of six 'a' characters

(more reference)[https://docs.python.org/3/library/re.html#regular-expression-syntax]


# Module Contents

## flags
re.A, re.ASCII
re.DEBUG
re.I, re.IGNORECASE
re.L, re.LOCALE
re.M, re.MULTILINE
re.S, re.DOTALL
re.X, re.VERBOSE


## re.compile(pattern, flags=0)

compile regex pattern to regex object. Efficient if same expression is used multiple times
* cahed - re.purge() - clear cache

```
prog = re.compile(pattern)
result = prog.match(string)

```
alternate

```
result = re.match(pattern, string)
```
## re.search(patten, string, flags=0)

* first location of regex patteren
* retuns match object
* None - if no Match

## re.match(pattern, string, flags=0)
* zero or more characters match at beginning of string enen in MULTILINE(not at beginning or each line)
* return Match object 
* None if no match
* re.search() - match anywhere

## re.fullmatch(pattern, string, flags=0)
* whole string match -> returns match object
* None 

## re.split(pattern, string, maxsplit=0, flags=0)
* split string by occurance of pattern.
* if maxsplit is non zero reminder is returned as final string.

```
re.split('a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```

## re.findall(patten, string, flags=0)
* returns all non overlapping matches
* string is scanned left-to-right
* matchs are returned in the order found

## re.finditer(patten, string, flags=0)
* returns an iterator yielding match objects over all non-overlapping matches

## re.sub(pattern, repl, string, count=0, flags=0)
* return the string obtained by replacin the leftmost non-overlapping occurances of pattern in string.

## re.subn(patten, repl, string, count=0, flags=0)
* same as sub(), but multiple substitution.
* returns tuple(new_string, number_of_subs_made)

## re.escape(pattern)
* Escape special character in pattern. 

```
print(re.escape('http://www.python.org'))
http://www\.python\.org
```
## re.purge()
* clear regual expression cache

## exception  re.error(msg, pattern=None, pos=None)
* Exception raised when a string passed to one of the functions here is not a valid regular expression


# Regular Expression Objects.

Compiled regular expression objects support the following methods and attributes:

### Pattern.search(string[, pos[, endpos]])
```
pattern = re.compile("d")
pattern.search("dog")     # Match at index 0
<re.Match object; span=(0, 1), match='d'>
pattern.search("dog", 1)  # No match; search doesn't include the "d"
```

### Pattern.match(string[, pos[, endpos]])
```
pattern = re.compile("o")
pattern.match("dog")      # No match as "o" is not at the start of "dog".
pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
<re.Match object; span=(1, 2), match='o'>
```
### Pattern.fullmatch(string[, pos[, endpos]])
### Pattern.split(string, maxsplit=0)
### Pattern.findall(string[, pos[, endpos]])
### Pattern.finditer(string[, pos[, endpos]])
### Pattern.sub(repl, string, count=0)
### Pattern.subn(repl, string, count=0)
    
### Pattern.flags
### Pattern.groups
### Pattern.groupindex
### Pattern.pattern

# Match Objects
* match object have boolen value of true. 
* No Match None

```
match = re.search(pattern, string)
if match:
    process(match)
```
### Match.expand(template)
### Match.group([group1, ...])
```
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match
'Isaac Newton'
m.group(1)       # The first parenthesized subgroup.
'Isaac'
m.group(2)       # The second parenthesized subgroup.
'Newton'
m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')
```

### Match.__getitem__(g)
```
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m[0]       # The entire match
'Isaac Newton'
m[1]       # The first parenthesized subgroup.
'Isaac'
m[2]       # The second parenthesized subgroup.
'Newton'
```

### Match.groups(default=None)
* Return a tuple containing all the subgroups of the match
```
m = re.match(r"(\d+)\.(\d+)", "24.1632")
m.groups()
('24', '1632')
```

### Match.groupdict(default=None)
```
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.groupdict()
{'first_name': 'Malcolm', 'last
```
 
### Match.start([group])
### Match.end([group])

```
m.string[m.start(g):m.end(g)]

email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
email[:m.start()] + email[m.end():]
'tony@tiger.net'
```

### Match.span([group])¶
### Match.pos
### Match.endpos
### Match.lastindex
### Match.lastgroup
### Match.re
* The regular expression object
