### Challenge description
You found this hatch. It should be easy to open, but you might need some force.

### Solution
We get a python script and it seems to refer that we might need to brute force the solution.

It seems like the encryption is adding an offset and then XORing the output. We get the encrypted value.
So the easiest way is to brute force the he2024 prefix and trying to figure out the kee/off values.

The implementation for this can be found [[.src/6/hatchlatch.py]]

The flag found is

he2024{h4tch_4cc355_gr4nt3d}
