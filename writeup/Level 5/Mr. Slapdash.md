### Challenge description
I found Mr. Slapdash's notes file where he keeps track of his credit cards.

He seems to have written down the CVV numbers in some sort of encoding. Can you crack it?

```
4929 2428 3716 8341   11/27  visa  
5209 2330 7086 6970   02/28  mastercard  
3793 568767 90378     03/28  amex  
6011 3798 6234 9679   07/27  discover  
  
cvv:  
4/1/3 3/2/5 2/2/2  
3/2/3 4/4/1 1/3/2   
1/4/4 4/4/1 4/1/4 1/1/1  
2/3/3 2/2/3 3/1/1  
```

### Solution
The CVVs are encoded with coordinates
row / column / index

162
897
1914
833

he2024{1628971914833}