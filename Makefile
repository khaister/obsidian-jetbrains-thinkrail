.PHONY: release release-dry-run

release:
	./scripts/release.sh $(ARGS)

release-dry-run:
	./scripts/release.sh --dry-run $(ARGS)
