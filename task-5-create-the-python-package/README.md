# Foobar

Counting function intended for counting single characters in words.
It works with string types and text files.
To do this, you need to use the appropriate arguments in the command line. 
Examples are given below


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this function.

```bash
pip install counting_function_momontd
```

## Usage

```python

from counting_function_momontd import count_single_characters


# returns '2'

count_single_characters.pluralize('aabcccdss')


# returns '4'

count_single_characters.pluralize('gggbvcd')


# returns '5'

count_single_characters.singularize('abcde')



```