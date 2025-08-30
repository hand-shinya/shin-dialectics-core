# Release Hashes Automation — Quick Guide

## 目的

GitHub のリリース（例：`v2.0.1`）で配布される `source.tar.gz` / `source.zip` の **SHA256** を自動計算し、`docs/HASHES.txt` に記録する。改ざん検出と再現性を保証する。

## セットアップ（リポジトリに既設）

* ワークフロー: `.github/workflows/release-hashes.yml`

  * 実行名: **Compute release hashes (v2.0.1)**
  * 出力: ① `docs/HASHES.txt` への追記、② PR（タイトル: `docs: add SHA256 hashes for v2.0.1 archives`）

> 権限設定（既設前提）
> Settings → Actions → **Workflow permissions** = *Read and write*、
> **Allow GitHub Actions to create and approve pull requests** = ON

## 使い方（毎回の手順）

1. GitHub → **Actions** → **Compute release hashes (v2.0.1)** → **Run workflow**。
2. 実行完了後、**Pull requests** を開く。
   PR タイトル **“docs: add SHA256 hashes for v2.0.1 archives”** を開き、**Merge pull request → Confirm merge**。
   （ブランチ保護で止まる場合は、一時的に承認/必須チェックを緩め、マージ後に元へ戻す）
3. 検証：`docs/HASHES.txt` に以下形式のブロックが存在することを確認。

   ```
   # v2.0.1
   SHA256  source.tar.gz  <64桁>
   SHA256  source.zip     <64桁>
   ```

## よくある詰まり所

* **Run ボタンが見えない**: 実行詳細ページではなく、左ペインのワークフロー名（Compute…）のトップに戻る。
* **PRが作成されない**: 上記の **Workflow permissions** と **Allow … PRs** を再確認。
* **main にマージできない**: Branch protection のレビュー/チェック要件を満たす（または一時的に緩和）。

## 次のリリースに適用（タグ更新）

* `.github/workflows/release-hashes.yml` 内の `v2.0.1` を新タグ（例：`v2.0.2`）に置換し、コミット。
* 以降の手順は同じ（Run → PR → Merge）。

---

### （任意）改良版：タグを入力して実行

固定タグを編集したくない場合は、下記のパラメータ化版に置き換える。実行時に `tag` を入力する。

```yaml
name: Compute release hashes (by tag)
permissions: { contents: write, pull-requests: write }
on:
  workflow_dispatch:
    inputs:
      tag:
        description: 'Git tag (e.g., v2.0.1)'
        required: true
        type: string
jobs:
  compute:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - name: Download archives
        run: |
          mkdir -p _artifacts
          curl -L -o _artifacts/source.zip    "https://github.com/${{ github.repository }}/archive/refs/tags/${{ inputs.tag }}.zip"
          curl -L -o _artifacts/source.tar.gz "https://github.com/${{ github.repository }}/archive/refs/tags/${{ inputs.tag }}.tar.gz"
      - name: Compute SHA256
        id: sha
        run: |
          ZIP_SHA=$(sha256sum _artifacts/source.zip    | awk '{print $1}')
          TGZ_SHA=$(sha256sum _artifacts/source.tar.gz | awk '{print $1}')
          echo "zip_sha=$ZIP_SHA" >> $GITHUB_OUTPUT
          echo "tgz_sha=$TGZ_SHA" >> $GITHUB_OUTPUT
      - name: Update docs/HASHES.txt (replace same-tag block)
        run: |
          mkdir -p docs
          touch docs/HASHES.txt
          TAG_ESC=$(printf "%s" "${{ inputs.tag }}" | sed 's/[.[\()*^$]/\\&/g')
          awk -v tag="$TAG_ESC" 'BEGIN{p=1} $0=="# "tag{p=0} /^# v/{if(!p){p=1;next}} p{print}' docs/HASHES.txt > docs/HASHES.txt.tmp || true
          mv docs/HASHES.txt.tmp docs/HASHES.txt
          {
            echo "# ${{ inputs.tag }}"
            echo "SHA256  source.tar.gz  ${{ steps.sha.outputs.tgz_sha }}"
            echo "SHA256  source.zip     ${{ steps.sha.outputs.zip_sha }}"
            echo
          } >> docs/HASHES.txt
      - uses: peter-evans/create-pull-request@v6
        with:
          branch: "chore/hashes-${{ inputs.tag }}"
          base: main
          title: "docs: add SHA256 hashes for ${{ inputs.tag }} archives"
          commit-message: "docs: add SHA256 hashes for ${{ inputs.tag }} archives"
          body: |
            SHA256 for ${{ inputs.tag }}:
            - source.tar.gz: ${{ steps.sha.outputs.tgz_sha }}
            - source.zip:    ${{ steps.sha.outputs.zip_sha }}
```

**実行方法**: Actions → *Compute release hashes (by tag)* → **Run workflow** → `tag` に `vX.Y.Z` を入力 → 実行 → 生成PRをマージ。

---

以上。これで、プロジェクトを知らない担当者でも、**目的・場所・操作・結果・次回の更新**が一読で分かり、ハッシュ記録を確実に運用できます。
