# Writeup for picoCTF 2019 : vault-door-5
## Steps:
In this one there was a custom url encoder and base64 encoder involved. In the `checkPassword` function, the `expected` string is both url encoded and base64 encoded, so if we develop the decoders for both and decode the expected string in reverse order, we'll get the flag as done in the java file.

## Flag:
``` picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095} ```
