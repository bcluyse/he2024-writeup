### Challenge description

I invented a new encoding: _Space64_.

How do you like it?

 [space64.txt](https://24.hackyeaster.com/app/rest/user/challenge/12/file)

### Solution

This text file obviously contains a base64 encoded file.
If we decode it, we get what seems to be a png file based on the headers.

However, the file does not seem to be a proper PNG.
We can try to replace all the following letters.

In the code given in [[space64.py]], we go over all available characters in base64 [A-Za-z+/].
The combination + / seems to give the image.

![[space64.png]]

he2024{l0st_1n_wh1t3sp4c3}
