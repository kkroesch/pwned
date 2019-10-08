from hashlib import sha1
from bloom import BloomFilter
from bottle import route, request, run, error

filter = BloomFilter("pwned-passwords-1.0u2.bloom")

@route('/check')
def check():
    password = request.query.password
    if filter.contains(password):
        return "BAD"
    else:
        return "GOOD"

run(host='0.0.0.0', port=8080, debug=False)
