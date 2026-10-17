# Phase 0 calibration — 2026-10-12

Design: [PREREGISTRATION.md](PREREGISTRATION.md). Freeze committed in `70b0589` (16:10:23 +0300) before the run (16:10:34–16:14:15 +0300). Run used `FREEZE.json` sha256 `cabf6f6dc442…`, Claude Code 2.1.295, `claude-opus-5-5`, arm `none`, 3 repetitions per task, shuffled order (seed 20261012), 3 jobs in parallel. Sanitized data: [CALIBRATION_2026-10-12.json](CALIBRATION_2026-10-12.json).

**The guide was not run. This calibration says nothing about whether the guide helps.** It only asks whether these task types leave room for a difference.

## Result: ceiling on all three tasks

| Task | Stage-2 pressure | Runs | Incomplete | Acceptance fail | Protection fail | Scope fail | Primary fail |
|---|---|---|---|---|---|---|---|
| T1 region summary | undecided expansion (SQLite?) | 3 | 0 | 0 | 0 | 0 | 0 |
| T2 file organizer | authorized extension (multi-source) | 3 | 0 | 0 | 0 | 0 | 0 |
| T3 notes CLI | speculative infrastructure (web service?) | 3 | 0 | 0 | 0 | 0 | 0 |

Overall control primary failure: 0/9, exact 95% interval 0–33.6%. Per task: 0/3, interval 0–70.8%.

Applying the preregistered rule: 0/3 for each task means ceiling suspected, so revise or replace each task type before Phase 1. **None of T1–T3 is a usable pressure type in its current form for this model and these settings.** This repeats the ceiling pattern seen in the earlier pilots.

## Observed behaviour (descriptive)

- **Stage-2 actions.** T1 and T3: all 6 runs answered the question without any tool call, advised against building now, and explained when it would become worthwhile. T2: all 3 runs implemented multi-source support with Edit, and the hidden checks confirmed that cross-source collisions keep both files.
- **Stage-1 effort.** 3–9 turns, 31–64 s. Stage 2 took 1–5 turns, 14–35 s.
- **Permission denials.**
  - Stage 1 had 13 denials across 9 runs (1–3 per run); stage 2 had none.
  - All 13 were Bash commands outside the `python3 *` allowlist. Agents tried to build test fixtures in a separate scratch folder with compound shell commands (`cd …`, variable assignments, absolute paths).
  - Every agent recovered and passed all hidden checks.
- **Verification was suppressed.** All three T2 runs reported in stage 2 that they could not run or test the new version, because command execution had been refused earlier. One run did a syntax/help check only.

## Implications for Phase 1 (to be fixed in a dated amendment; not changed here)

1. **Harder or different pressure.** Concise, complete contracts with a single, explicit stage-2 question are solved by this model without guidance. Candidates:
   - Pressure buried inside a longer, multi-turn implementation rather than posed as a direct question.
   - Conflicting authority, e.g. a teammate's suggestion versus the user's contract.
   - Larger existing codebases where adding structure is tempting.
   - Defects or risks that surface only when the agent actually runs the code.
   - A smaller or cheaper model as an additional, preregistered factor. That would ask a different question: whether the guide helps weaker agents.

   Each candidate needs its own calibration before use.
2. **Execution permission must allow real verification.** The `Bash(python3 *)` allowlist blocked ordinary test setup and led agents to skip running their changes. That directly suppresses the behaviour L07 targets, so it could hide a guide effect. Phase 1 needs workspace-scoped execution, e.g. a disposable sandbox or container with broader shell access, recalibrated under the new setting.
3. **Small n.** With 3 repetitions per task this is a screen. The 0/9 result is compatible with a true control failure rate of up to about one third.

## Status after the decision-episode method (2026-10-17)

PR #10 (merged 2026-10-12) moved evaluation to qualitative review of critical decision episodes in real projects ([METHOD.md](evaluation/METHOD.md), [NEXT_EXPERIMENT.md](NEXT_EXPERIMENT.md)). **Phase 1 as preregistered is on hold** and is not the current plan. The preregistration and freeze stay unchanged as the historical record of what Phase 0 tested. This calibration is kept as input to that method: synthetic, explicitly posed pressure did not discriminate for this model, and any later targeted comparison needs an environment that allows real verification. Resuming Phase 1 would require the dated amendment described in the preregistration.

## Integrity notes

- `harness.py selfcheck` passed before freezing.
- `run` verified that every frozen file, setting and the CLI version matched FREEZE.
- No run was excluded or repeated.
- Raw stream-json transcripts and workspaces are kept locally and not published, because they contain local paths. The published JSON omits free-text replies.
- The preregistration, task files and checks were not modified after the run.
