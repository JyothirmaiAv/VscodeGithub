

 simple Python program that encrypts a word using the Caesar Cipher technique.

## Description

This script shifts each letter in a word by a specified number of positions in the alphabet.

For example, with a shift of **3**:

```text
a → d
b → e
c → f
...
```

## Code

```python
a = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(word, shift):
    encrypt = ''
    for letter in word:
        position = a.index(letter)
        encrypt += a[position + shift]
    return encrypt

word = 'gvlqef'
print(encrypt(word, 3))
```

## How It Works

1. Define the alphabet.
2. Loop through each character in the input word.
3. Find the character's position in the alphabet.
4. Shift the position by the specified amount.
5. Append the new character to the encrypted string.
6. Return the encrypted result.

## Example

Input:

```python
word = "abc"
shift = 3
```

Output:

```text
def
```

## Usage

Run the script:

```bash
python cipher.py
```

## Limitations

- Only works with lowercase English letters (`a-z`).
- Does not handle spaces, numbers, or special characters.
- Large shift values may cause an `IndexError`.

## Possible Improvements

- Support uppercase letters.
- Support spaces and punctuation.
- Use modulo (`%`) arithmetic to handle wrap-around.

Example:

```python
encrypt += a[(position + shift) % len(a)]
```

This allows:

```text
x → a
y → b
z → c
```

## Author

Created as a beginner Python project to understand:
- Functions
- String manipulation
- Loops
- Caesar Cipher encryption
