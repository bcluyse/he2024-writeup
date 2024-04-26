### Challenge description

Bunny Bob grinned from ear to ear, as he told the story of his new idea. "_ROT. It's just ROT. Nothing more. But get this: Each letter is rotted individually, and I am using different numbers for each letter!_".

Fred Rabbit wasn't impressed. "_Hmm. Interesting. How do you communicate the needed individual rotations to the recipient?_".  
"_Oh. That_", Bob smiled. "_You could say it's a piece of cake._"

Here's the encoded flag:

```
ii35;6Ykf|h~j8adgf7ve5uuiw37wflaj}x`9rbgj|7  
```

### Solution

We can reverse engineer the first ROTs because we know the he2024 prefix. We try with ROT47 since that supports ASCII.

i -> h  = -1
i -> e = -4
3-> 2 = -1
5-> 0 = -5
; -> 2 = -9
6-> 4 = -2

It seems like these are the digits of pi. (the hint).
I have written a script in .src/4/piece-of-cake.py which decrypts the flag.

he2024XThat_wa5_a_b1t_1rrat10nal_but_0kaaay
