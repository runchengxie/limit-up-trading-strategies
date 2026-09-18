# Public 文档与 Pages 迁移 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 archive 中适合公开的工程和文档改进迁入 public 仓库，补齐 MkDocs、GitHub Pages 和团队可执行的代码质量检查。

**Architecture:** 保留 public 现有 `src/`、`tests/`、`pyproject.toml` 和 Python CI，把 public 文档组织为 MkDocs 站点，并通过独立 Pages workflow 发布 `site/`。archive 的原始策略、Notebook、数据和内部历史不复制到 public。

**Tech Stack:** Python 3.11/3.12、pytest、Ruff、MkDocs 1.6.1、Material for MkDocs 9.7.7、GitHub Actions Pages。

**Spec:** `docs/superpowers/specs/2026-09-18-public-docs-pages-migration-design.md`

## Global Constraints

- 不覆盖 public 的 `src/`、`tests/`、`pyproject.toml` 和现有 CI 行为。
- 不复制 archive 的原始策略 TXT、Notebook、Excel、CSV、图片、日志、私有脱敏记录和内部计划。
- MkDocs 只读取 public 的 `docs/`，Pages 只上传 MkDocs 生成的 `site/`。
- 保留 Python 3.11/3.12 测试矩阵、`python -m pytest -q` 和 `python -m compileall -q src tests`。
- 文档以中文为主，API、库名、文件名、命令和正式文献标题保留原文。

---

### Task 1: 加强 public 代码质量检查

**Files:**
- Modify: `pyproject.toml`
- Modify: `.github/workflows/ci.yml`
- Modify: `src/limit_up_event_study/events.py` only if Ruff reports a concrete issue
- Modify: `src/limit_up_event_study/returns.py` only if Ruff reports a concrete issue
- Modify: `tests/test_events.py` only if Ruff reports a concrete issue
- Modify: `tests/test_returns.py` only if Ruff reports a concrete issue
- Modify: `tests/test_public_api.py` only if Ruff reports a concrete issue

**Interfaces:**
- Consumes: existing package, tests and CI matrix.
- Produces: a reproducible Ruff lint check without changing the public API.

- [ ] **Step 1: Add the Ruff development dependency and configuration**

Extend `pyproject.toml` with:

```toml
dev = ["ruff>=0.8,<1"]

[tool.ruff]
target-version = "py311"
line-length = 88

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F", "I", "UP", "B"]
```

- [ ] **Step 2: Install the development extra and run Ruff**

Run:

```text
python -m pip install -e ".[test,dev]"
python -m ruff check src tests
```

Expected: Ruff passes. If it reports a real issue in tracked source or tests, make the smallest behavior-preserving fix and add or update a focused test only when behavior changes.

- [ ] **Step 3: Add Ruff to CI**

Change the CI install command to `python -m pip install -e ".[test,dev]"` and add a step after installation:

```yaml
- name: Lint source and tests
  run: python -m ruff check src tests
```

- [ ] **Step 4: Run the existing test and compile checks**

Run:

```text
python -m pytest -q
python -m compileall -q src tests
```

Expected: 13 tests pass and compilation succeeds.

- [ ] **Step 5: Commit the code-quality changes**

```text
git add pyproject.toml .github/workflows/ci.yml src tests
git commit -m "ci: add Ruff checks for public research code"
```

### Task 2: Port and localize public documentation

**Files:**
- Create: `AGENTS.md`
- Modify: `README.md`
- Modify: `docs/references/literature-and-broker-reports.md`
- Modify: `docs/research/strategy-research-roadmap.md`
- Modify: `docs/release/public-release-checklist.md`

**Interfaces:**
- Consumes: public code scope and the archive's language and maintenance improvements.
- Produces: Chinese-first public documentation that describes only public code and public research materials.

- [ ] **Step 1: Add public collaboration rules**

Create `AGENTS.md` with the public repository scope, Python validation commands, public-release constraints, and the rule that archive-only raw materials are not copied into this repository.

- [ ] **Step 2: Rewrite the public README without archive-only claims**

Keep the public repository's actual package name, `src/` API, test commands, synthetic-input scope and link to the private archive. Write the primary explanation in Chinese. Do not list archive TXT, Notebook or factor-data paths as public files.

- [ ] **Step 3: Polish the existing public Markdown pages**

Use Chinese headings and natural Chinese prose. Keep paper titles, API names, filenames and shell commands unchanged. Remove unnecessary English headings, semicolons, quotation marks and formulaic summary phrases without changing research claims.

- [ ] **Step 4: Run text and link checks**

Run:

```text
git diff --check
rg -n "不是.{0,20}而是|总体来说|总的来说|综上|；|—" README.md AGENTS.md docs -g "*.md" -g "!docs/superpowers/**"
```

Expected: no whitespace errors. Any remaining match must be a deliberate technical or bibliographic exception.

- [ ] **Step 5: Commit the public documentation changes**

```text
git add AGENTS.md README.md docs/references docs/research docs/release/public-release-checklist.md
git commit -m "docs: localize public research documentation"
```

### Task 3: Add the public MkDocs site

**Files:**
- Create: `mkdocs.yml`
- Create: `requirements-docs.txt`
- Create: `docs/index.md`
- Create: `docs/maintenance-and-validation.md`

**Interfaces:**
- Consumes: the public Markdown pages from Task 2.
- Produces: `mkdocs build --strict` output with explicit navigation over public documents only.

- [ ] **Step 1: Pin the compatible documentation dependencies**

Create `requirements-docs.txt` with:

```text
mkdocs==1.6.1
mkdocs-material==9.7.7
```

- [ ] **Step 2: Configure the public navigation**

Create `mkdocs.yml` with `docs_dir: docs`, the Material theme, search, code-copy and table-of-contents extensions, and this navigation:

```yaml
nav:
  - 首页: index.md
  - 研究路线: research/strategy-research-roadmap.md
  - 文献与研究假设: references/literature-and-broker-reports.md
  - 维护与验证: maintenance-and-validation.md
  - 公开发布清单: release/public-release-checklist.md
```

Exclude `superpowers/**` from the published site.

- [ ] **Step 3: Add a public landing page and maintenance page**

The landing page must describe the event-study package, execution-aware evaluation, synthetic inputs and research boundary. The maintenance page must list pytest, compileall, Ruff and MkDocs commands and explain that archive raw materials are intentionally excluded.

- [ ] **Step 4: Build the site strictly**

Run:

```text
python -m pip install -r requirements-docs.txt
mkdocs build --strict
```

Expected: exit code 0 and `site/index.html` exists. The generated `site/` directory must remain ignored and untracked.

- [ ] **Step 5: Commit the MkDocs site**

```text
git add mkdocs.yml requirements-docs.txt docs/index.md docs/maintenance-and-validation.md
git commit -m "docs: add public MkDocs site"
```

### Task 4: Deploy MkDocs to GitHub Pages

**Files:**
- Create: `.github/workflows/docs.yml`

**Interfaces:**
- Consumes: Task 3's `mkdocs.yml` and documentation dependencies.
- Produces: a GitHub Pages deployment from the `main` branch using only the generated `site/` artifact.

- [ ] **Step 1: Add the Pages workflow**

Create a workflow triggered by pushes to `main`, pull requests for build validation, and manual dispatch. The build job must use Python 3.11, install `requirements-docs.txt`, run `mkdocs build --strict`, and upload `site/` with `actions/upload-pages-artifact@v4`. The deploy job must run only for pushes to `main`, depend on the build job, use the `github-pages` environment, and deploy with `actions/deploy-pages@v4`.

- [ ] **Step 2: Validate the workflow shape locally**

Confirm the workflow contains `pages: write`, `id-token: write`, `needs: build`, `path: site`, and the `github-pages` environment. Run `git diff --check`.

- [ ] **Step 3: Commit the Pages workflow**

```text
git add .github/workflows/docs.yml
git commit -m "ci: deploy public docs to GitHub Pages"
```

### Task 5: Full verification and public PR

**Files:**
- Verify: `src/`, `tests/`, `pyproject.toml`, `.github/workflows/ci.yml`, `.github/workflows/docs.yml`, `mkdocs.yml`, `docs/`

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: a clean public branch ready for a PR and a Pages deployment run.

- [ ] **Step 1: Run the complete local verification**

Run:

```text
python -m pytest -q
python -m compileall -q src tests
python -m ruff check src tests
mkdocs build --strict
git diff --check
```

- [ ] **Step 2: Check the final repository boundary**

Run `rg --files` and confirm public contains no archive strategy TXT, raw Notebook, factor Excel/CSV/image/log directory, or archive internal plan/spec files beyond the public migration design and implementation plan.

- [ ] **Step 3: Push the feature branch and create a PR**

Use a branch named `codex/public-docs-pages-migration`, push it to `origin`, and create a PR targeting `main` with the local verification results and the explicit statement that archive raw materials were not copied.

- [ ] **Step 4: Verify remote CI and Pages**

Confirm the existing Python CI and new docs workflow complete successfully. Confirm the Pages API reports a deployed URL and that the site contains the public landing page.
