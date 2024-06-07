# 发布 make release
.PHONY: release
release:
	python ./version-cli/auto_release.py
