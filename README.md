# THE RULES

An experimental, source-traced working guide for AI-assisted software projects. Research the real problem, test the critical assumption, set enough scope, build the narrow working flow, verify it, and deliver. Each core law includes a trigger and a proportionality/stop condition.

**DRAFT / advisory. Additional quality or speed benefit has not been demonstrated.** This is a working-style guide, not a proven productivity system, enforced policy, or grant of authority. [Evidence and negative results](docs/EVIDENCE.md).

[ Türkçe ](README.tr.md)

## What you install

Eight core laws in `guide/core.json`. The guide carries no frozen project task or phase. Current task, acceptance, phase and decision gaps come from the live user request and project evidence. Apply only the laws that affect the next decision; do not restart a full lifecycle or create documents for every small edit. Agent selection of the right trigger is itself unverified.

The installable guide is Turkish. English documentation explains the interface; an English law translation is not yet available. Actual UTF-8 byte size is reported by `guide_check.py`; tokens and effectiveness are not inferred from size.

## One project installer

Python 3.9+, standard library only. From a reviewed checkout:

```sh
python3 -B tools/clients.py install --project /absolute/path/to/project --clients claude,cursor,antigravity
python3 -B tools/clients.py verify --project /absolute/path/to/project
python3 -B tools/clients.py remove --project /absolute/path/to/project
```

Use a single name if needed. For Codex use the same installer with `--clients codex`. Do not combine Codex with Cursor/Antigravity in one installation: shared AGENTS.md discovery could duplicate context.

| Client | Project file |
|---|---|
| Claude Code | Managed section appended to CLAUDE.md |
| Cursor | .cursor/rules/the-rules.mdc |
| Antigravity | .agents/rules/the-rules.md |
| Codex | Managed section appended to AGENTS.md |

The eight-law text is embedded in each adapter. Existing user text is preserved; existing dedicated rule files are refused. Installation, repeat installation, integrity verification and guarded removal use one state format. Only installer-created empty directories are cleaned. Modified files and unexpected integration files are preserved with an error. Global settings and accounts are untouched. Use project version control; no crash-safe multi-file or concurrent-install guarantee is made.

## Existing installations

No automatic migration or overwrite. The old two-law profile installer remains an explicitly deprecated `--context` compatibility mode; it is not the recommended product. Remove a previous installation with its corresponding verified tool, then install the guide. `integrate.py` is a compatibility entry point: new Codex installs delegate to clients.py; legacy integration.json verification/removal uses a retained cleanup engine. Old catalog/profile tools remain for research reproducibility. [Migration](docs/MIGRATION_0.14.md).

## Research archive, not the installed product

`library/` preserves 236 unratified detail/control records plus the eight historical core records, with source trace. `profiles/` preserves the old explicit two-law mappings. They are a research/candidate archive, not a promise that every record reaches the model or has been adopted. They are not loaded by the default guide installation. [Archive status](library/README.md).

## Verification and limits

```sh
python3 -B tools/check.py
python3 -B tools/integration_check.py
python3 -B tools/clients_check.py
python3 -B tools/portability_check.py
python3 -B tools/stdout_check.py
python3 -B tools/guide_check.py
python3 -B tools/verify_package.py
```

CI runs all seven on Ubuntu and Windows/Python 3.9. Prior client-loading evidence applies to the old two-law build profile: Claude Code PASS (tools disabled), Antigravity PASS (limited), Cursor NOT RUN. **New eight-law guide: Claude Code PASS (user-reported, tools-disabled comparative loading test); Antigravity PASS (limited) in a fresh installed/uninstalled UI comparison; Cursor and Codex NOT RUN.** Loading is not rule compliance or improved output. Prior pilot findings remain unchanged.

Distribution candidate 0.14.1-draft; new guide content 0.14; historical catalog 0.3 and profiles 0.11 are unchanged. No public license is granted, as explicitly chosen by the owner; this is not an open-source licensing claim. [Rights](NOTICE.md), [contributions](CONTRIBUTING.md), [next experiment proposal](docs/NEXT_EXPERIMENT.md).

Installed default guide metadata is advisory/nonbinding. Source mappings travel with the installation as context/provenance.json; original private source documents are not included. See docs/GUIDE_METADATA.md.

Evaluation now focuses on [critical decision episodes](docs/evaluation/METHOD.md): preserve the frame while incorporating legitimate change, compare reasons/actions/results, and disclose uncertainty without a composite productivity score. [Retrospective examples](docs/evaluation/RETROSPECTIVE_EXAMPLES.md) are exploratory, unblinded and not an effectiveness claim.
