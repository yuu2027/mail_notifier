#!/bin/bash
# .env を読み込む
export $(grep -v '^#' .env | xargs)

# cron をフォアグラウンドで実行（ログを保持）
cron -f
