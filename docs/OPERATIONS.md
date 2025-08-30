# OPERATIONS — Release, DOI, Hashes (Shin-Dialectics Core)

## 0. 前提
- Zenodo 連携：GitHub → Zenodo で **Publish releases to Zenodo** を ON（済）。
- Repository → Settings → Actions → **Workflow permissions** = *Read and write*（済）。

## 1. リリース
1) GitHub の **Releases** で `vX.Y.Z` を作成（source.zip/tar.gz は自動添付）。  
2) Release notes は雛形：
   - What’s included / Provenance & Integrity / Note
   - DOI（version, concept）は Zenodo 公開後に追記・更新可。

## 2. ハッシュ（自動）
1) **Actions → Compute release hashes (generic)** を開く。  
2) `tag` に `vX.Y.Z` を入力し **Run workflow**。  
3) 自動で PR 「docs: add SHA256 hashes for vX.Y.Z archives」が作成される。  
4) 内容を確認し **Merge**。  
   - `docs/HASHES.txt` に `## vX.Y.Z` ブロックが追加（既存ブロックがあれば置換）。

## 3. DOI / 引用
- 概念 DOI（Concept）: **10.5281/zenodo.16992501**（固定）。  
- バージョン DOI：Zenodo のリリースページ右上に表示（発行ごとに異なる）。  
- 反映先：
  - `README.md` → バッジ＆「How to cite」  
  - `CITATION.cff` → `doi`, `version`, `date-released`  
  - `docs/PRIORITY-LEDGER.md` → Release ログ（1行ブロック）

## 4. 変更の最小セット（新リリースごと）
- `README.md`：How to cite の DOI（version）を新しいものに差し替え。  
- `CITATION.cff`：`version` と `date-released` を更新、`doi` に **version DOI** を設定。  
- `docs/PRIORITY-LEDGER.md`：JST タイムスタンプで 1 ブロック追記。  
- **Hashes**：本ワークフローを実行し PR を merge。

## 5. 検証
- Releases ページ：DOI 表示／Assets（zip/tar.gz）／本文。  
- `docs/HASHES.txt`：対象タグの SHA256 が存在。  
- `README.md`：コードフェンス閉じ忘れなし。  
- `CITATION.cff`：`repository-code` のプレースホルダ無し。

## 付記（任意改善）
- ORCID 追加：`CITATION.cff` の `authors` に `orcid:` を追記可。  
- リリース署名：`docs/HASHES.txt` の「Signature」を運用ポリシーに合わせて記入。
