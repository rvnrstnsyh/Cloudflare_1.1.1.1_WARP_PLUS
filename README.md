<a href="https://www.cloudflare.com"><img alt="Cloudflare" src="https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Cloudflare-logo-vector.svg/1200px-Cloudflare-logo-vector.svg.png"></a>
<a href="https://1.1.1.1"><img width="200" alt="1.1.1.1" src="https://cdn.fing.io/images/isp/HK/logo/cloudflare_warp_logo.png"></a>

WARP+ uses Cloudflare’s virtual private backbone, known as Argo, to achieve higher speeds and ensure your connection is encrypted across the long haul of the Internet. [Read more](https://blog.cloudflare.com/announcing-warp-plus)
## How to use
Extract the .zip file first - verify the signature with my [public key](https://keys.openpgp.org/vks/v1/by-fingerprint/F739B2ED9CEB7482B1D34529F0F35EAD50642AD7),
and execute with python.
```
~# gpg --verify signature.asc Cloudflare_1.1.1.1_WARP_PLUS.py
~# python3 Cloudflare_1.1.1.1_WARP_PLUS.py
```
#### Get your client ID
> [mobile] Settings > Advance > Diagnostics > ID

> [desktop] Settings > Preferences > General > Device ID
#### Reset if the number of GB hasn't increased 
> [mobile] Settings > Advance > Connection options > Reset security keys

> [desktop] Settings > Preferences > Connection > Reset Encryption Keys
```
+--------------------------------------+
| Cloudflare | 1.1.1.1 WARP+           |
+------------+-------------------------+
|            | https://rvnrstnsyh.dev  |
|            | re@rvnrstnsyh.dev       |
+--------------------------------------+
[-] Work on ID: ********-****-****-****-************
[+] [□□□□□□□□□□] 100%
[!] 100 GB has been successfully added to your account.
[#] Total: 100 success, 0 fail
[*] After 20 seconds, a new request will be sent.
```
This will recursively in every 20 seconds.

**Please note this isn't an internet data quota.**

## License

MIT
