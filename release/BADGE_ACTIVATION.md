# Badge activation record

The workflow badges report runs on public `main`. At the Version 1.0.1 commit `f9d3df8` all workflows passed: runs 45713425449 (verify), 45713425521 (replay), 45713425657 (PDF).

The DOI badge uses the version DOI 10.5281/zenodo.24544624 because it cites the exact archived Version 1.0.1. The concept DOI is linked in the README citation section. The DOI badge was added only after both DOIs resolved and the archived file matched the GitHub source archive of tag `v1.0.1` (see `DOI_DEPOSIT.md`).

Before this update was committed, the DOI badge image was fetched from Zenodo without credentials. It returned HTTP 200 and shows the version DOI. The workflow badge states are taken from the runs listed above.
