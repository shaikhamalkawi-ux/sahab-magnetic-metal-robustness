# Sahab V34 full executable reproducibility archive — GitHub only

This archive contains the **full V34 reproducibility inputs, code, source-reconciliation ledger, split-level outputs, and numerical verification** for the historical Sahab / Amman–Airport / Zagreb study. It is distinct from the smaller [public-method example](../public_method/).

**Release file:** [Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip](Sahab_V34_GitHub_Complete_Reproducibility_20261012.zip)

**Size:** 2,155,168 bytes · **SHA-256:** `4971969d21f1ba09741e2551eba952a21ef2bb1d4cd33334066e45cb7e73cb95`

**Contents:** 55 entries, including 54 file payloads and SHA-256 manifest. The archive retains original data and computational results; it excludes confidential peer-review notices, machine `__pycache__` artifacts, unpublished source PDFs, passwords and internal manuscript packaging.

Study inputs: Sahab (48 primary reconciled records from 56 historical rows; 54 identities resolved), Amman–Airport (44), and Zagreb (25 matched surface sites). **Sahab n=48 is not the complete historical n=56 archive.** Original V34 inputs remain locked.

### Reproduce

Extract the ZIP, install `requirements.txt`, and run:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/verify_v34.py
python verify_release.py
```

The archive was independently replayed in a fresh working copy on Python 3.13, obtaining 80/80 SLSQP checks, maximum absolute numerical difference `7.327471962526033e-15`, 5/5 primary split-output byte replay, and 54/54 manifest PASS. The original V34 science and labels have not been altered.

**Source and rights:** See `docs/SOURCE_RIGHTS_AND_CROSSWALK.md` inside the archive. The depositor reports coauthor consent to public availability; source-specific copyright and reuse permissions remain distinct. Zagreb adaptation is attributed to a CC BY 4.0 publication. Do not infer a blanket license on every original record.

**Amman sample-8 note:** Frozen V34 `Fine_LF=246.05` differs from about `224.390243902439` in a separate public Amman reconstructed master; the archived source-definition difference is documented and not silently reconciled.

**Publication:** No article acceptance is claimed. GitHub is the publication location *now*. Zenodo will be considered only after journal acceptance.
