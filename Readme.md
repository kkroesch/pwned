# Pwnedcheck

  1. Download the pre-computed Bloom files; see header of `bloom.py` how to do it.
  1. Start app with `python3 app.py`.
  1. Convert password to SHA1 sum: `python3 -c 'from hashlib import sha1; print(sha1(b"Mys3cretPwndword").hexdigest())'`
  1. Check with `curl https://pwndchk.scapp-corp.swisscom.com/check\?password\=60c9750abcb91910fa16cec7b716cfa03925a3ae`


