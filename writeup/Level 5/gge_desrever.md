### Challenge description

?ssem siht elgnatnu ot em pleh uoy naC .desrever tog ti dna gge ym deppord I !pleH

 [gnp.galf](https://24.hackyeaster.com/app/rest/user/challenge/20

### Solution

It obviously looks like the file is reversed in some way.
After looking at the bytes in xxd there does not seem to be a straightforward .PNG anywhere.

However, if we reverse the full binary in cyberchef, the file ends with

GNP.

So if we reverse the file at that moment and render the output we get the flag.

![[gge_desrever_recipe.png]]

![[egg_reversed.png]]

After scanning, it seems like we need 1 more level of reversing

```
➜  files zbarimg egg_reversed.png | rev  
he2024{enough_reversing_for_now:)}:edoC-RQ
```

