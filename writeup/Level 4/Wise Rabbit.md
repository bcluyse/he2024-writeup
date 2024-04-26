### Challenge description
After a lengthy slumber spanning nine years, Wise Rabbit finally resurfaces on Hacky Easter!

_A simple number guessing,_  
_might be a little stressing,_  
_but with a simple tweak,_  
_you'll find the egg you seek._

[Wise Rabbit's Page](http://ch.hackyeaster.com:2405/)

### Solution

We see the code basically wants us to give 13037 but it is checking also that we are passing at least 6 characters with strlen.
Immediately, it seems like we should pass 1337 as we are leet.

- 13037 -> too long
- 13037.0 -> invalid character
- 130370e-1 = flag

he2024{p33_4g3_p33_c0d3_cr4ck3d!}