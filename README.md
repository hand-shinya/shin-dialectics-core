# Shin-Dialectics 2.0 — Core (Public Priority Release)
**Tagline (EN)**: Generate many negations at once, trigger a phase change, land a synthesis.  
**タグライン (JA)**: 複数否定を同時に生み、相転移を起こし、統合へ着地する。

This repository is the **canonical, lean, and verifiable** publication of **Shin‑Dialectics 2.0**.  
It exists to: **(1) record priority (先取権)**, **(2) enable permissive reuse**, and **(3) provide minimal runnable tools and schemas**.

---

## Core ideas / 核心
- **Simultaneous Multiple Negation, E₂(n)** — generate many antitheses at once across diverse observation axes:  
  \[ E_2(n) = \{ g_i(E_1, A_i, C) \}_{i=1..n} \]
  内在的否定[i]と外在的否定[e]を並列生成し、**創造的緊張**を最大化する。
- **Quantity→Quality thresholds (λₚ/λₐ/λₛ/λᵢ)** — when counts and structure cross operational cutoffs, the system reorganizes toward synthesis.
- **Three‑layer closed loop** — *Language* ↔ *Math/Functions* ↔ *Code*, governed by **τ (stop criteria)** and **U (uncertainty budget)**.
- **Quantum‑mode sketch** — \(|ψ⟩ = α|T⟩ + Σ_i β_i|A_i⟩ + Σ_j γ_j|S_j⟩\) captures delayed commitment and superposition over alternatives.
- **Manifold metaphor** — high‑curvature regions in the “concept manifold” map to creative tension hot‑spots.

> Single source of truth for parameters: `src/specs/params.py` — λ/τ/U and default axes/stances are defined **once** and reused by tools, prompts, and schemas.

---

## Layout
```
src/specs/params.py               # λ/τ/U & defaults (single source of truth)
src/tools/multi_negation_generator.py
src/tools/threshold_monitor.py
implementations/core-prompts/three-layer-meta-prompt.md
implementations/validation/schemas/{antithesis,synthesis,priority-ledger}.schema.json
docs/PRIORITY-LEDGER.md, docs/HASHES.txt
docs/papers/{ja_original,ja}/ + build_index.py, verify_index.py, INDEX.csv
examples/minimal_run.md
LICENSE, LICENSES/LICENSE-CC-BY-4.0.txt, CITATION.cff, .gitignore, requirements.txt
```

## Quick start
```bash
# 1) Generate E₂(n) antitheses (demo, deterministic)
python src/tools/multi_negation_generator.py --thesis "AI in secondary education" --axes 4 --stances 5 > antithesis.json

# 2) Decide consolidate/explore (λ/τ/U thresholds)
python src/tools/threshold_monitor.py --thesis "AI in secondary education" --lambda-a 20 --tau 0.7 --u 0.2 > synthesis.json

# 3) Validate JSON (use any JSON Schema validator against schemas/)
```

## Priority (先取権)
- Primary evidence: `docs/PRIORITY-LEDGER.md` (JST timeline) + SHA‑256 workflow in `docs/HASHES.txt`.  
- For Japanese originals: place under `docs/papers/ja_original/` then run `build_index.py` to get ASCII copies and hashes recorded in `INDEX.csv`.

## License
- **Code**: MIT (`LICENSE`)
- **Docs & Prompts**: CC BY 4.0 (`LICENSES/LICENSE-CC-BY-4.0.txt`)

## Cite
See `CITATION.cff`.  
Short form: *Handa, S. (2025). Shin‑Dialectics 2.0 — Core (v2.0‑core) [Software].*

---
*Last update: 2025-08-24*
