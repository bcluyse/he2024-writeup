### Challenge description

This time, Bunny Bob was lost in thoughts. _"I cracked your code"_, the young bunny from before told him. _"Is this using the same number again? It's irrational to think this would work twice."_

_"No"_, Bob replied. _"It's not that irrational at all, when you have a closer look."_

_"But my approach doesn't work here at all!"_ Bunny Bob sighed.

_"It's the same mechanic. Just don't start at the beginning. Start right after every hacker's birthday."_

His young friend looked at him quizzically and hopped away, none the wiser.

Here's the encoded flag:

```
he876:|I94kcxk6uohyp9t4cn}ti:vtcir7foowg8tbk8sfy~4166~  
```

### Solution

From the description we can derive
- same ROT approach as in [[Piece of Cake]]
- different irrational number from pi and we do not start from the beginning
- prefix is 01011970

We find the known part of the key for he2024{
0067461

If we search in digit finders (http://www.subidiom.com/pi/pi.asp) for the first occurrence of the following pattern

010119700067461

We can find the following digits as part of E

0101197000674612947443578958611408777414804710387714755756388118445082180751150269761415002213210142

If we plug that into the code, we get the flag

he2024{G00d_th1ng_th3s3_numb3rs_ar3_not_1mag1nary....}