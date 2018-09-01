
.DEFAULT: diagrams

clean:
	rm -f *.svg *.csv *-gram.tsv >/dev/null 2>&1 || /bin/true
diagrams: 1-gram.svg 2-gram.svg
tables: 1-gram.csv 2-gram.csv 3-gram.csv 4-gram.csv 5-gram.csv 6-gram.csv 7-gram.csv 8-gram.csv 9-gram.csv

ngrams-all.tsv:
	curl http://norvig.com/tsv/ngrams-all.tsv.zip | gunzip >$@

%-gram.tsv: ngrams-all.tsv
	sed /$*-gram/,/$$(($* + 1))-gram/'!d' $< | grep -v -e '-gram' | cut -d$$'\t' -f 1-2 >$@

%.csv: %.tsv huffman.py
	python huffman.py <$< >$@

%.dot: %.tsv huffman.py
	python huffman.py --graph <$< >$@

%.svg: %.dot
	dot -Tsvg -o$@ $^

