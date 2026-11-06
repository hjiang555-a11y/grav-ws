# Exact-frequency verification — no numerical change

During final code inspection, nearest-index lookup raised a concern that nominal-frequency tables might use nearby grid points. Explicit recalculation established that the inherited annual grid already contained all five exact frequencies. The original and rechecked spectral, nominal-frequency and temporal tables are byte-identical. There was no numerical or unit-conversion error.

The rechecked version at `../diurnal_spectrum_exact_20261106T1105Z/` adds explicit frequency assertions and retains the same results. Its final private delivery is under `reports/diurnal_spectrum_exact_codex_20261106T1105Z/`. The earlier upload was interrupted after the first figure files, before report delivery; these figures remain valid.

The preliminary concern and its correction are retained in the local verification trail. Use the complete rechecked delivery for convenient access.
