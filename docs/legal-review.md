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

The first curated pass in `legal-mapping.yml` covers 22 high-risk upstream
questions:

- replace GDPR legal bases, controller terminology, Article 9 categories, and
  the EU/EEA transfer boundary;
- separate personal-data compliance from ethics-review applicability;
- route human-subject research, reuse, consent, human biobanks, Indigenous
  Peoples research, and scientific use of animals independently;
- distinguish legally regulated personal data from other sensitive
  information;
- localize retention, security, processing-location, and reuse restrictions;
- replace EU database-right assumptions with a Taiwan review of copyright,
  contracts, trade secrets, and government-funded R&D terms.

The proposed text is English only. It is not implemented in the KM and must not
be translated yet.

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

The 2025 Cyber Security Management Act revision also has an effective date to
be determined by the Executive Yuan. Its regulated scope is government
agencies and designated specific non-government agencies; it is not a generic
security law for every research project.

These items remain declared in `legal-mapping.yml` with
`promulgated_not_in_force` status so they cannot silently become current
requirements.

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

Regenerate and validate against the exact source bundle:

```shell
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
out-of-date generated inventory.

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

English is the authoring language for the KM fork. After its legal wording is
approved and released under an immutable version, the zh-Hant repository pins
that release and translates by UUID and source text. A later legal correction
creates a new KM patch version; it never rewrites an already translated source
release.

The Traditional Chinese statutory text is authoritative if an official English
translation differs. Translators should preserve legal identifiers and links,
and raise terminology questions in review rather than editing English source
meaning inside the translation repository.

[nhi-status]: https://dep.mohw.gov.tw/DOS/cp-2498-87143-113.html
[pdpa-amendment]: https://www.pdpc.gov.tw/News_Content/20/1010/
[science-europe]: https://scienceeurope.org/our-resources/practical-guide-to-the-international-alignment-of-research-data-management/
