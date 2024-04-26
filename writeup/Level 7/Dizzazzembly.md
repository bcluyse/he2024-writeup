### Challenge description

Have a look at this dizzazzembly.

When entering the flag, the corresponding program did output:

```
da.,.0w`-vv[evv[luj^&dUZ'pp*pp)cXb'ds  
```

 [code.txt](https://24.hackyeaster.com/app/rest/user/challenge/28/file)

### Solution
This is python byte code.

First, we reconstruct the python byte code.
I have done this manually with some ChatGPT assistance since codes like decompyle/uncompyle did not work out of the box.
The ChatGPT made quite some mistakes but it was easy to refactor to the correct output.

We could create the byte code output with:
```bash
python -m dis dizzazzembly.py > files/dizzazzembly_mine.txt
```

The reversed version can be found in HackyEaster.2024/src/7/reazzembly.py.

When we pass the encrypted message, we get the flag:
he2024{d1zz_izz_pyth0n_d1zz4zz3mbl1n}
