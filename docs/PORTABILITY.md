# Portability patch 0.13.1-draft

Confirmed before fix: a Git checkout with core.autocrlf=true failed package hashes. Fix: explicit LF checkout attributes, explicit UTF-8 reads and UTF-8/LF writes for Python 3.9+. Encoding alone would not prevent Windows write newline translation; textio.write_utf8 sets newline explicitly.

Shared distribution version now covers both installers. Profile 0.11 and catalog 0.3 are separate content versions, intentionally unchanged. Catalog checks derive count and excluded count from data and validate unique IDs; core coverage remains a specific eight-law contract.

Directory removal records created parents and removes them only when empty. Preexisting directories and new user files survive. Historical integration states lacking created_dirs remain readable; their directories are preserved. Previously installed projects are not auto-upgraded or rewritten.

Regression checks simulate cp1252 default encoding and CRLF default writing. Native Windows tests NOT RUN. Git CRLF-enabled local clone, ordinary checks, and package hashes pass after patch. Original user configuration backup continues to use bytes.

CLI JSON output uses ASCII escapes so redirected Latin-1/CP1252 streams do not fail after a successful installation. JSON parsers recover the original Unicode strings. stdout_check.py exercises real install, repeat-install, verify and remove subprocesses for both installers with strict PYTHONIOENCODING and redirected pipes; file content remains UTF-8/LF. Native Windows execution remains NOT RUN.
