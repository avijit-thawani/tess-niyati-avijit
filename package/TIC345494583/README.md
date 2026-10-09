# Preregistered transit predictions: TESS planet-candidate signal "Niyati" on HD 354088 (TIC 345494583)

**Status: unvetted candidate signal.** Found 2026-10-09 in a blind search; detailed vetting (transit fit, hold-out seasons, second reduction, pixel-level centroids) is in progress. This record exists to timestamp the detection and the predictions below before any further data are taken. "Niyati" (Sanskrit: "destiny") is an informal nickname, not an IAU name.

## The star
| | |
|---|---|
| Names | HD 354088 = HIP 97983 = TIC 345494583 = Gaia DR3 1820410141709587712 = TYC 1620-2297-1 |
| Position (ICRS) | RA 298.698762°, Dec +17.119072° (Sagitta) |
| Type | G0 dwarf, Teff ≈ 6000 K, R ≈ 1.38 R☉, M ≈ 1.11 M☉ (TIC v8.2) |
| Brightness / distance | TESS mag 7.93; 79.7 pc (260 ly) |

## The signal
| | |
|---|---|
| Period | 2.901451 d (rough ±0.00006 d) |
| Reference mid-transit | BJD_TDB 2458685.7484 (rough ±0.036 d) |
| Depth / duration | ≈106 ppm / ≈3.5 h |
| Implied radius | ≈1.6 R⊕ (if on the target star, undiluted) |
| Transits in data | 31, across 4 TESS sectors spanning 5.1 years |
| Detection strength | BLS SDE 15.9; empirical (red-noise) SNR 11.9 |
| Automatic red flags | none of 14 (odd/even, secondary eclipse, variability, sector consistency, TESS-orbit alias, single-event dominance, etc.) |

## Search
Box-least-squares search of TESS-SPOC (else QLP) full-frame-image light curves of 1,098 dwarf stars at 60–100 pc never observed at 2-minute cadence, excluding known planet hosts, TOIs and CTOIs (lists retrieved 2026-10-09). Pipeline adapted from github.com/paraschopra/tess-planet-candidates.

**False-alarm baseline:** the identical search and triage on all 1,098 light curves flipped upside down produced no flag-free signal above SDE 11.7. This signal (15.9) and two others in the real survey exceed that.

## Checked against catalogs (2026-10-09)
Not in the ExoFOP TOI or CTOI lists or the NASA Exoplanet Archive. SIMBAD lists it as a high-proper-motion G0 star, with no binary classification. No catalogued eclipsing binary within 2.1′ has a period commensurate with 2.9015 d. The nearest is Gaia DR3 1820410137384323456: G ≈ 16.9, 31″ away, P = 3.783 d.

## Main caveats
- **Crowding:** this is a crowded field near the galactic plane, with TESS pixels of 21″. A faint eclipsing binary inside the aperture could mimic the signal.
- **Detection by NASA and MIT:** the star is bright. Why their own searches did not flag it has not yet been established.
- **Timing uncertainties:** these are rough, taken from the search rather than an MCMC fit. A fitted update will be posted as a new version of this record.

## Files
- `candidate.json`: the parameters above, machine-readable.
- `345494583_predicted_transits.csv`: predicted mid-transit times to the end of 2028, in BJD_TDB and UTC, with 1σ and ±3σ windows.
