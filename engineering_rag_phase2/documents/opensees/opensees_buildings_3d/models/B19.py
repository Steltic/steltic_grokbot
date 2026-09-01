"""B19 - snow long-span industrial (2 storeys). Realistic 3D steel building; sanity-checked.
Defining feature: snow-governed long-span industrial gravity.
Run:  python model.py   -> prints the sanity-check suite; exits 0 iff all checks pass.
Built/analyzed by the shared 3D engine (../../engine/engine3d.py); selects config "B19".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "engine"))
import engine3d as E
if __name__ == "__main__":
    r = E.report("B19")
    sys.exit(0 if r["allp"] else 1)
