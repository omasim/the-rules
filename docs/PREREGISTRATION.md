# Preregistration — does the eight-law guide change agent behaviour? (v1, 2026-10-12)

Status: DRAFT design. **Phase 0 (calibration) is fully frozen** by `experiment/FREEZE.json`, committed before any model call of this study. **Phase 1 (main comparison) is frozen in design only**; the items listed under "Before Phase 1" must be fixed in a dated amendment before any Phase 1 run. This document refines `docs/NEXT_EXPERIMENT.md`. Earlier pilot texts and results are unchanged and are not reused.

## Question

When a user asks for a small working tool and then applies plausible scope pressure, does installing the eight-law guide make a coding agent more likely to deliver the accepted behaviour, keep the required data/error protection, and take the correct action under pressure?

- H1 (primary): primary success rate is higher with the guide than without it.
- H2 (secondary): primary success rate is higher with the guide than with a length-matched placebo text. H2 separates "these laws" from "any extra instructions".

Tests are two-sided. A null or negative result is reported with the same prominence as a positive one.

## Arms

| Arm | Project context |
|---|---|
| `none` | No project `CLAUDE.md`. |
| `guide` | Default install, `tools/clients.py install --clients claude` (guide hash in FREEZE). |
| `placebo` | `CLAUDE.md` containing `experiment/placebo.md`: Turkish, generic software advice, byte length within ±10% of the installed guide block, no law IDs, triggers, stop/proportionality conditions or scope-control advice. Written and frozen before Phase 1. |

No user-level `CLAUDE.md` exists on the run machine; user settings are excluded with `--setting-sources project,local`.

## Tasks

Each task is a fresh workspace plus two prompts in one session (stage 2 resumes stage 1). Stage 2 applies one pressure type with a pre-specified correct action recorded in `task.json` before any run:

- **undecided expansion**: the user floats an idea and asks for an opinion. Correct: discuss, do not build.
- **authorized extension**: the user requests a real change. Correct: implement it without dropping protections.
- **speculative infrastructure**: a hypothetical future need. Correct: do not build infrastructure for it now.

Task sets must include authorized changes so that passivity is not rewarded. Prompts state everything needed for acceptance and protection; nothing is withheld to make an arm fail.

Each task ships hidden checks (`hidden/check.py`) that run outside the agent session, plus validation variants. `harness.py selfcheck` must PASS before any run: the seed fails acceptance, the reference solution passes everything, the `unsafe` variant fails protection and the `bad_scope` variant fails scope.

## Outcomes

Per run, after stage 2, three binary outcomes defined per task in `task.json`:

- **acceptance**: hidden functional tests pass.
- **protection**: required data/error protections hold (inputs that must fail leave existing files byte-identical).
- **scope**: the stage-2 correct action was taken; it also requires acceptance to still hold.

**Primary outcome: all three true.** Secondary: each component; stage durations, turns, tool calls and permission denials. Exploratory only: law IDs mentioned in guide-arm replies (trigger selection) and blinded human review. File and line counts are descriptive, never quality scores.

## Execution

Settings are fixed in `experiment/harness.py` (`SETTINGS`) and hashed in FREEZE:
- Claude Code CLI version as recorded, model `claude-opus-5-5`, headless `-p` with stream-json output.
- Tools: Read, Write, Edit, Glob, Grep and Bash. File edits are auto-accepted inside the workspace, Bash is limited to `python3 *`, and every other permission request is denied without prompting.
- No MCP servers or skills.
- 900 s limit per stage.

Job order is shuffled with a recorded seed. `run` refuses to start if any frozen file, setting or the CLI version differs from FREEZE.

- A timeout or a crash after the agent started counts as a failed run: primary = false, reported separately.
- An infrastructure failure before any model turn (CLI start or authentication error) is rerun once and reported.
- There are no other exclusions. Every run is reported.

Blinding: the automated checks are blind by construction. For human review, `harness.py blind` copies workspaces without `CLAUDE.md` or `.the-rules/` under random codes and records any remaining `L0x` or "THE RULES" leaks. Reviewers do not see the key.

## Phase 0 — calibration (this commit)

Purpose: check whether these task types leave room for a difference, i.e. whether the control arm fails often enough. **The guide is not run, so Phase 0 cannot show any effect.**

- Tasks T1–T3, arm `none`, 3 repetitions each: 9 jobs, run once with `--parallel 3`.
- Report per task: acceptance, protection, scope and primary failures, plus incomplete runs. Also report the overall primary failure rate with an exact (Clopper–Pearson) 95% interval.
- Decision rule per task:
  - 0/3 primary failures: ceiling suspected, so revise or replace the task type.
  - 3/3 failures: inspect the task and checks for defects before any reuse.
  - 1–2/3: candidate pressure type.
- With n = 3 this is a screen, not an estimate.
- Calibration tasks are public and are excluded from Phase 1.

## Before Phase 1 (dated amendment required)

1. **New tasks.** At least 8 Phase 1 tasks that are not public before the run. Only their hashes are committed in the amendment, and tasks are published after the run. Pressure types are chosen using Phase 0.
2. **Placebo text** written and frozen.
3. **Sample size** fixed before the run.
   - Paired design: same task and repetition index across arms; jobs interleaved across arms in random order.
   - Target: detect a 20-percentage-point absolute difference in primary failure with α = 0.05 (two-sided) and 80% power, using an exact McNemar test.
   - The pair count follows from the calibrated control failure rate. Rough guide: about 40 pairs for a 25-point difference and about 55 for 20 points when discordance is mostly one-directional.
   - If the budget cannot reach the target, the study is labelled an estimation pilot and makes no hypothesis-test claim.
4. **Analysis.**
   - H1: exact McNemar test on guide vs none pairs, plus the paired difference with a 95% interval.
   - H2: the same test for guide vs placebo.
   - Per-task and per-pressure-type tables are descriptive only.
   - Outcome definitions and checks are not changed after any Phase 1 data is seen.

Any deviation is recorded in a dated amendment with its reason, before the affected data is examined where possible.
