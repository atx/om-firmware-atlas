# Update a scoped status

Preconditions: exact camera, firmware/project/build scope and a source for the observation. Read the affected camera/project routes and [evidence rules](../../docs/evidence.md).

Add or correct the observation before its capability assertion. Distinguish physical camera, emulator and static methods. Emulator evidence needs the emulator's repository, revision, model and stand-ins; when a maintainer reports runs on an unpublished emulator, record them in the coverage and limitations of their maintainer-summary evidence instead. Record actual steps, outcome, identity strength and missing details. A manifest's expected digest cannot fill a reported/observed package field. A posted date is not an unstated physical test date.

Preserve older failures and supersession reasons. Do not carry results to another model or package. Link contradictory evidence and narrow the assertion when scope differs. Generate and inspect camera, evidence and source pages together, run the checks and submit a PR.
