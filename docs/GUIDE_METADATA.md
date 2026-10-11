# Advisory guide metadata and installed provenance — 0.14.1-draft

The initial eight-law guide copied historical catalog metadata: level mandatory and a source_file path not present inside installations. The law prose was advisory, but this metadata could confuse a model reading selection.json. New guide records now explicitly use level advisory and binding false. Historical catalog bytes remain unchanged; original levels are historical data rather than operative metadata.

Each installed law source_file now resolves relative to its selection.json directory to provenance.json. This installed file carries the 88 R-source mappings required by the core guide, plus hashes identifying the historical catalog/trace. It is included in the guide seal, installed lock and installer integrity checks. It does not contain the private original source documents, and traceability is not a redistribution grant or proof of source truth.

Existing installations and old release assets are not rewritten. Remove a verified previous installation, then reinstall if this fix is wanted. Default markdown law/trigger/stop text is unchanged; this does not constitute a new live client test. Historical --context mode still preserves historical records and is deprecated; normalized metadata applies to the default core guide.

The per-law version identifies the installed guide record, including its metadata; it is not a prose-only version. It changes to 0.14.1-draft for the advisory/provenance correction while title, rule, trigger, proportionality, check and source IDs remain unchanged. The original catalog record version remains 0.3.0-draft in the historical archive.
