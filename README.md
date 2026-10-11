# THE RULES

A source-traced rule library for AI-assisted software work: research the problem, test critical assumptions, define a sufficient scope, build a working prototype, verify it, and deliver it without unnecessary planning or architecture.

**Experimental / DRAFT.** Local adapters are available for Claude Code, Cursor, Google Antigravity, and Codex. The library does not grant additional authority or enforce model behavior. Our pilots have **not demonstrated an additional quality or speed benefit** from adding THE RULES.

[ Türkçe / Turkish ](README.tr.md)

## Start with two relevant laws

| Phase | Profile | Laws |
|---|---|---|
| Research a problem or idea | discover | L01, L02 |
| Define acceptance and scope | frame | L02, L03 |
| Build the first real flow | build | L04, L05 |
| Handle a defect or proposed change | change | L05, L06 |
| Verify and deliver | deliver | L07, L08 |

The full catalog contains 244 draft records: eight core laws and 236 retained synthesis/control records. Selecting a profile does not delete or ratify other records. Context content is currently Turkish; this README provides English navigation.

## Install into a project

Python 3.9+, standard library only. Clone this repository, select a reviewed commit, and run commands from this checkout. Do not run unreviewed remote scripts. First edit `examples/build.json` with your actual task and decision gap.

```sh
python3 -B tools/clients.py install --project /absolute/path/to/project --context examples/build.json --clients claude,cursor,antigravity
python3 -B tools/clients.py verify --project /absolute/path/to/project
```

Use a single client name if needed. Claude Code appends a managed section to `CLAUDE.md`; Cursor creates `.cursor/rules/the-rules.mdc`; Antigravity creates `.agents/rules/the-rules.md`. The selected short content is embedded directly. Existing user rules are preserved; conflicting managed paths are refused.

For Codex, choose this installer instead:

```sh
python3 -B tools/integrate.py install --project /absolute/path/to/project --context examples/build.json --agents
python3 -B tools/integrate.py verify --project /absolute/path/to/project
```

Both installers use `.the-rules/`; do not stack them. Shared AGENTS.md discovery may otherwise duplicate guidance. Installation is project-local and does not change global settings or accounts.

## Remove or switch

```sh
python3 -B tools/clients.py remove --project /absolute/path/to/project
# For an installation made with integrate.py:
python3 -B tools/integrate.py remove --project /absolute/path/to/project
```

Removal restores original files only when installed files are unchanged. Modified adapters, extra files, symlinks, or conflicting paths cause a refusal so work is preserved. Switching profile or client set requires reviewing/removing the old installation first. Version-control your project: the installer does not promise crash-safe multi-file transactions or concurrent-install safety.

## Check the package

```sh
python3 -B tools/check.py
python3 -B tools/integration_check.py
python3 -B tools/clients_check.py
python3 -B tools/portability_check.py
python3 -B tools/verify_package.py
```

These check selection, source integrity, local install, repeat install, and restoration in temporary projects. They do not start AI models. [Client documentation](docs/CLIENT_COMPATIBILITY.md) and [live loading check](docs/CLIENT_SMOKE.md) explain what remains to verify.

## Evidence and limitations

[Evidence summary](docs/EVIDENCE.md) reports successful local integration checks and three pilot families. Live loading in the three new clients and live GitHub download are not yet verified. A rule file is guidance, not a security boundary. We publish limitations and negative results alongside intended behavior.

## Status and rights

Distribution candidate: `v0.13.1-draft`; profile content: `0.11.0-draft`; catalog content: `0.3.0-draft`. No public license has been granted yet. Public visibility does not mean permission to redistribute or reuse under MIT or another open-source license. Third-party sources retain their own rights. See [rights notice](NOTICE.md).

Contributions: [CONTRIBUTING.md](CONTRIBUTING.md). Changes to laws remain proposals until explicitly adopted.

Portability: tracked text stays LF with `.gitattributes`; generated text explicitly uses UTF-8/LF. CP1252 and CRLF behavior are simulated in regression tests; native Windows execution remains unverified. Removal cleans only empty directories created by the installer, preserving existing directories and added user files.
