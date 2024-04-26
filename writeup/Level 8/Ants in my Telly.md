### Challenge description
Tired of fuzzy, soft, nice things, the bunnies are watching a nature video about spiders and ants.

But what's _that_?

 [ants_in_my_telly.mp4](https://24.hackyeaster.com/app/rest/user/challenge/35/file)

### Solution

##### Metadata
Running `exiftool` on the file, gives some weird metadata in the descrption
`waltzb_dnymph{for}quickj?gsvex`

This seems to be an example of a pangram
Waltz bad nymph for quick jigs vex.

This might prove useful later on in the challenge.

##### Image

If we take the average of all the frames, we can very clearly see that there are pixels which are never changing. This is already quite obvious from the video.

So we want to use this as a mask. 
The implementation for this mask can be found at src/8/ants-generate-mask.py

![[average_cropped.png]]

If we use the mask on the pangram, we do not really get any useful input. 

```
knyaydjwrmaq}nsrmkur{knsnrtx_{rkp}r{gronrpr_cw}nsr{aazv
```

So what if we check with our known plaintext he2024?
We see h comes at index 22 in the mask and at index 12 in the pangram. So we have room for 10 characters.
Let's add the digits 0123456789

```
he9197{0_w1nd8r_why_th8r8_just_had_to_b8_a_sp0der_t11?}
```

After some reverse engineering, we can find the correct pangram and the correct flag.

```
1028456432waltzb_dnymph{for}quickj?gsvex

he2024{1_w0nd3r_why_th3r3_just_had_to_b3_a_sp1der_t00?}
```