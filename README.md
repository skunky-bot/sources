# Skunky source registry

This repository is the canonical home for source metadata, usage permissions and ingestion policy for the Skunky platform (including SkunkScrape).

## V1 contract

`registry/sources.v1.json` contains the versioned allowed-source schema. Currently it includes only a safe `example.com` documentation fixture; **no production scraping targets have been approved**.

Properties: `id`, `label`, `url`, `tags`, `enabled`, `mode`, `outreach_allowed`, `lawful_basis`, `robots_review`.

The `search` repository currently carries a matching fixture for self-contained development; a release workflow to distribute signed/versioned registry artifacts is pending.

## Security

A previously tracked `.env` file has been removed from this branch. Rotate any associated live credentials, assess exposure and consult [remediation guidance](docs/SECURITY.md). Git history still contains earlier versions until separately remediated.

Do not include personal leads, proxy credentials or API secrets in the source registry. Privacy/compliance and source rights must be approved before enabling any production target.

Run `python -m pytest -q tests/test_registry.py` and review source changes through a protected PR.
