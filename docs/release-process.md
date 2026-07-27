# KM release process

## Mutable work

Use one pull-request branch for a release. Amend and force-push with
`--force-with-lease` as needed. The branch and pull-request checks are mutable.

For legal changes, keep `legal-mapping.yml` at `proposed` while drafting. A
passing validator proves that sources and upstream questions still match; it
does not replace the Taiwan legal or domain review required before moving a
mapping to `legally_reviewed`.

## Immutable boundary

1. Regenerate `legal-question-inventory.yml` and validate
   `legal-mapping.yml` against the pinned parent bundle.
2. Obtain the required Taiwan legal, privacy, ethics, or domain review and mark
   the approved mappings `legally_reviewed`.
3. Review the resulting questionnaire branches, not only individual strings.
4. Implement the approved change in the existing DSW Knowledge Model Editor.
5. Publish a new numeric KM version.
6. Export the exact bundle to `km/root-tw.km`.
7. Generate the manifest from the exported bundle:
   `dsw-km-prepare-release --repo-root .`. For a replacement manifest that has
   not been merged or tagged, add `--overwrite`.
8. Run `dsw-km-validate-release --repo-root .`.
9. Squash-merge the release pull request.
10. Create the immutable `v<version>` tag on that merge commit.
11. Update the zh-Hant repository to the immutable source release and translate
    only that approved version.

Never move a published tag or replace an existing DSW version. Corrections get
a new patch version. Pull-request and tag CI download the previous GitHub
Release asset and reject rewritten historical packages.
