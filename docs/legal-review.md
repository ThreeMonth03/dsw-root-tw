# Taiwan legal localization

## Decision

Keep the Science Europe research-data-management structure, but replace
EU-specific legal assumptions with conditional Taiwan routes. Science Europe
Core Requirements 4a-4c remain useful: protect personal data and security,
identify intellectual-property and access constraints, and address ethics.
They are not themselves Taiwan law.

This repository is an engineering and review record, not legal advice. Before a
question reaches `legally_reviewed`, a Taiwan-qualified reviewer with the
relevant domain must confirm it. Depending on the topic, that reviewer may be
legal counsel, an IRB or research-ethics office, a privacy officer, a biobank
office, an animal-care committee, or the responsible government authority.

## Four layers

Keep these layers separate in questions and review notes:

1. International RDM guidance, such as the [Science Europe practical
   guide][science-europe].
2. Taiwan statutes and regulations.
3. Institution, ethics-board, repository, contract, and funder requirements.
4. Facts that determine whether a rule applies to the particular project.

A policy is not promoted to a law, and a law that has been promulgated but has
not taken effect is not presented as current law.

## Initial changes

The second curated pass in `legal-mapping.yml` covers 45 high-risk upstream
questions, 29 inherited answer, choice, and reference texts, and two new
per-project questions with 11 conditional screening choices:

- replace GDPR legal bases, controller terminology, Article 9 categories, and
  the EU/EEA transfer boundary;
- separate personal-data compliance from ethics-review applicability;
- route human-subject research, reuse, consent, human biobanks, Indigenous
  Peoples research, and scientific use of animals independently;
- route medical human trials, infectious biological materials, wildlife,
  National Health Insurance data, artificial intelligence, national core
  critical technologies, related trade secrets, Taiwan export controls,
  patents, public-sector records, and foreign or funder rules only when project
  facts trigger them;
- distinguish legally regulated personal data from other sensitive
  information;
- localize retention, security, processing-location, and reuse restrictions;
- replace EU database-right assumptions with a Taiwan review of copyright,
  contracts, trade secrets, and government-funded R&D terms.

The proposed English text is implemented in the generated meeting draft. A
Traditional Chinese meeting draft is maintained in the dedicated locale
repository so both languages can be reviewed together. Neither language is a
released or legally approved version yet.

## Time-sensitive watch list

The 2025 Personal Data Protection Act amendment was promulgated, but the
[official PDPC material][pdpa-amendment] says its effective date is to be set
separately. The official consolidated law page can therefore display amended
text that is not yet effective. Check the PDPC status and amendment comparison,
especially around security duties and the transition from current Article 27
to amended Article 20-1, before every release.

The National Health Insurance Data Management Act was promulgated in December
2025. As of 13 July 2026, the [Ministry of Health and Welfare still described
the Act and subordinate rules as about to take effect][nhi-status]. Treat it as
a conditional pending branch for National Health Insurance data until an exact
effective date is officially announced.

The 2025 Cyber Security Management Act revision took effect on 1 December
2025. Its regulated scope is public agencies and designated specific non-public
agencies; it is not a generic security law for every research project.

The PDPA amendment and National Health Insurance Data Management Act remain
declared in `legal-mapping.yml` with `promulgated_not_in_force` status so they
cannot silently become current requirements. The Cyber Security Management Act
is declared `in_force` but appears only as a conditional route.

## Files and automation

`legal-inventory-rules.yml` contains broad keyword topics. The generated
`legal-question-inventory.yml` is a leakage detector, not the approved change
list. False positives are expected.

`legal-mapping.yml` is curated. Every mapping records:

- the upstream question UUID and exact English title;
- the intended action and proposal status;
- a rationale;
- official sources and provisions;
- proposed English title and guidance.

Its `content_overrides` section binds every inherited answer, choice, or URL
reference to the exact upstream fields before replacing them. Upstream wording
changes therefore fail validation instead of silently applying a stale legal
edit.

Its `question_additions` section defines the per-project applicability screen
and determination record. Question and choice UUIDs derive from stable
jurisdiction-scoped IDs rather than a package version, so a later patch release
does not sever DSW history or existing translations. Validation also follows
every target's ancestor path and rejects entities hidden below deleted
questions, answers, or chapters.

Regenerate and validate against the exact source bundle:

```shell
make draft TOOLING_REPO_DIR=../dsw-km-translation-tool

dsw-km-build-legal-inventory \
  --km /path/to/dsw-root-2.7.0.km \
  --rules legal-inventory-rules.yml \
  --out legal-question-inventory.yml

dsw-km-validate-legal-mapping \
  --km /path/to/dsw-root-2.7.0.km \
  --mapping legal-mapping.yml
```

CI uses the immutable source dependency recorded in the workflows and rejects a
changed checksum, stale UUID, changed title, unknown legal-source reference, or
out-of-date generated inventory. It also rebuilds `km/root-tw.km` and requires a
byte-for-byte match, so the generated package cannot drift from the mapping.

## Review and implementation states

Use these states in order:

1. `candidate`: identified but not yet drafted.
2. `proposed`: sourced engineering proposal; current first-pass state.
3. `legally_reviewed`: applicability and wording confirmed by the responsible
   Taiwan reviewer.
4. `implemented`: entered through the DSW Knowledge Model Editor and exported.
5. `verified`: exported behavior, links, branching, and both languages checked.

Do not move an item to `legally_reviewed` merely because CI passes. CI proves
traceability and consistency, not legal correctness.

## Bilingual release rule

English is the authoring language for the KM fork. Before the first release,
the English and zh-Hant meeting-draft branches may be amended together. After
approval, the zh-Hant repository pins the immutable English source release by
commit and bundle checksum. A later legal correction creates a new KM patch
version; it never rewrites an already translated source release.

The Traditional Chinese statutory text is authoritative if an official English
translation differs. Translators should preserve legal identifiers and links,
and raise terminology questions in review rather than editing English source
meaning inside the translation repository.

[nhi-status]: https://dep.mohw.gov.tw/DOS/cp-2498-87143-113.html
[pdpa-amendment]: https://www.pdpc.gov.tw/News_Content/20/1010/
[science-europe]: https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/
