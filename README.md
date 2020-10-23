# Regex engine
This repository contains a regex engine that can handle basic regex syntax, including literals (a, b, c, etc.), wild-card (.), and metacharacters (?, *, +, ^, $).

The program takes in one string (two elements to be compared must be separated by `|`). On the left of the delimiter `|` is the regular expression, and on the right is the string that is being compared to that regular expression.
In the output there is a boolean representing whether the string matches the regex. 

## Get started!
- download the repository
- run the program in the command-line
```
NumericMatrixProcessor > python main.py
```
### Sample usage
**Usage of `$` and `^`:**
```
Input:    '^app|apple'           Output: True
Input:     'le$|apple'           Output: True
Input:      '^a|apple'           Output: True
Input:      '.$|apple'           Output: True
Input:  'apple$|tasty apple'     Output: True
Input:  '^apple|apple pie'       Output: True
Input: '^apple$|apple'           Output: True
Input: '^apple$|tasty apple'     Output: False
Input: '^apple$|apple pie'       Output: False
Input:    'app$|apple'           Output: False
Input:     '^le|apple'           Output: False
```
**Usage of `?` and `*`:**
```
Input: 'colou?r|color'       Output: True
Input: 'colou?r|colour'      Output: True
Input: 'colou?r|colouur'     Output: False
Input: 'colou*r|color'       Output: True
Input: 'colou*r|colour'      Output: True
Input: 'colou*r|colouur'     Output: True
Input:  'col.*r|color'       Output: True
Input:  'col.*r|colour'      Output: True
Input:  'col.*r|colr'        Output: True
Input:  'col.*r|collar'      Output: True
Input: 'col.*r$|colors'      Output: False
```
**Usage of a backward slash (the escape symbol):**
```
Input:      '\.$|end.'              Output: True
Input:     '3\+3|3+3=6'             Output: True
Input:       '\?|Is this working?'  Output: True
Input:       '\\|\'                 Output: True
Input: 'colou\?r|color'             Output: False
Input: 'colou\?r|colour'            Output: False
```
