# Vetting checklist for a TESS planet-candidate search

Run every step, in order, **before** any public claim, preregistration, social post or nickname. A signal must pass every **gate**. Steps marked *(info)* add context, but a failure there is not on its own a reason to drop the signal.

This search learned the order the hard way. Two signals were preregistered after passing steps 1–5. Then step 8 (pixels) put both on faint neighbours. Run step 8 before step 11.

| # | Step | Tool | Pass if | Typical kill |
|---|---|---|---|---|
| 1 | **Novelty**: target is not a known host or candidate | live ExoFOP TOI and CTOI lists, NASA Exoplanet Archive (`ps`), all fetched on the day; `pipeline/01_targets.py`, `check_catalogs.py` | TIC absent from all three | Already a TOI or CTOI, or a known planet |
| 2 | **Blind detection**: the signal comes out of a search that wasn't told the period | `03_search.py` (BLS, 0.5–25 d) | SDE ≥ 7, SNR ≥ 6, ≥ 3 transits with data | (n/a, this is the detection) |
| 3 | **Red-flag triage**: 14 automatic impostor tests | `05_triage.py` | No hard flags. Soft flags, such as `crowded_period` at < 1 d, need a reason to keep | odd/even mismatch, secondary eclipse, variability repeat, TESS-orbit alias, one or few events dominate, inconsistent sectors, too long or too deep |
| 4 | **False-alarm baseline**: flip every light curve upside down and rerun steps 2–3 | `06_inverted.py`, then `05_triage.py` on the flipped stars | Candidate SDE is above the strongest flag-free *flipped* signal across the whole survey | Weaker than chance produces |
| 5 | **Known-binary cross-match**: eclipsing binaries and variable stars within ~6 TESS pixels | `check_catalogs.py` (TESS EB catalogs, Gaia DR3 `vari_eclipsing_binary` and NSS, AAVSO VSX) | No neighbour with a period equal to, or a simple ratio of, the candidate's period (1:1, 1:2, 2:1, 2:3, 3:2) | Commensurate EB nearby |
| 6 | **Transit fit and stellar density**: shape and duration fit a planet around *this* star | `07_fit.py` (MCMC, batman) | Transit vs flat Δχ² ≳ 30; flat-bottomed (not V); free-fit density within ~2σ of the TIC density | Dip far too long for the star (density ≪ catalog, e.g. 0.13 vs 1.71 g/cm³); V-shaped |
| 7 | **Hold-out seasons**: hide each year, predict it from the rest | `08_holdout.py` | Blind period matches, and hidden-season depth ≥ 3σ at predicted times, in every season (allow one weak season if the others are strong) | Hidden season shows nothing at predicted times, or the timing drifts by hours |
| 8 | **Pixel difference imaging**: *where* the light goes missing | `10_pixels.py` | Missing-light centroid consistent with the target (< 3σ offset), and no neighbour fits better than the target; depth not rising with aperture size | **Offset onto a faint neighbour**: all three signals here, at 33″ (38.7σ), 47″ (21.6σ), 14″ (3.4σ) |
| 9 | **Second reduction**: NASA (TESS-SPOC) vs MIT (QLP) | `09_products.py` | Depths agree within ~2σ, and agree sector by sector | Present in only one pipeline; scattered per-sector depths |
| 10 | **Host star sanity** *(info)* | Gaia DR3: parallax, RUWE, `non_single_star`; SIMBAD object type | RUWE < 1.4; not a known spectroscopic binary; distance and size match the TIC | RUWE ≫ 1.4 (unresolved companion), so the radius and density are unreliable |
| 11 | **Preregister**, only after 1–10 pass | Zenodo: summary, fitted ephemeris, predicted transit times | (n/a) | (n/a) |
| 12 | **Statistical validation** *(before calling it a "strong" candidate)* | TRICERATOPS (`12_triceratops.py`) | False-positive probability < 1.5% and nearby-false-positive probability < 0.1% (validation thresholds) | High nearby-EB probability |
| 13 | **Publish, then report** | RNAAS note, then ExoFOP Published Candidate Upload Request, then CTOI | (n/a) | (n/a) |

## Rules of thumb
- **Faint neighbours are the risk, not the reassurance.** A neighbour 6 mag fainter supplies ~0.4% of the light, so a 10% eclipse on it fakes a ~400 ppm dip. Summing neighbour flux (a dilution factor) says how much a neighbour *could* fake; only step 8 (or ground-based imaging) says whether one *does*.
- **A bright star with a strong signal that NASA's and MIT's own searches missed** deserves extra suspicion, not excitement. Find out why it was missed before claiming it.
- **A strictly periodic signal that passes the hold-out test is still not proof it's on the target.** Eclipsing binaries are periodic too.
- **Don't trust headline SDE alone.** Flipped data reached SDE 34.6 before triage. The comparison that counts is flag-free vs flag-free.
- **Retract in public, the same way you claimed.** Publish a new Zenodo version and correct the README. Keep the original timestamp as the record.

## Gate log template
Copy one block per signal into the results README.

```
TIC ___________  P = ______ d  depth = ____ ppm  Rp = ____ R⊕
 1 novelty            PASS / FAIL  (lists dated ____)
 2 blind detection    SDE ____  SNR ____  N_tr ____
 3 triage             hard flags: ____   soft: ____
 4 flipped baseline   max flag-free flipped SDE ____   candidate ____
 5 known EBs          nearest commensurate: ____
 6 fit                Δχ² ____  b ____  ρ_free/ρ_TIC ____
 7 hold-out           seasons passed __ / __
 8 pixels             offset ____″ (____σ)  best neighbour Δχ² ____
 9 SPOC vs QLP        ____ vs ____ ppm
10 host               RUWE ____  SIMBAD ____
VERDICT: candidate / likely false positive (reason) / inconclusive
```
