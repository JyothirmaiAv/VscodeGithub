# Caesar Cipher

A Python implementation of the classic Caesar cipher, used to encrypt 
and decrypt text by shifting each letter a fixed number of places in 
the alphabet.

## What it does
- Encrypts text by shifting each letter forward by a chosen amount (1–25)
- Decrypts text by shifting letters back by the same amount
- Preserves uppercase/lowercase and leaves non-letter characters (spaces, punctuation) unchanged
- Validates that the shift value is a valid integer between 1 and 25

## How it works
- `caesar()` is the core function: it builds a shifted version of the alphabet and uses `str.maketrans()` to map each letter to its shifted counterpart
- `encrypt()` and `decrypt()` are simple wrapper functions that call `caesar()` with the right direction

## Concepts used
Functions, default arguments, string methods (`str.maketrans`, `str.translate`), input validation, string slicing

## Example
```python
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
# Output: Courage is found in unlikely places.
```
