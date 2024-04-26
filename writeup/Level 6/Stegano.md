### Challenge description

My friend sent me this image, but I don't get the message.

Never heard of this stenago thing.

 [stenago.png](https://24.hackyeaster.com/app/rest/user/challenge/25/file)

### Solution

This challenge is obviously steganography based.
Let us first check with the tool aperisolve and see if there is anything obvious going on.

The `zsteg` output does not really lead to anything.
We can see weird patterns in the following bit planes though at the top.

Red: 2
![[stenago-red-2.png]]
Green: 3
![[stenago-green-3.png]]
Blue: 4
![[stenago-blue-4.png]]

https://georgeom.net/StegOnline/extract 
Can help us extract the bit planes and we immediately get the flag
he2024{h1d1ng_stuff_1n_p1x3ls}