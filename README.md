# A 1,098-star TESS search at 60–100 pc: three strong signals, all retracted as likely neighbour eclipsing binaries

> **Correction (2026-10-13).** The two signals preregistered on 2026-10-09 as candidates **"Niyati"** (HD 354088 / TIC 345494583) and **"Avijit"** (TYC 717-2552-1 / TIC 156733696) are **retracted as planet candidates on those stars**. Pixel-level difference imaging places the missing light on faint neighbouring stars, 33″ and 47″ from the targets. Likely cause: blended eclipsing binaries. A third strong signal (TIC 180791301) fails the same way. **This search produced no surviving planet candidates.** The original Zenodo records are kept as the dated record, with a new version noting the retraction: [Niyati](https://doi.org/10.5281/zenodo.23271252), [Avijit](https://doi.org/10.5281/zenodo.23271302).

We searched five years of NASA TESS full-frame-image data on **1,098 Sun-like and smaller stars at 60–100 parsecs (196–326 light-years)**. None of them were observed at 2-minute cadence, and known planet hosts, TOIs and CTOIs were excluded (lists checked 2026-10-09). Three signals stood far above the survey's false-alarm baseline. All three then failed vetting.

## Gate log
Steps follow [`CHECKLIST.md`](CHECKLIST.md). Fit, hold-out, pixel and second-reduction plots are in `results/phase3/plots/`.

| Step | "Niyati" TIC 345494583 | "Avijit" TIC 156733696 | TIC 180791301 |
|---|---|---|---|
| Star | HD 354088, G0, T = 7.9, 79.7 pc | TYC 717-2552-1, ~5700 K, T = 8.7, 73.4 pc | TYC 7148-1002-1, ~4900 K, T = 9.9, 70.5 pc |
| Signal | P = 2.90144 d, 115 ppm, 3.6 h | P = 1.81719 d, 494 ppm, 3.7 h | P = 0.58012 d, 189 ppm, 1.8 h |
| 1 Novelty | pass | pass | pass |
| 2 Blind detection (SDE / empirical SNR) | 15.9 / 11.9 | 15.4 / 10.2 | 20.7 / 23.9 |
| 3 Triage, 14 red flags | pass, no flags | pass, no flags | pass; soft flag `crowded_period` |
| 4 Flipped baseline (max flag-free flipped SDE 11.7) | pass | pass | pass |
| 5 Known EBs within 2.1′ | pass (none commensurate) | pass (none) | not checked |
| 6 Fit: ρ_free vs ρ_TIC (g/cm³) | mild tension: 0.31 vs 0.60 | **fail**: 0.13 vs 1.71 (dip far too long) | **fail**: 0.70 vs 3.07 |
| 7 Hold-out seasons | pass, 4/4 | **fail**, 2/3 (2021 season: nothing at predicted times) | pass, 4/4 |
| 8 **Pixels**: missing-light offset | **fail**: 33.0″ N (38.7σ), onto Gaia DR3 1820410137384323584 (G = 17.0), which needs a ~28% eclipse | **fail**: 47.1″ SE (21.6σ), onto Gaia DR3 3323296950337617408 (G = 15.7), ~24% eclipse | **fail**: 13.9″ SW (3.4σ), consistent with Gaia DR3 5530349118981595136 (G = 16.6, 12″), ~6% eclipse |
| 9 NASA (SPOC) vs MIT (QLP) | **fail**: SPOC 125 ± 12 ppm, consistent per sector; QLP inconsistent per sector | **fail**: 550 vs 372 ppm; sectors disagree | **fail**: SPOC 207 ± 11 ppm; QLP 347 ± 278, inconsistent |
| 10 Host (Gaia RUWE, NSS flag, SIMBAD) | clean: 0.87, single | clean: 0.97, single | clean: 0.93, single |
| **Verdict** | **likely neighbour EB** | **likely neighbour EB** | **likely neighbour EB** |

The host stars themselves look clean and single. In each case the periodic dimming is real, but it's centred on a faint neighbour inside the 21″ TESS pixels, not on the target. Niyati's signal is strictly periodic and passes all four hold-out seasons. That makes it a good candidate *eclipsing binary* on the neighbouring star, which could be reported as such.

## Lessons
1. **The pixel test (checklist step 8) is the decisive cheap test.** Run it before any public claim. We preregistered after steps 1–5 and had to retract.
2. **Beating the false-alarm baseline proves a signal isn't noise. It doesn't prove where the signal comes from.**
3. **Faint neighbours are the risk, not the reassurance.** A dilution-factor argument ("neighbours are 5–6 mag fainter") can't exclude a blend.
4. **Bright stars with strong, unflagged signals should raise suspicion.** NASA's and MIT's pipelines likely had reasons to pass on these.

## How it was done
The pipeline is adapted from [paraschopra/tess-planet-candidates](https://github.com/paraschopra/tess-planet-candidates). Changes in this repo:

- **Target shell:** 60–100 pc instead of < 60 pc (`pipeline/01_targets.py`). The rest of the cuts are unchanged: dwarfs with R < 1.5 R☉, contamination < 0.2, ≥ 3 sectors spanning ≥ 2 yr, FFI-only, expected SNR ≥ 10.
- **Known-host exclusion:** fresh TOI/CTOI/NASA lists, retrieved 2026-10-09.
- **Download robustness:** a network timeout (`pipeline/env.py`) and a hard per-star timeout (`pipeline/02_download.py`).
- **Vetting targets:** `pipeline/vet.py` points at the three signals.
- **Catalog cross-check:** `check_catalogs.py`, against live ExoFOP, the NASA Exoplanet Archive, and EB/variable catalogs.
- **Preregistration package:** `make_package.py`.

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python pipeline/01_targets.py   # then 02_download, 03_search, 05_triage, 06_inverted, 07_fit, 08_holdout 1, 09_products, 10_pixels
```

Light curves (~770 MB) are not in the repo; `02_download.py` re-fetches them from MAST.

## Results in this repo
- `results/targets_searched.csv`: the 1,098 searched stars.
- `results/phase2/signals.csv`, `results/phase2/triage.csv`: every search signal, with red flags.
- `results/phase3/inverted_triage.csv`: the upside-down false-alarm baseline.
- `results/phase3/*_{fit,holdout,pixels,products}.json`, `results/phase3/plots/`: vetting outputs for the three signals.
- `package/TIC*/`: the files originally deposited on Zenodo, now superseded.

## Credits and license
- **Pipeline:** Paras Chopra (MIT).
- **This search and vetting:** Avijit Thawani, with AI coding agents.
- **Data:** all public. NASA TESS via MAST, ESA Gaia, the TESS Input Catalog, ExoFOP, and the NASA Exoplanet Archive.
- **License:** code is MIT (see `LICENSE`); text, figures and data products are CC BY 4.0.
