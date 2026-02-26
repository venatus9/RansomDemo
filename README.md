# RansomDemo
A demonstrative example of a ransomware program built in python.

When ran the program targets a **single file** called `flag.txt`.

This program expects a **remote flask endpoint** to recieve the generated private key, if it cannot reach one, no files are encrypted (wouldn't be much of a ransom otherwise).
