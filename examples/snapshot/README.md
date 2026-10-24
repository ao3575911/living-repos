# Snapshot demo

Shows the `snapshot_restore` capability and the `snapshot` manifest field added in protocol v0.3.0. The bootstrap writes a file, snapshots the paths listed in `snapshot.paths`, overwrites the file, then restores the snapshot.

## Run

```sh
cd examples/snapshot
pip install PyYAML
python bootstrap.py
```

## Expected output

```text
{"event": "start", "project_id": "snapshot", "retention_days": 3, "snapshot_paths": ["work/"]}
{"content": "version 1", "event": "task", "name": "write"}
{"event": "snapshot", "id": "1", "paths": ["work/"]}
{"content": "version 2", "event": "task", "name": "overwrite"}
{"content": "version 1", "event": "restore", "id": "1"}
{"event": "done"}
```

Afterwards `work/notes.txt` contains `version 1`. CI runs the script and compares its output with [`expected-output.txt`](expected-output.txt).
