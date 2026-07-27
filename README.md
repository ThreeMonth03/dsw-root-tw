# Taiwan DSW Knowledge Model

This repository is the source, review, release, and audit mirror for the
English Taiwan customization of the Common DSW Knowledge Model.

- DSW identity: `tw:root-tw`
- initial parent: `dsw:root:2.7.0`
- current status: awaiting the first reviewed KM release

The DSW Knowledge Model Editor is the only writer of KM events. GitHub stores
reviewed specifications, exported bundles, manifests, checksums, tags, and
release assets. Never hand-edit or merge-conflict-resolve `km/root-tw.km`.

The repository also keeps a checksum-bound legal review:

- `legal-question-inventory.yml` is generated keyword triage and may contain
  false positives.
- `legal-mapping.yml` is the curated Taiwan proposal bound to exact upstream
  question UUIDs and official sources.
- `docs/legal-review.md` explains the decision model, known pending laws, and
  review gates.

English questionnaire text is approved and released here first. Traditional
Chinese is maintained separately in `dsw-root-tw-locales-zh_Hant`, pinned to an
immutable release from this repository. Translation is intentionally deferred
until the legal wording is reviewed.

Start with [the legal-review guide](docs/legal-review.md), then follow
[the release process](docs/release-process.md).
