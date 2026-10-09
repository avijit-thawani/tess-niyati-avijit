# Preregistered transit predictions: TESS planet-candidate signal "Avijit" on TYC 717-2552-1 (TIC 156733696)

**Status: unvetted candidate signal.** Found 2026-10-09 in a blind search; detailed vetting (transit fit, hold-out seasons, second reduction, pixel-level centroids) is in progress. This record exists to timestamp the detection and the predictions below before any further data are taken. "Avijit" (Sanskrit: "unconquered") is an informal nickname, not an IAU name.

## The star
| | |
|---|---|
| Names | TYC 717-2552-1 = TIC 156733696 = Gaia DR3 3323297706251675648 = 2MASS J06041995+0830063 |
| Position (ICRS) | RA 91.083178°, Dec +8.501749° (Orion) |
| Type | Sun-like dwarf, Teff ≈ 5700 K, R ≈ 0.94 R☉, M ≈ 1.02 M☉ (TIC v8.2) |
| Brightness / distance | TESS mag 8.75; 73.4 pc (239 ly) |

## The signal
| | |
|---|---|
| Period | 1.817187 d (rough ±0.00003 d) |
| Reference mid-transit | BJD_TDB 2458468.4809 (rough ±0.034 d) |
| Depth / duration | ≈466 ppm / ≈3.3 h |
| Implied radius | ≈2.3 R⊕ (if on the target star, undiluted) |
| Transits in data | 38, across 3 TESS sectors spanning 6.1 years |
| Detection strength | BLS SDE 15.4; empirical (red-noise) SNR 10.2 |
| Automatic red flags | none of 14 (odd/even, secondary eclipse, variability, sector consistency, TESS-orbit alias, single-event dominance, etc.) |

## Search
Box-least-squares search of TESS-SPOC (else QLP) full-frame-image light curves of 1,098 dwarf stars at 60–100 pc never observed at 2-minute cadence, excluding known planet hosts, TOIs and CTOIs (lists retrieved 2026-10-09). Pipeline adapted from github.com/paraschopra/tess-planet-candidates.

**False-alarm baseline:** the identical search and triage on all 1,098 light curves flipped upside down produced no flag-free signal above SDE 11.7. This signal (15.4) and two others in the real survey exceed that.

## Checked against catalogs (2026-10-09)
- Not in the ExoFOP TOI or CTOI lists or the NASA Exoplanet Archive.
- SIMBAD lists it as a high-proper-motion star, with no binary classification.
- No catalogued eclipsing binary or variable star (TESS EB catalogs, Gaia DR3 eclipsing and orbital binaries, AAVSO VSX) within 2.1′.

## Main caveats
- **Duration:** the 3.3 h dip is about 1.5× the longest central transit expected for a 1.82 d orbit around a star of this density. That is within the triage limit, but it is a known signature of blended eclipsing binaries, or of a wrong stellar radius. The transit fit will test it.
- **Detection by NASA and MIT:** the star is bright. Why their own searches did not flag it has not yet been established.
- **Timing uncertainties:** these are rough, taken from the search rather than an MCMC fit. A fitted update will be posted as a new version of this record.

## Files
- `candidate.json`: the parameters above, machine-readable.
- `156733696_predicted_transits.csv`: predicted mid-transit times to the end of 2028, in BJD_TDB and UTC, with 1σ and ±3σ windows.
