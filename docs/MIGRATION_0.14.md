# Transition to the working guide — DRAFT

New installs: clients.py with explicit --clients and no --context. All four adapters use the same engine. No fixed phase/task is written to the install state. Future task changes require no reinstall.

Existing clients.json: verify and remove with clients.py; altered files remain protected. Existing Codex integration.json: integrate.py verify/remove delegates to legacy cleanup. The old implementation remains only for compatibility; new Codex installs use the shared engine. Preserve original tools/checkout if manually changed state requires reconciliation. There is no in-place automatic migration.

Old --context profile selection is retained as deprecated compatibility for old commands and regression tests. It remains a frozen-profile mode, not the new product. Profiles and full catalog are retained as research archive. Explicit client-set changes still require removal/reinstall to preserve ownership boundaries; this is separate from live task/phase changes.

New eight-law client behavior has not been live tested. Old two-law evidence remains historical and must not be relabeled as proof of the new guide.
