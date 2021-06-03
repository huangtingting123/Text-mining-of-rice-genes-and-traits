# Text-mining-of-rice-genes-and-traits
## 1.File segmentation.
```Bash
  split -l 2000 all_abstract.txt abstract_ -a 1
  find ./ -name "abstract_*" | while read id; do mv $id ${id}.txt; done
