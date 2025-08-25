# Pack 001（第1回：AI拡張弁証法 導入）アップロード手順

## 収録ファイル（この順で配置）
1. `docs/papers/ja_original/001-ai-augmented-dialectics-intro.md`（JP原文・YAML付き）
2. `docs/HASHES.txt`（SHA-256の追記済み）
3. `docs/PRIORITY-LEDGER-append-001.json`（レジャー追記用の1件）
4. `docs/papers/TIMELINE-JST.csv`（JSTタイムラインの控え）

## Git手順（例）
```bash
git add docs/papers/ja_original/001-ai-augmented-dialectics-intro.md docs/HASHES.txt docs/PRIORITY-LEDGER-append-001.json docs/papers/TIMELINE-JST.csv
git commit -m "papers: add Pack 001 (JP original, hash, ledger-append, timeline-JST)"
# 署名付きタグ（任意）
git tag -s papers-2025-08-25 -m "Papers snapshot JST 2025-08-25"
git push && git push --tags
```

## 既存ファイルへの追記
- `docs/PRIORITY-LEDGER.md` が既に存在する場合：本パックの `docs/PRIORITY-LEDGER-append-001.json` の内容を1件分追記してください（本文の再掲は不要）。
- 存在しない場合：新規に `docs/PRIORITY-LEDGER.md` を作成し、以下のJSONをコードブロックとして保存するか、将来の自動集約スクリプトの入力として本JSONを保管してください。

## ハッシュ（検証用）
- `001-ai-augmented-dialectics-intro.md` の SHA-256: `cc9c928cb1a8c0715b1cbe0515f61a0d195456aaea260b719341ef2acd24285c`

## 備考
- このパックは**証拠性（先取権の時点固定）を最優先**に設計しています。
- 英訳（EN）は希望に応じて別パックで提供可能です（`docs/papers/en/` 配下に配置し、同様に HASHES/LEDGER に追記）。
