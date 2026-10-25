#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Tools"))

from dependency_updater import Step, Updater

URL = "https://github.com/google/brotli/archive/refs/tags/v{version}.tar.gz"


def update_source(updater):
    updater.replace_source()
    updater.remove(".github")
    updater.update_config()


updater = Updater(__file__, "brotli", URL)
updater.run([
    Step("Replace the source with the release and update Config.txt", update_source,
        "Updated brotli to version {version}"),
    updater.clone_dependencies_step(),
])
