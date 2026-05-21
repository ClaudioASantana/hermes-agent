import subprocess
import json
import time

def test_payload(payload):
    print(f"Sending: {payload}")
    p = subprocess.Popen(["hermes", "mcp", "serve"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p.stdin.write(json.dumps(payload) + "\n")
    p.stdin.flush()
    time.sleep(1)
    
    import select
    while select.select([p.stdout], [], [], 0)[0]:
        line = p.stdout.readline()
        if not line: break
        print("STDOUT:", line.strip())
        
    while select.select([p.stderr], [], [], 0)[0]:
        line = p.stderr.readline()
        if not line: break
        print("STDERR:", line.strip())
        
    p.terminate()

test_payload({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "Cursor",
            "version": "1.0.0"
        }
    }
})

