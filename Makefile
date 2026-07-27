TOOLING_REPO_DIR ?= ../dsw-km-translation-tool
TOOLING_PYTHON := $(TOOLING_REPO_DIR)/.venv/bin/python
SOURCE_KM ?= $(TOOLING_REPO_DIR)/tests/fixtures/source_inputs/dsw_root_2.7.0.km

.PHONY: draft

draft:
	@test -x "$(TOOLING_PYTHON)" || { \
		printf '%s\n' "Missing $(TOOLING_PYTHON); run 'make install-dev' in $(TOOLING_REPO_DIR)." >&2; \
		exit 2; \
	}
	$(TOOLING_PYTHON) scripts/build_draft.py \
		--repo-root . \
		--tooling-repo "$(TOOLING_REPO_DIR)" \
		--source-km "$(SOURCE_KM)"
	$(TOOLING_REPO_DIR)/.venv/bin/dsw-km-prepare-release \
		--repo-root . \
		--overwrite
