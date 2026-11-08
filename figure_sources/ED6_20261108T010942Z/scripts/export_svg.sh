#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
pdftocairo -svg figures/ED_Figure_6.pdf figures/ED_Figure_6.svg
