### Challenge description
Welcome to the Index of Planets!

- `nc ch.hackyeaster.com 2403`

### Solution

We get the following prompt after connecting
```
------------  
PLANET INDEX  
  
last update: August 2006  
------------  
1 Mercury  
2 Venus  
3 Earth  
4 Mars  
5 Jupiter  
6 Saturn  
7 Uranus  
8 Neptune  
------------
```

We already notice a few things.
The input is meant to be given 1->8 and the hint seems to refer to Pluto no longer being a planet in 08/2006.

After trying some inputs, with larger inputs > 8 it always returns `Invalid index`

The most interesting output comes from 0:
```
cat: /usr/src/planetindex/planet-0.txt: No such file or directory
```

If we try negative numbers, we see that it circles back and get a weird problem when trying to get to index 9.

```
Enter the index of the planet > -65527  
Invalid index checksum (i%10 + 7 <= 0)! Quitting.
```

We try to get around the invalid index checksum by doubling the value

```
Enter the index of the planet > -131063  
------------  
Pluto, roses are red,  
here's your flag: he2024{plut0_41nt_n0_plan3t_n0_m0r3}
```