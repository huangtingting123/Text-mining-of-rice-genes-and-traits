# Text-mining-of-rice-genes-and-traits
## 1. File segmentation.
```Bash
    split -l 2000 all_abstract.txt abstract_ -a 1
    find ./ -name "abstract_*" | while read id; do mv $id ${id}.txt; done
```
## 2. Coexisting sentence analysis.
```Bash
    python ../sentence.py abstract/abstract_a.txt result_a.txt
```
## 3. Merge result.
```Bash
    python ../merge.py result_a.txt result_b.txt result.txt
```
