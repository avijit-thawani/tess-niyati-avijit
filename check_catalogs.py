"""Check both candidate stars (and their neighbours) against live planet, candidate and eclipsing-binary catalogs."""
import io
import requests
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u
from astroquery.vizier import Vizier
from astroquery.mast import Catalogs

TICS = [345494583, 156733696]
for t in TICS:
    print(f"\n===== TIC {t}")
    for f, col in [("toi.csv", "TIC ID"), ("ctoi.csv", "TIC ID"), ("nasa_ps_tic.csv", "tic_id")]:
        df = pd.read_csv(f"../shell60_100/data/catalogs/{f}")
        print(f"  repo snapshot {f}: {int((df[col] == t).sum())} rows")

    toi = pd.read_csv(io.StringIO(requests.get(
        "https://exofop.ipac.caltech.edu/tess/download_toi.php?sort=toi&output=csv", timeout=60).text))
    ctoi = pd.read_csv(io.StringIO(requests.get(
        "https://exofop.ipac.caltech.edu/tess/download_ctoi.php?sort=ctoi&output=csv", timeout=60).text))
    print(f"  live ExoFOP TOI: {int((toi['TIC ID'] == t).sum())}, CTOI: {int((ctoi['TIC ID'] == t).sum())}")

    q = f"select pl_name from ps where tic_id='TIC {t}'"
    r = requests.get("https://exoplanetarchive.ipac.caltech.edu/TAP/sync",
                     params={"query": q, "format": "csv"}, timeout=60).text
    print(f"  live NASA Exoplanet Archive: {r.strip().splitlines()[1:] or 'none'}")

    star = Catalogs.query_object(f"TIC {t}", catalog="TIC", radius=0.0003 * u.deg)
    star = star[star["ID"] == str(t)][0]
    c = SkyCoord(star["ra"], star["dec"], unit="deg")
    near = Catalogs.query_region(c, catalog="TIC", radius=126 * u.arcsec)  # ~6 TESS pixels
    near = near[near["ID"] != str(t)]
    print(f"  Tmag {star['Tmag']:.2f}; TIC neighbours within 2.1': {len(near)}, "
          f"brightest dTmag {min(near['Tmag']) - star['Tmag']:.1f}" if len(near) else "  no neighbours")

    v = Vizier(columns=["**"], row_limit=50)
    for cat, name in [("J/ApJS/258/16", "TESS EB catalog (Prsa+2022)"),
                      ("B/vsx/vsx", "AAVSO VSX variables"),
                      ("I/357/tbosb2", "Gaia DR3 orbital binaries"),
                      ("I/358/veb", "Gaia DR3 eclipsing binaries"),
                      ("J/AJ/165/141", "TESS FFI EBs (Howard+)")]:
        try:
            res = v.query_region(c, radius=126 * u.arcsec, catalog=cat)
            print(f"  {name}: {sum(len(x) for x in res)} within 2.1'")
        except Exception as e:
            print(f"  {name}: query failed ({type(e).__name__})")
