import hashlib

N = int("FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123", 16)

def sm3(data: bytes) -> bytes:
    return hashlib.new("sm3", data).digest()

def build_known_record(private_key_int: int) -> bytes:
    proof = sm3(private_key_int.to_bytes(32, "big") + b"|audit-proof").hex()
    return (
        f"idx=1000;user=guest;proof={proof};"
        f"action=view;status=ok;comment=freshman_crypto_lab;"
    ).encode()

SIG1 = "3b2c11a5578dca2b899a0483864e6b772c1af5ef6ab150bdaa232aedb433dd8ac5efd3822c57111343060f85cd3030686fbde94865f2371d3612b898e2212672"
SIG2 = "091931932b06b60dafc9f7ef77f8e43e181e96f212915dda24a894f253a0f8189e074018846ec2ff810e78dc0d862d270e2bc6689d0b5425c9c952cf25839845"

C1000 = bytes.fromhex(
    "ad2a60ab3a12d996b02a50a752f6800c62d3f6139dbf5481b2b1d823212a3a922dd2420b394e2eef74cc6da05c65766de54d2482dc5fc48a99c38f53da339093833d347eeb98b3caf3d454d0641028cf5ef8aaf89bccecd004fad7e454b2f275bad5b19bd08160ce8e55ccb383a016af178cf747c74c29c72b3f5d7ebf8d31f8cdd170cee613b4eaf9415cd97d"
)

C1002 = bytes.fromhex(
    "26830a073c4a2aeb298e7df44b6d746cbf457a8fdf07938ec5a5fe27a255d2a5f9074c2aed91f4cce2850cd65e1462ca35b9ad94b99ee39459f08fc543a3ff3bf595fc81c1972fc88909d7ad"
)
r1,s1=int.from_bytes(SIG1[:64]),int.from_bytes(SIG1[64:])
r2,s2=int.from_bytes(SIG2[:64]),int.from_bytes(SIG2[64:])