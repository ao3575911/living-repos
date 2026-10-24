# Living Repositories guide

Runnable examples of the [Living Repositories Protocol](https://ao3575911.github.io/living-repos-protocol/). Each example is a directory you can copy into your own repository.

## Examples

<!-- BEGIN GENERATED: examples -->

| Example | Capabilities | Isolation | State target |
| --- | --- | --- | --- |
| [`_template`](https://github.com/ao3575911/living-repos/tree/main/examples/_template) | run_tasks, publish_state | dedicated-vm | control-process |
| [`hello`](https://github.com/ao3575911/living-repos/tree/main/examples/hello) | run_tasks, publish_state | sandbox-process | file |

Generated from each example's manifest by `scripts/gen_readme.py`.

<!-- END GENERATED: examples -->

## Add a manifest to your repository

1. Copy `examples/_template/.living/manifest.yaml` into your repository as `.living/manifest.yaml`.
2. Set `project_id` and the capabilities your agent needs. Field rules: [schema reference](https://ao3575911.github.io/living-repos-protocol/schema-reference.html).
3. Validate it in CI:

```yaml
- uses: actions/checkout@v7.0.1
- uses: ao3575911/living-repos-protocol@v0.3.0
  with:
    manifests: .living/manifest.yaml
```

## Background

- [Strategy](https://github.com/ao3575911/living-repos/blob/main/STRATEGY.md)
- [Architecture](architecture.md)
- [Roadmap](roadmap.md)
- [QA strategy](qa-strategy.md)

Source: [github.com/ao3575911/living-repos](https://github.com/ao3575911/living-repos).
