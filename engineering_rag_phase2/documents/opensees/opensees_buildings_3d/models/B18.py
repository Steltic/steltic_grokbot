"""B18 - out-of-plane offset (8 storeys). Realistic 3D steel building; sanity-checked.
Defining feature: out-of-plane / in-plane offset of the lateral system (Type 4).
Run:  python model.py   -> prints the sanity-check suite; exits 0 iff all checks pass.
Built/analyzed by the shared 3D engine (../../engine/engine3d.py); selects config "B18".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "engine"))
import engine3d as E
if __name__ == "__main__":
    r = E.report("B18")
    sys.exit(0 if r["allp"] else 1)
