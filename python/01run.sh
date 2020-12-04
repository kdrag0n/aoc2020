#!/usr/bin/env bash

set -eufo pipefail

cd "$(dirname "$0")"

num="$1"
problem="${2:-}"

if [ ! -f in/$num ]; then
    echo "Download input"
    curl -H 'Cookie: session=53616c7465645f5f22bb9dcf311ba0ab21cc64e6bbee1ebd781eb85872c856994b4fa8069899c943958e4f10d76ab1bf' "https://adventofcode.com/2020/day/$num/input" | tee in/$num
fi

if [ "x$problem" = "x" ]; then
    ./day$num.py in/$num
else
    ./day${num}-2.py in/$num
fi
