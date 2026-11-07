"""Verify original transfer integrity. Does not write files or require dependencies."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    failures=[]
    for name,expected in manifest['sha256'].items():
        file=ROOT/name
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest()!=expected: failures.append(name)
    if failures: raise SystemExit('Missing or changed transfer files: '+', '.join(failures))
    print(f"Verified {len(manifest['sha256'])} transferred files against SHA-256 hashes.")
if __name__=='__main__':main()
