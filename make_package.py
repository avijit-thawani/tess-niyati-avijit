"""Preregistration package for the top candidate: summary + predicted transit times (search ephemeris)."""
import json
import sys
from pathlib import Path

import astropy.units as u
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord, get_constellation
from astropy.time import Time
from astroquery.mast import Catalogs

TIC = int(sys.argv[1]) if len(sys.argv) > 1 else 345494583
OUT = Path("package") / f"TIC{TIC}"
OUT.mkdir(parents=True, exist_ok=True)

tr = pd.read_csv("results/phase2/triage.csv")
r = tr[(tr.tic == TIC) & (tr.signal == 1)].iloc[0]
P, t0_btjd, dur_d = float(r.period), float(r.t0), float(r.duration_hr) / 24
baseline = float(r.baseline_d)
n_cyc = baseline / P
# Without the MCMC fit, bound timing error by assuming the epoch is good to ~1/4 duration at each end.
sig_t0 = dur_d / 4
sig_P = dur_d / 4 / n_cyc

s = Catalogs.query_object(f"TIC {TIC}", catalog="TIC", radius=0.0003 * u.deg)
s = s[s["ID"] == str(TIC)][0]
c = SkyCoord(s["ra"], s["dec"], unit="deg")
info = {
    "TIC": TIC, "Gaia_DR3": str(s["GAIA"]), "HIP": str(s["HIP"]) if s["HIP"] else None,
    "TYC": str(s["TYC"]) if s["TYC"] else None,
    "ra_deg": round(float(s["ra"]), 6), "dec_deg": round(float(s["dec"]), 6),
    "constellation": get_constellation(c), "Tmag": round(float(s["Tmag"]), 3),
    "Teff_K": round(float(s["Teff"])), "R_star_Rsun": round(float(s["rad"]), 3),
    "M_star_Msun": round(float(s["mass"]), 3), "distance_pc": round(float(s["d"]), 2),
    "distance_ly": round(float(s["d"]) * 3.2616, 1),
    "period_d": round(P, 6), "period_sigma_d_rough": round(sig_P, 6),
    "t0_BJD_TDB": round(t0_btjd + 2457000, 5), "t0_sigma_d_rough": round(sig_t0, 4),
    "depth_ppm": round(float(r.depth_ppm), 1), "duration_hr": round(float(r.duration_hr), 2),
    "rp_earth": round(float(r.rp_earth), 2), "n_transits": int(r.n_transits),
    "sde": round(float(r.sde), 2), "snr_empirical": round(float(r.snr_emp), 2),
    "n_sectors_used": int(r.n_sectors_used), "baseline_d": round(baseline, 1),
    "flags": None if pd.isna(r["flags"]) else r["flags"],
}
(OUT / "candidate.json").write_text(json.dumps(info, indent=2))

now = Time.now().jd - 2457000
end = Time("2028-12-31").jd - 2457000
n0 = int(np.ceil((now - t0_btjd) / P))
n1 = int((end - t0_btjd) / P)
rows = []
for n in range(n0, n1 + 1):
    tm = t0_btjd + n * P
    sig = np.hypot(sig_t0, n * sig_P)
    utc = Time(tm + 2457000, format="jd", scale="tdb").utc
    rows.append({"epoch": n, "mid_BJD_TDB": round(tm + 2457000, 5),
                 "mid_UTC_approx": utc.strftime("%Y-%m-%d %H:%M"),
                 "sigma_min": round(sig * 1440, 1),
                 "window_start_UTC": (utc - 3 * sig * u.day - dur_d / 2 * u.day).strftime("%Y-%m-%d %H:%M"),
                 "window_end_UTC": (utc + 3 * sig * u.day + dur_d / 2 * u.day).strftime("%Y-%m-%d %H:%M"),
                 "depth_ppm": info["depth_ppm"], "duration_hr": info["duration_hr"]})
pd.DataFrame(rows).to_csv(OUT / f"{TIC}_predicted_transits.csv", index=False)
print(json.dumps(info, indent=2))
print(f"{len(rows)} predicted transits -> {OUT}")
