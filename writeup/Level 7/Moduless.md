### Challenge description
Can you decrypt me even without the modulus?

 [problem.py](https://24.hackyeaster.com/app/rest/user/challenge/29/file

### Solution

We know
- e: public exponent
- d: private exponent
- n-q
- n-p
- C: ciphertext

We need to figure out n because without the modulus we cannot reconstruct the message.

hint1 = n - p = pq - p = p(q - 1)
hint2 = n - q = pq - q = q(p - 1)

First guess:
Let's have a look at the factorization database factordb.com.
We know p and q have to be prime, maybe the database might contain certain values.

[Hint 1](http://factordb.com/index.php?query=17061347780794249474937241232210067248853992326832612618246691021883473946134655677687441412157857703606444858129229798729181511999941417079248816916398800254158380205975686822877683332947748593883879973137797066913439129505904185975901786363274357224292820647481353241115812182163209817605574692194107051614650879245007286513127155460653132782119052901592516408114681455884212579226838379050354351979274017290886704282949858854855220545880052711872903284127358620618442660935241175277762438290440049748381402411449900120675924310471041887374487007916064485523648828943063195915214058020064461558868092911435089696088)

Multiple factors are found
- 2 (too small)
- 7 (too small)
- 23 (too small)
- 394871483009 (too small)
- 241950124618457 (too small?)
- http://factordb.com/index.php?id=1100000006604199987
	- no known factors in the database

[Hint 2](http://factordb.com/index.php?query=17061347780794249474937241232210067248853992326832612618246691021883473946134655677687441412157857703606444858129229798729181511999941417079248816916398800254158380205975686822877683332947748593883879973137797066913439129505904185975901786363274357224292820647481353241115812182163209817605574692194107051614682608366033433427655544056745556231593264049326018746703896654050234167841676926759637292807314933999966217282511228601089336295804775690349998659758021221369291834448080631738623473608907605109479463903233113943877434062712654852684276670025876108200973499112716384186485697596614301411957746226430962874694)

=> Has no known factors in the database. So it will not help us in our endeavour.

#### First attempt
I first tried to make a quadratic equation for n.

```
n = p q
n = (n - h1) (n - h2)
n = n^2 - n(h1 + h2) + h1 h2
0 = n^2 - n(h1 + h2 + 1) + h1 h2
```

However, trying to solve this equation never gave any useful solutions due to 

#### Second attempt

We know 1 = ed mod phi
This can be reduced to the following
```math
1 = ed mod phi
ed = 1 + k phi where k is a positive integer
phi = (ed - 1) / k 
```


We look for a phi which matches the h1/h2 conditions
```
phi = (p-1)(q-1)
phi = (pq - p - q + 1)
phi = n - (n-h1) - (n-h2) + 1
phi = n - n + h1 - n + h2 + 1
phi = -n + h1 + h2 + 1
n = h1 + h2 - phi + 1
```

The implementation can be found in [[moduless.py]]
If we try this for k values between 1 and 1000 and decrypt the messages for these n, we eventually find the flag
he2024{n_r3ec0v3r3d!}
