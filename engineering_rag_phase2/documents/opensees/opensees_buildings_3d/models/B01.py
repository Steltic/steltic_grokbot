"""
B01 - 3D realistic steel building #1  (also stands up the reusable 3D engine).

Low-rise office. 3 storeys @ 13 ft (hn = 39 ft), 5 x 3 bays @ 30 ft
(150 ft x 90 ft plan), fixed bases, rigid floor diaphragms. Lateral system:
3D space moment frame (all beam-column joints moment-connected) -- the simplest
realistic low-rise system; perimeter-MF + interior leaning columns is introduced
in a later building. ASCE 7-22 ELF, SDC B (low seismic). Sections are realistic
ASSUMED sizes (not designed). Units: kip, inch.

Standalone + self-checking: run `python model.py` -> prints the sanity-check suite
and exits non-zero if any check fails.

Sanity checks (definition of "validated"):
  1 equilibrium  - base reactions balance applied storey shear (X and Y), tol 0.1%
  2 stability    - all eigenvalues > 0 (no spurious/zero-energy modes)
  3 period       - T1 within 0.5x .. 3x of ASCE 7 Ta (bare-centreline runs flexible)
  4 modal mass   - cumulative effective modal mass >= 90% in BOTH directions
  5 drift        - max interstorey drift ratio sane and < 0.020 (SDC B/Risk II)
  6 base shear   - ELF V recovered at the base (X and Y)
"""
import math, sys
import openseespy.opensees as ops

g = 386.4
E, Gmod = 29000.0, 11200.0

# --- realistic ASSUMED sections (A in^2, I in^4) ---
SEC = {
    "W14X132": dict(A=38.8, Ix=1530.0, Iy=548.0, J=12.3),
    "W27X94":  dict(A=27.7, Ix=3270.0, Iy=124.0, J=4.03),
}
COL, BEAM = "W14X132", "W27X94"

# --- geometry ---
NX, NY = 5, 3
SX = SY = 30.0 * 12
HS = 13.0 * 12
NF = 3
xs = [i * SX for i in range(NX + 1)]
ys = [j * SY for j in range(NY + 1)]
zs = [k * HS for k in range(NF + 1)]
Bx, By = xs[-1], ys[-1]
AREA = (Bx / 12) * (By / 12)               # ft^2

# --- loads / seismic (SDC B) ---
D_FLOOR, D_ROOF, CLAD_PSF, L_FLOOR = 75.0, 60.0, 15.0, 50.0
SDS, SD1, R, Ie = 0.25, 0.10, 3.0, 1.0
Cd = 3.0                                     # ASCE 7 Table 12.2-1 (steel system not detailed)
Ct, xexp = 0.028, 0.8
hn_ft = zs[-1] / 12
Ta = Ct * hn_ft ** xexp
Cu, TL = 1.6, 6.0
DRIFT_LIMIT = 0.020                         # ASCE 7 Table 12.12-1, Risk II MF

def ntag(i, j, k): return k * 10000 + i * 100 + j
def mtag(k): return k * 10000 + 9999

def floor_seismic_weight(k):
    d = D_ROOF if k == NF else D_FLOOR
    w = d * AREA / 1000.0
    perim_ft = 2 * (Bx + By) / 12
    trib_h = (HS / 12) if k < NF else (HS / 24)
    return w + CLAD_PSF * perim_ft * trib_h / 1000.0

def floor_gravity_pdelta(k):
    d = D_ROOF if k == NF else D_FLOOR
    l = 0.0 if k == NF else L_FLOOR
    return (d + 0.5 * l) * AREA / 1000.0

def floor_mass(k): return floor_seismic_weight(k) / g
def floor_Jm(k):   return floor_mass(k) * (Bx ** 2 + By ** 2) / 12.0

def build(transf="Linear"):
    ops.wipe()
    ops.model("basic", "-ndm", 3, "-ndf", 6)
    for k in range(NF + 1):
        for i in range(NX + 1):
            for j in range(NY + 1):
                ops.node(ntag(i, j, k), xs[i], ys[j], zs[k])
    for i in range(NX + 1):
        for j in range(NY + 1):
            ops.fix(ntag(i, j, 0), 1, 1, 1, 1, 1, 1)
    for k in range(1, NF + 1):
        ops.node(mtag(k), Bx / 2, By / 2, zs[k])
        ops.fix(mtag(k), 0, 0, 1, 1, 1, 0)
    colT = "PDelta" if transf == "PDelta" else "Linear"
    ops.geomTransf(colT, 1, 1.0, 0.0, 0.0)     # column strong axis resists X-sway
    ops.geomTransf(colT, 2, 0.0, 1.0, 0.0)     # column strong axis resists Y-sway
    ops.geomTransf("Linear", 3, 0.0, 0.0, 1.0) # beams: local z horizontal, Iz vertical-plane
    c, b = SEC[COL], SEC[BEAM]
    et = 1
    for i in range(NX + 1):
        for j in range(NY + 1):
            tt = 2 if (i == 0 or i == NX) else 1
            for k in range(NF):
                ops.element("elasticBeamColumn", et, ntag(i, j, k), ntag(i, j, k + 1),
                            c["A"], E, Gmod, c["J"], c["Iy"], c["Ix"], tt)
                et += 1
    for k in range(1, NF + 1):
        for j in range(NY + 1):
            for i in range(NX):
                ops.element("elasticBeamColumn", et, ntag(i, j, k), ntag(i + 1, j, k),
                            b["A"], E, Gmod, b["J"], b["Ix"], b["Iy"], 3); et += 1
        for i in range(NX + 1):
            for j in range(NY):
                ops.element("elasticBeamColumn", et, ntag(i, j, k), ntag(i, j + 1, k),
                            b["A"], E, Gmod, b["J"], b["Ix"], b["Iy"], 3); et += 1
    for k in range(1, NF + 1):
        slaves = [ntag(i, j, k) for i in range(NX + 1) for j in range(NY + 1)]
        ops.rigidDiaphragm(3, mtag(k), *slaves)
        ops.mass(mtag(k), floor_mass(k), floor_mass(k), 0.0, 0.0, 0.0, floor_Jm(k))
    return et - 1

def modal(nmodes=9):
    build("Linear")
    w2 = ops.eigen("-fullGenLapack", nmodes)
    T = [2 * math.pi / math.sqrt(max(x, 1e-12)) for x in w2]
    Mtot = sum(floor_mass(k) for k in range(1, NF + 1))
    effX, effY = [], []
    for mode in range(1, nmodes + 1):
        Lx = Ly = Mi = 0.0
        for k in range(1, NF + 1):
            p = ops.nodeEigenvector(mtag(k), mode)         # [UX,UY,UZ,RX,RY,RZ]
            mk, Jk = floor_mass(k), floor_Jm(k)
            Lx += mk * p[0]; Ly += mk * p[1]
            Mi += mk * (p[0] ** 2 + p[1] ** 2) + Jk * p[5] ** 2
        effX.append((Lx ** 2) / Mi / Mtot if Mi > 0 else 0.0)
        effY.append((Ly ** 2) / Mi / Mtot if Mi > 0 else 0.0)
    return T, w2, effX, effY

def elf(T1):
    W = sum(floor_seismic_weight(k) for k in range(1, NF + 1))
    Tu = min(T1, Cu * Ta)
    Cs = SDS / (R / Ie)
    cap = SD1 / (Tu * (R / Ie)) if Tu <= TL else SD1 * TL / (Tu ** 2 * (R / Ie))
    Cs = max(min(Cs, cap), max(0.044 * SDS * Ie, 0.01))
    V = Cs * W
    kk = 1.0 if Tu <= 0.5 else (2.0 if Tu >= 2.5 else 1 + (Tu - 0.5) / 2.0)
    whk = {k: floor_seismic_weight(k) * zs[k] ** kk for k in range(1, NF + 1)}
    s = sum(whk.values())
    return Cs, V, Tu, kk, {k: V * whk[k] / s for k in range(1, NF + 1)}, W

def static_lateral(Fx, direction):
    build("PDelta")
    di = 0 if direction == "X" else 1
    ops.timeSeries("Linear", 1); ops.pattern("Plain", 1, 1)
    for k in range(1, NF + 1):
        p = floor_gravity_pdelta(k) / ((NX + 1) * (NY + 1))
        for i in range(NX + 1):
            for j in range(NY + 1):
                ops.load(ntag(i, j, k), 0, 0, -p, 0, 0, 0)
    for k in range(1, NF + 1):
        f = [0.0] * 6; f[di] = Fx[k]; ops.load(mtag(k), *f)
    ops.constraints("Transformation"); ops.numberer("RCM"); ops.system("BandGen")
    ops.test("NormDispIncr", 1e-8, 100); ops.algorithm("Newton")
    ops.integrator("LoadControl", 1.0); ops.analysis("Static")
    ok = ops.analyze(1)
    disp = {k: ops.nodeDisp(mtag(k), di + 1) for k in range(1, NF + 1)}
    drifts, prev = [], 0.0
    for k in range(1, NF + 1):
        drifts.append((disp[k] - prev) / HS); prev = disp[k]
    ops.reactions()
    Rsum = sum(ops.nodeReaction(ntag(i, j, 0), di + 1)
               for i in range(NX + 1) for j in range(NY + 1))
    return ok, disp, drifts, Rsum

def run_checks(verbose=True):
    res, checks = {}, {}
    T, w2, eX, eY = modal(9)
    res["T"] = T; res["cumX"] = sum(eX); res["cumY"] = sum(eY)
    Cs, V, Tu, kk, Fx, W = elf(T[0])
    res.update(Cs=Cs, V=V, Tused=Tu, k=kk, W=W)
    sx = static_lateral(Fx, "X"); sy = static_lateral(Fx, "Y")
    res["roofX"], res["driftXe"], res["RX"] = sx[1][NF], max(abs(d) for d in sx[2]), sx[3]
    res["roofY"], res["driftYe"], res["RY"] = sy[1][NF], max(abs(d) for d in sy[2]), sy[3]
    # ASCE 7-22 Eq. 12.8-15: design story drift = Cd * delta_elastic / Ie
    res["driftX"] = Cd * res["driftXe"] / Ie
    res["driftY"] = Cd * res["driftYe"] / Ie
    res["okX"], res["okY"] = sx[0], sy[0]

    checks["equilibrium_X"] = (abs(res["RX"] + V) <= 1e-3 * V, f"R={res['RX']:.2f} vs -V={-V:.2f}")
    checks["equilibrium_Y"] = (abs(res["RY"] + V) <= 1e-3 * V, f"R={res['RY']:.2f} vs -V={-V:.2f}")
    checks["stability"]     = (min(w2) > 0, f"min eigenvalue={min(w2):.4g}")
    checks["period"]        = (0.5 * Ta <= T[0] <= 3 * Ta, f"T1={T[0]:.3f}s in [{0.5*Ta:.2f},{3*Ta:.2f}]")
    checks["modal_mass_X"]  = (res["cumX"] >= 0.90, f"cumX={res['cumX']:.3f}")
    checks["modal_mass_Y"]  = (res["cumY"] >= 0.90, f"cumY={res['cumY']:.3f}")
    checks["drift_X"]       = (0 < res["driftX"] < DRIFT_LIMIT, f"max={res['driftX']:.5f} (1/{1/res['driftX']:.0f}) < {DRIFT_LIMIT}")
    checks["drift_Y"]       = (0 < res["driftY"] < DRIFT_LIMIT, f"max={res['driftY']:.5f} (1/{1/res['driftY']:.0f}) < {DRIFT_LIMIT}")
    checks["base_shear_X"]  = (abs(abs(res["RX"]) - V) <= 1e-3 * V, f"|R|={abs(res['RX']):.2f} ~ V={V:.2f}")
    checks["base_shear_Y"]  = (abs(abs(res["RY"]) - V) <= 1e-3 * V, f"|R|={abs(res['RY']):.2f} ~ V={V:.2f}")
    # serviceability: floor-beam vertical deflection, simple span, strong axis (Ix): live L/360, total L/240
    bIx = SEC[BEAM]["Ix"]; span = SX; trib = SY
    wLL = L_FLOOR/1000.0/144.0*trib; wTL = (D_FLOOR+L_FLOOR)/1000.0/144.0*trib
    dLL = 5*wLL*span**4/(384*E*bIx); dTL = 5*wTL*span**4/(384*E*bIx)
    checks["beam_defl_LL"] = (dLL < span/360, f"{dLL:.2f}in < L/360={span/360:.2f}")
    checks["beam_defl_TL"] = (dTL < span/240, f"{dTL:.2f}in < L/240={span/240:.2f}")

    if verbose:
        print(f"plan {Bx/12:.0f}x{By/12:.0f} ft, {NF} storeys @ {HS/12:.0f} ft, hn={hn_ft:.0f} ft")
        print(f"W={W:.0f} kip  Ta={Ta:.3f}s  Cs={Cs:.4f}  V={V:.1f} kip  Tused={Tu:.3f}s  k={kk:.2f}")
        print(f"T1..T3 = {T[0]:.3f}/{T[1]:.3f}/{T[2]:.3f} s   cumModalMass X={res['cumX']:.2f} Y={res['cumY']:.2f}")
        print(f"roof drift X={res['roofX']:.3f} in (max {res['driftX']:.5f}), Y={res['roofY']:.3f} in (max {res['driftY']:.5f})")
        print("--- sanity checks ---")
        for name, (ok, msg) in checks.items():
            print(f"  [{'PASS' if ok else 'FAIL'}] {name:14s} {msg}")
    res["checks"] = checks
    res["all_pass"] = all(ok for ok, _ in checks.values())
    return res

if __name__ == "__main__":
    r = run_checks()
    print("\nRESULT:", "ALL CHECKS PASS" if r["all_pass"] else "SOME CHECKS FAILED")
    sys.exit(0 if r["all_pass"] else 1)
