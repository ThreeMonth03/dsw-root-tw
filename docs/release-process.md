# KM release process

## Mutable work

Use one pull-request branch for a release. Amend and force-push with
`--force-with-lease` as needed. The branch and pull-request checks are mutable.

For legal changes, keep `legal-mapping.yml` at `proposed` while drafting. A
passing validator proves that sources and upstream questions still match; it
does not replace the Taiwan legal or domain review required before moving a
mapping to `legally_reviewed`.

Run `make draft TOOLING_REPO_DIR=../dsw-km-translation-tool` after every wording
change. This regenerates the KM bundle and release manifest. Both remain mutable
on the pull-request branch. The matching zh-Hant pull-request branch is rebuilt
from this exact bundle and can be amended at the same time.

## Immutable boundary

1. Regenerate `legal-question-inventory.yml` and validate
   `legal-mapping.yml` against the pinned parent bundle.
2. Obtain the required Taiwan legal, privacy, ethics, or domain review and mark
   the approved mappings `legally_reviewed`.
3. Review the resulting questionnaire branches, not only individual strings.
4. Regenerate the mapped bundle. Implement any reviewed structural change not
   represented by `question_additions` in the existing DSW Knowledge Model
   Editor and export it to `km/root-tw.km`.
5. Confirm the numeric KM version and publish it in the controlled DSW
   environment.
6. Generate the manifest from the exact final bundle:
   `dsw-km-prepare-release --repo-root . --overwrite`.
7. Run `dsw-km-validate-release --repo-root .`.
8. Squash-merge the release pull request.
9. Create the immutable `v<version>` tag on that merge commit.
10. Update the zh-Hant repository to the immutable source release and translate
    only that approved version.

Never move a published tag or replace an existing DSW version. Corrections get
a new patch version. Pull-request and tag CI download the previous GitHub
Release asset and reject rewritten historical packages.

Importing a meeting draft into DSW consumes its package identity. If the same
test instance must receive another amended `0.1.0`, delete the earlier package
only when DSW confirms it is unused; otherwise build the feedback round as a
new patch version. Git amend does not bypass DSW package identity rules.
