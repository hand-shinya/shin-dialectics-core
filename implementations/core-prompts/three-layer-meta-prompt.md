# Official Three-Layer Meta-Prompt (Core)
Parameters: `src/specs/params.py` only.

**Phase 0 — Premise Audit**
- Extract explicit/implicit premises; surface contradictions.
- Generate internal [i] and external [e] lines of critique; map to axes.

**Layer 1 — E₂(n) generation**
- Per axis, generate `n` stances (mix [i]/[e]); count λₐ := |axes|×n.

**Layer 2 — Thresholding (λ/τ/U)**
- If (λₐ≥LAMBDA_A) ∧ (τ≥TAU_STOP) ∧ (U≤U_MAX) ⇒ consolidate; else explore_more.

**Layer 3 — Validation & Ledger**
- Validate JSON against schemas; append to `docs/PRIORITY-LEDGER.md` with SHA-256 (see `docs/HASHES.txt`).
