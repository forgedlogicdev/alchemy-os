#!/usr/bin/env python3
"""
AlchemyOS P2P Mesh Daemon
Connects all AlchemyOS nodes via Tailscale (online) or LAN hotspot (offline).
AES-256-GCM authenticated messages. Password-protected.
"""

import socket, json, hashlib, time, threading, os, struct
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

P2P_PORT = 45999
BEACON_PORT = 8888
CONFIG_PATH = os.path.expanduser("~/.config/alchemy/p2p_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {
        "node_id": socket.gethostname(),
        "password": "",
        "capabilities": [],
        "tailscale": True
    }

class P2PNode:
    def __init__(self):
        self.config = load_config()
        self.node_id = self.config.get("node_id", socket.gethostname())
        self.peers = {}
        self.running = True
        self.key = hashlib.sha256(self.config["password"].encode()).digest()
        self.aes = AESGCM(self.key)

    def encrypt(self, plaintext):
        nonce = os.urandom(12)
        ct = self.aes.encrypt(nonce, plaintext.encode(), None)
        return nonce + ct

    def decrypt(self, data):
        nonce, ct = data[:12], data[12:]
        return self.aes.decrypt(nonce, ct, None).decode()

    def advertise_udp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        msg = json.dumps({
            "node_id": self.node_id,
            "port": P2P_PORT,
            "caps": self.config.get("capabilities", [])
        }).encode()
        while self.running:
            sock.sendto(msg, ("255.255.255.255", BEACON_PORT))
            time.sleep(5)

    def listen_udp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", BEACON_PORT))
        while self.running:
            data, addr = sock.recvfrom(1024)
            try:
                info = json.loads(data.decode())
                peer_id = info["node_id"]
                if peer_id != self.node_id:
                    self.peers[peer_id] = {"addr": addr[0], "port": info["port"], "caps": info.get("caps", []), "last_seen": time.time()}
                    self.connect_peer(peer_id, addr[0], info["port"])
            except:
                pass

    def connect_peer(self, peer_id, host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            handshake = self.encrypt(json.dumps({"type": "hello", "node_id": self.node_id, "caps": self.config.get("capabilities", [])}))
            sock.send(struct.pack(">I", len(handshake)) + handshake)
        except:
            pass

    def serve_tcp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", P2P_PORT))
        sock.listen(10)
        while self.running:
            try:
                conn, addr = sock.accept()
                threading.Thread(target=self.handle_conn, args=(conn, addr), daemon=True).start()
            except:
                pass

    def handle_conn(self, conn, addr):
        try:
            raw = conn.recv(4)
            if len(raw) < 4: return
            length = struct.unpack(">I", raw)[0]
            data = conn.recv(length)
            msg = json.loads(self.decrypt(data))
            if msg["type"] == "hello":
                peer_id = msg["node_id"]
                self.peers[peer_id] = {"addr": addr[0], "caps": msg.get("caps", []), "last_seen": time.time()}
                resp = self.encrypt(json.dumps({"type": "ack", "node_id": self.node_id}))
                conn.send(struct.pack(">I", len(resp)) + resp)
                self.on_peer_connected(peer_id)
            elif msg["type"] == "request":
                self.on_request(msg, conn)
        except Exception as e:
            pass
        finally:
            conn.close()

    def on_peer_connected(self, peer_id):
        caps = self.peers[peer_id].get("caps", [])
        for cap in caps:
            pass

    def on_request(self, msg, conn):
        pass

    def heartbeat(self):
        while self.running:
            now = time.time()
            dead = [p for p, info in self.peers.items() if now - info["last_seen"] > 30]
            for p in dead:
                del self.peers[p]
            time.sleep(10)

    def send_to(self, peer_id, action, payload):
        if peer_id not in self.peers:
            return None
        info = self.peers[peer_id]
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((info["addr"], info["port"]))
            msg = self.encrypt(json.dumps({"type": "request", "from": self.node_id, "action": action, "payload": payload}))
            sock.send(struct.pack(">I", len(msg)) + msg)
            raw = sock.recv(4)
            length = struct.unpack(">I", raw)[0]
            data = sock.recv(length)
            return json.loads(self.decrypt(data))
        except:
            return None

    def start(self):
        threads = [
            threading.Thread(target=self.serve_tcp, daemon=True),
            threading.Thread(target=self.listen_udp, daemon=True),
            threading.Thread(target=self.advertise_udp, daemon=True),
            threading.Thread(target=self.heartbeat, daemon=True),
        ]
        for t in threads:
            t.start()
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False

if __name__ == "__main__":
    node = P2PNode()
    node.start()
