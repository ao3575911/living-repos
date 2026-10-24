# Hello demo

The smallest working Living Repository. A bootstrap script reads `.living/manifest.yaml`, refuses capabilities it does not support, runs one task and publishes state to `.living/state.json`, logging one JSON object per line as the manifest requires.

## Run

```sh
cd examples/hello
pip install PyYAML
python bootstrap.py
```

## Expected output

```text
{"event": "start", "project_id": "hello", "protocol_version": "v0.1.0-draft"}
{"event": "task", "name": "greet", "result": "hello from hello"}
{"event": "state", "path": ".living/state.json", "status": "ready"}
{"event": "done"}
```

It also writes `.living/state.json`:

```json
{"last_task": "greet", "status": "ready"}
```

CI runs the script and compares its output with [`expected-output.txt`](expected-output.txt).
