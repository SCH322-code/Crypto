import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

N = int("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123", 16)
def sm3(data: bytes) -> bytes:#首先就是这个语法，：bytes是指data的类型是bytes是吗,->bytes则是指输出？同时bytes是什么数据类型？
    return hashlib.new("sm3", data).digest()#.digest()函数是干什么的

def bad_sm2_sign(sm2, message: bytes, device_secret: bytes):
    digest = sm3(message)
    k = int.from_bytes(sm3(device_secret), "big") % (N - 1) + 1#int.from_bytes是什么？ "big"又是什么
    return sm2.sign_with_k(digest, k)#这是什么

def get_iv(index: int) -> bytes:
    return b"\x00" * 12 + index.to_bytes(4, "big")#b"\x00" * 12这是什么语法？b"\x00"是指什么？index.to_bytes又是什么？

def encrypt_record(key: bytes, index: int, plaintext: bytes) -> bytes:
    cipher = Cipher(algorithms.SM4(key), modes.CTR(get_iv(index)))#Cipher函数是什么
    enc = cipher.encryptor()#这是什么
    return enc.update(plaintext) + enc.finalize()#这我也看不懂

def build_known_record(private_key_int: int) -> bytes:
    proof = sm3(private_key_int.to_bytes(32, "big") + b"|audit-proof").hex()#.to_bytes(32, "big")是什么.hex()是什么
    return (
        f"idx=1000;user=guest;proof={proof};"
        f"action=view;status=ok;comment=freshman_crypto_lab;"
    ).encode()#.encode()是什么函数


# ===== Captured public data =====

PUBLIC_KEY = "0dcd3edc3127b3b02cbc563d47aac19492ea2c2ac5710f47aeb1c24a7c70f4e7d61b260cc882dbbdcd770073a1ebef6aa20b96a852c3d5f32089befc32843595"

MSG1 = b'approve:guest:read'
SIG1 = "3b2c11a5578dca2b899a0483864e6b772c1af5ef6ab150bdaa232aedb433dd8ac5efd3822c57111343060f85cd3030686fbde94865f2371d3612b898e2212672"

MSG2 = b'approve:guest:export'
SIG2 = "091931932b06b60dafc9f7ef77f8e43e181e96f212915dda24a894f253a0f8189e074018846ec2ff810e78dc0d862d270e2bc6689d0b5425c9c952cf25839845"

C1000 = bytes.fromhex(
    "ad2a60ab3a12d996b02a50a752f6800c62d3f6139dbf5481b2b1d823212a3a922dd2420b394e2eef74cc6da05c65766de54d2482dc5fc48a99c38f53da339093833d347eeb98b3caf3d454d0641028cf5ef8aaf89bccecd004fad7e454b2f275bad5b19bd08160ce8e55ccb383a016af178cf747c74c29c72b3f5d7ebf8d31f8cdd170cee613b4eaf9415cd97d"
)

C1002 = bytes.fromhex(
    "26830a073c4a2aeb298e7df44b6d746cbf457a8fdf07938ec5a5fe27a255d2a5f9074c2aed91f4cce2850cd65e1462ca35b9ad94b99ee39459f08fc543a3ff3bf595fc81c1972fc88909d7ad"
)
