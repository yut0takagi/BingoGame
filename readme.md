
# 🎯 ビンゴゲームアプリ

このリポジトリは、Python および Jupyter Notebook を使用して作成されたシンプルなビンゴゲームアプリです。ユーザーがビンゴカードを操作し、シャッフル音とともにゲームを楽しむことができます。

## 📁 ファイル構成

- `BingoApp.py`：ビンゴゲームのメインロジックを含む Python スクリプト。
- `BingoApp.ipynb`：Jupyter Notebook 形式でのビンゴゲーム実装。
- `shuffle_sound.mp3`：シャッフル時に再生される効果音ファイル。
- `readme.md`：プロジェクトの概要と使用方法を記載したファイル。

## 🚀 インストール方法

1. このリポジトリをクローンします：

   ```bash
   git clone https://github.com/yut0takagi/BingoGame.git
   cd BingoGame
   ```

2. 必要な Python パッケージをインストールします：

   ```bash
   pip install -r requirements.txt
   ```

   > **注意**：`requirements.txt` ファイルが存在しない場合、必要なパッケージを手動でインストールしてください。

## 🎮 使用方法

### Python スクリプトを使用する場合

```bash
python BingoApp.py
```

### Jupyter Notebook を使用する場合

1. Jupyter Notebook を起動します：

   ```bash
   jupyter notebook
   ```

2. ブラウザで `BingoApp.ipynb` を開き、セルを順に実行します。

## 🔊 効果音の再生

ゲーム中のシャッフル時に `shuffle_sound.mp3` が再生されます。音声が再生されない場合は、以下を確認してください：

- システムの音量設定
- 必要な Python ライブラリ（例：`pygame`）がインストールされているか

## 🛠 開発環境

- Python 3.x
- Jupyter Notebook
- 必要なライブラリ（例：`pygame`、`random` など）

## 📄 ライセンス

このプロジェクトのライセンス情報は記載されていません。使用や再配布を行う際は、リポジトリ所有者に確認してください。
