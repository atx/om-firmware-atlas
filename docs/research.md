# Start with the work that already exists

First choose the [exact camera and generation](../views/cameras/index.md). Check the firmware identity, related projects and known gaps. Shared code or a similar model name is a research lead; it does not make an existing patch portable.

## Choose a task

| You want to… | Start here |
|---|---|
| Identify or unpack firmware | [Identity and containers](../knowledge/platform/identity.md) |
| Understand patch construction | [Patching methods](../knowledge/methods/patching.md) |
| Trace or decompile code | [Analysis tool profiles](../knowledge/tooling/analysis.md) |
| Exercise firmware outside a camera | [Emulation coverage](../knowledge/emulation/coverage.md) |
| Move or add film looks | [Looks and interfaces](../knowledge/interfaces/looks.md) |
| Compare related bodies | [Cross-model reasoning](../knowledge/comparisons/models.md) |

## Choose a contribution home

For an existing mod, use its repository and contribution process. For an emulator/tool defect, use its implementation owner and identify the exact fork/revision. For a shared-interface change, check current consumers and maintainer policy; a consolidation proposal is not automatically an agreement.

Use the Atlas for cross-project explanations, source records and scoped evidence. Before recommending a new repository, inspect existing branches, issues and related attempts and explain why those homes do not fit. The [project directory](../views/projects/index.md) gives starting destinations, not an ownership ruling.

AI contributors should follow [AGENTS.md](../AGENTS.md). These routes can be read without installing a firmware toolchain; the documentation scripts are optional aids for reading and required for validating edits.
