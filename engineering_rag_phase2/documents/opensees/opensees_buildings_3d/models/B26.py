"""B26 - high-aspect narrow office (5 storeys). Realistic 3D steel building; sanity-checked.
Defining feature: high plan aspect ratio (long narrow footprint).
Run:  python model.py   -> prints the sanity-check suite; exits 0 iff all checks pass.
Built/analyzed by the shared 3D engine (../../engine/engine3d.py); selects config "B26".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "engine"))
import engine3d as E
if __name__ == "__main__":
    r = E.report("B26")
    sys.exit(0 if r["allp"] else 1)
