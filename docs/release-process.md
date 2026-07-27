# KM release process

## Mutable work

Use one pull-request branch for a release. Amend and force-push with
`--force-with-lease` as needed. The branch and pull-request checks are mutable.

## Immutable boundary

1. Review `legal-mapping.yml` and the proposed questionnaire behavior.
2. Implement the approved change in the existing DSW Knowledge Model Editor.
3. Publish a new numeric KM version.
4. Export the exact bundle to `km/root-tw.km`.
5. Copy `release-manifest.example.yml` to `release-manifest.yml`, fill the
   package ancestry, and calculate `sha256sum km/root-tw.km`.
6. Run `dsw-km-validate-release --repo-root .`.
7. Squash-merge the release pull request.
8. Create the immutable `v<version>` tag on that merge commit.

Never move a published tag or replace an existing DSW version. Corrections get
a new patch version.
