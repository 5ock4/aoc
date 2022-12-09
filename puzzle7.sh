for dir in `find . -type d -print`; do ls -ltrR $dir | grep ^- | awk '$5 > 0 {SUM += $5} END {print SUM}'; done | awk '$0 > 100000 {SUM += $0} END {print SUM}'
