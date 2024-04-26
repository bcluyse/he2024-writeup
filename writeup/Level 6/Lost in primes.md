### Challenge description
One of our Prime eggs is lost.

It was last seen at [factordb.com](http://factordb.com/).

The only thing we know is that it has not yet been proven that it is really prime, and has more than 27000 digits.

🚩 Flag

- slightly different flag prefix this time, `HE24`!
    
- format: `HE24{sample_flag}`
    

 [leaked_part.png](https://24.hackyeaster.com/app/rest/user/challenge/26/file)

### Solution

- The leaked part looks like binary, so we can filter the primes based on that.
- FactorDB provides search endpoints
	- mindigits = 27000
	- not yet proven, so we should search on probably prime or unknown

The idea is to create a script which
- fetches numbers from 27000 digits onwards
- only U/PP
- Only keep 'binary' representations in decimal.

With the output, I would then assume binary -> UTF-8

#### Probably Prime?
After searching with the script in [[.src/6/lost_in_primes.py]]
I found the following candidate which looks a lot like the image.

http://factordb.com/index.php?showid=1100000004627024178

If we enter the binary into the 
https://www.dcode.fr/binary-image

We get the following image:

![[.src/files/dcode-image.png]]

and the following flag
HE24{fun_with_pr1mes}