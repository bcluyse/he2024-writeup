![[Pasted image 20240306104216.png]]

The name refers to base encoding. It does not look like base64 encoding at all.
After testing multiple base** encoding algorithms, it seems like base85 results in the flag.

https://gchq.github.io/CyberChef/#recipe=From_Base85('!-u',true,'z')&input=Qk9ycVExLE8%2BOTFnYXM8P1onZSg/WSsrdEFuRTM3Cg

`he2024{64_is_not_enuff!}`
