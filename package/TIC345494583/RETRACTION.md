# Retraction (version 2, 2026-10-13): "Niyati" on HD 354088 (TIC 345494583)

**The signal is retracted as a planet candidate on HD 354088.**

Vetting completed after version 1 (2026-10-09) shows that the periodic dimming is real, but it is not on the target star:

- **Pixel-level difference imaging** (4 sectors, 24 transits) places the missing light **33.0″ north of the target (38.7σ)**. That is on or near the faint neighbour Gaia DR3 1820410137384323584 (G = 17.0, 32.6″), which fits better than the target by Δχ² = 199. Making the observed dip would need a ~28% eclipse on that star, which is typical of an eclipsing binary. The measured depth also rises with aperture size, as expected for an off-target source.
- **Second reduction:** MIT QLP does not reproduce the NASA TESS-SPOC depth consistently from sector to sector.
- **Transit fit:** the dip is slightly too long for HD 354088, with free-fit stellar density 0.31 vs 0.60 g/cm³ catalogued.
- **Unaffected:** the host star itself looks clean, with Gaia RUWE 0.87 and no non-single-star flag. The period is recovered in all four held-out seasons.

**Most likely explanation:** an eclipsing binary at the neighbour's position, blended into the 21″ TESS pixels. The predicted times in version 1 remain valid as predictions *for that signal*, wherever it originates.

Full vetting outputs and the checklist used are at https://github.com/avijit-thawani/tess-niyati-avijit
