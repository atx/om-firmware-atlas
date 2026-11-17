# Read a status with its evidence

The Atlas stores capability assertions separately from observations. Each assertion names a camera, firmware, project and mod build, then links supporting or contradicting evidence. [Browse the observations](../views/evidence/index.md).

| Information | What it establishes |
|---|---|
| Published release | A project made something available; test coverage is a separate question |
| Inspected implementation | A stated code/data finding under the inspected scope |
| Emulator observation | Specific behaviour under the named emulator, revision, model, scenario and stand-ins |
| Physical-camera report | What a reporter says happened on the identified camera/package |
| Report completeness | Whether identity, steps, dates and outcomes were actually supplied |
| Recovery observation | Restoration from one particular failed state, not every possible failure |

A partial report can still be useful. For example, a release label and overall owner result can be retained while the package hash or procedure remains unknown. An expected manifest digest is not a reported or observed installed-package digest. The date a comment was posted is not automatically the date of the test.

“Complete” is a documentation label, not an independent reproduction or safety guarantee. Complete physical reports require exact target/build, a reported or observed package hash, procedure, explicit test date and outcome. One camera report remains one report.

## Conflicting observations

Compare model, firmware, package, configuration, test method and date before deciding there is a disagreement. Retain both when the difference is unresolved. Newer text does not automatically replace older direct evidence. Historical failures remain useful after later packages succeed.

The Atlas uses precise descriptions rather than a single green “supported” badge. “No evidence catalogued” means unknown. It does not mean a test failed or nobody is working on the feature.

For an example, compare [the original OM-5 startup report](../views/evidence/om5-prealpha1-boot.md) with [the Mark II alpha12 owner report](../views/evidence/om5-ii-alpha12-owner.md).
