"""B07 - dual MF+CBF core (10 storeys). Realistic 3D steel building; sanity-checked.
Defining feature: dual system with 25% moment-frame backup check.
Run:  python model.py   -> prints the sanity-check suite; exits 0 iff all checks pass.
Built/analyzed by the shared 3D engine (../../engine/engine3d.py); selects config "B07".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "engine"))
import engine3d as E
if __name__ == "__main__":
    r = E.report("B07")
    sys.exit(0 if r["allp"] else 1)
