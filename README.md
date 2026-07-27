# Taiwan DSW Knowledge Model

This repository is the source, review, release, and audit mirror for the
English Taiwan customization of the Common DSW Knowledge Model.

- DSW identity: `tw:root-tw`
- initial parent: `dsw:root:2.7.0`
- current status: mutable bilingual `0.1.0` meeting draft; not released

The checked-in draft is generated from the exact parent bundle and
`legal-mapping.yml`; never hand-edit or merge-conflict-resolve
`km/root-tw.km`. The deterministic builder applies source-bound title, guidance,
answer, choice, and reference replacements and creates the two curated Taiwan
legal-routing questions with stable entity UUIDs. Structural changes outside
that declared schema remain work for the DSW Knowledge Model Editor.

The repository also keeps a checksum-bound legal review:

- `legal-question-inventory.yml` is generated keyword triage and may contain
  false positives.
- `legal-mapping.yml` is the curated Taiwan proposal bound to exact upstream
  question UUIDs and official sources.
- `docs/legal-review.md` explains the decision model, known pending laws, and
  review gates.

English questionnaire text is authored here. Traditional Chinese is maintained
separately in `dsw-root-tw-locales-zh_Hant`. During the meeting-draft phase the
two pull-request branches advance together; after approval, the translation
repository pins the immutable source release.

Build the same draft locally with:

```shell
make draft TOOLING_REPO_DIR=../dsw-km-translation-tool
```

Start with [the legal-review guide](docs/legal-review.md), then follow
[the release process](docs/release-process.md).
