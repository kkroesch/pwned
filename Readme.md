# Pwnedcheck

Simple web-callable wrapper around [marcans Bloom Filter](https://gist.github.com/marcan/23e1ec416bf884dcd7f0e635ce5f2724).

  1. Download the pre-computed Bloom files; see header of `bloom.py` how to do it.
  1. Start app with `python3 app.py`.
  1. Convert password to SHA1 sum: `python3 -c 'from hashlib import sha1; print(sha1(b"Mys3cretPwndword").hexdigest())'`
  1. Check with `curl http://localhost:8080/check\?password\=60c9750abcb91910fa16cec7b716cfa03925a3ae`
