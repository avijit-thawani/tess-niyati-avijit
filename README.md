# Two new TESS planet-candidate signals: "Niyati" and "Avijit"

A blind search of five years of NASA TESS full-frame-image data on **1,098 Sun-like and smaller stars, 60–100 parsecs away (196–326 light-years), that TESS never observed at 2-minute cadence**. It found two strong transit-like signals that are not on any NASA candidate or planet list (checked 2026-10-09).

> **Status: unvetted candidate signals.** They passed every automatic red-flag test and beat a survey-wide false-alarm baseline. Detailed vetting is in progress (transit fit, hold-out seasons, second data reduction, pixel-level centroids). TESS's 21-arcsecond pixels cannot rule out a faint neighbouring eclipsing binary; only follow-up with other telescopes can turn these into planets.

| | **"Niyati"** (Sanskrit: destiny) | **"Avijit"** (Sanskrit: unconquered) |
|---|---|---|
| Star | HD 354088 = HIP 97983 = TIC 345494583 | TYC 717-2552-1 = TIC 156733696 |
| Constellation, distance | Sagitta, 260 ly (79.7 pc) | Orion, 239 ly (73.4 pc) |
| Star type, TESS mag | G0 dwarf, ~6000 K; 7.9 | Sun-like dwarf, ~5700 K; 8.7 |
| Orbital period | 2.901440 ± 0.000035 d (fit) | 1.817187 d (search; fit pending) |
| Transit depth / duration | 115 ± 13 ppm / 3.6 h (fit) | ~466 ppm / ~3.3 h (search) |
| Size | 1.61 ± 0.17 Earth radii (fit) | ~2.3 Earth radii (search) |
| Transits in data | 31, across 5.1 years | 38, across 6.1 years |
| Detection strength (BLS SDE) / empirical SNR | 15.9 / 11.9 | 15.4 / 10.2 |
| **Preregistered predictions** | [doi:10.5281/zenodo.23271252](https://doi.org/10.5281/zenodo.23271252) | [doi:10.5281/zenodo.23271302](https://doi.org/10.5281/zenodo.23271302) |

Nicknames are informal, not IAU names.

## Evidence so far
- **Passed all 14 automatic red-flag tests**, including:
  - odd/even dip depths agree;
  - no secondary eclipse;
  - consistent across sectors;
  - no single dip dominates;
  - not a TESS-orbit alias;
  - not stellar variability.
- **Beat the false-alarm baseline.** We ran the identical search and triage on all 1,098 light curves flipped upside down, so they contain no real dips. No flag-free fake signal reached SDE 12; the maximum was 11.7. In the real data, these two reached 15.9 and 15.4.
- **Not previously known.** Neither star is in:
  - the live ExoFOP TOI or CTOI lists;
  - the NASA Exoplanet Archive;
  - SIMBAD as a binary.

  No catalogued eclipsing binary or variable star within 2.1′ has a matching period. Sources checked: TESS EB catalogs, Gaia DR3 eclipsing and orbital binaries, AAVSO VSX.
- **Niyati transit fit** (`results/phase3/plots/345494583_fit.png`):
  - the transit model beats a flat line by Δχ² = 109;
  - flat-bottomed, impact parameter b ≈ 0.2;
  - Rp = 1.61 ± 0.17 R⊕.

## Caveats
- **Niyati's dip is slightly long.** Its free-fit stellar density is about half the catalogued value, a ~1.5σ tension. Possible causes: a blend, a larger star than catalogued, or an eccentric orbit.
- **Avijit's dip is about 1.5× the longest expected** for its period and star. That is a known blended-binary signature.
- **Crowded field.** Niyati lies in a crowded galactic-plane field. A faint G = 16.9 eclipsing binary (P = 3.783 d, not commensurate with the candidate's period) sits 31″ away.
- **Missed by NASA and MIT.** Both stars are bright. Why NASA's and MIT's own full-frame-image searches did not flag these signals is not yet established.

## How it was done
The pipeline is adapted from [paraschopra/tess-planet-candidates](https://github.com/paraschopra/tess-planet-candidates), which found two candidates in the <60 pc shell. Changes in this repo:

- **Target shell:** 60–100 pc instead of <60 pc (`pipeline/01_targets.py`). The rest of the target cuts are unchanged: dwarfs with R < 1.5 R☉, contamination < 0.2, ≥3 sectors spanning ≥2 yr, FFI-only, expected SNR ≥ 10.
- **Known-host exclusion:** fresh TOI/CTOI/NASA lists, retrieved 2026-10-09.
- **Download robustness:** a network timeout (`pipeline/env.py`) and a hard per-star timeout (`pipeline/02_download.py`), so hung MAST connections can't stall the run.
- **Vetting targets:** `pipeline/vet.py` points at the new candidates.
- **Catalog cross-check:** `check_catalogs.py`, against live ExoFOP, the NASA Exoplanet Archive, and EB/variable catalogs.
- **Preregistration package:** `make_package.py` generates the Zenodo package.

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python pipeline/01_targets.py   # then 02_download, 03_search, 05_triage, 06_inverted, 07_fit ...
```

Light curves (~770 MB) are not in the repo; `02_download.py` re-fetches them from MAST.

## Results in this repo
- `results/targets_searched.csv`: the 1,098 searched stars.
- `results/phase2/signals.csv`, `results/phase2/triage.csv`: every search signal, with red flags.
- `results/phase3/inverted_triage.csv`: the upside-down false-alarm baseline.
- `results/phase3/*_fit.json`, `results/phase3/plots/`: transit fits.
- `package/TIC*/`: the exact files deposited on Zenodo.

## Next steps
1. Finish vetting: Avijit's fit, hold-out seasons, NASA-vs-MIT reductions, and pixel-level difference imaging. Post the results as new Zenodo versions.
2. A short Research Note of the AAS. ExoFOP has required publication before CTOI upload since 2026-08-19.
3. Then submit CTOIs **TIC 345494583.01** and **TIC 156733696.01**.

## Credits and license
- **Pipeline:** Paras Chopra (MIT).
- **This search and these candidates:** Avijit Thawani.
- **AI assistance:** analysis was run with AI coding agents.
- **Data:** all public. NASA TESS via MAST, ESA Gaia, the TESS Input Catalog, ExoFOP, and the NASA Exoplanet Archive.
- **License:** code is MIT (see `LICENSE`); text, figures and data products are CC BY 4.0.
