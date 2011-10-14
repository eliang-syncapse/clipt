OUTPUT_DIRS = output/clipt/services reports/coverage
THRIFT_SOURCES = src/thrift/services.thrift

build : copy-files convert-to-python3 test

create-directories :
	mkdir -p $(OUTPUT_DIRS)

generate-thrift-sources : $(THRIFT_SOURCES) create-directories
	echo $(THRIFT_SOURCES) | xargs -t thrift --gen py:new_style -out output/clipt

convert-to-python3:
	2to3 --no-diffs -vwn output/clipt/services

copy-files : create-directories generate-thrift-sources
	cp src/clipt.py output/
	cp -R src/clipt output/

test :
	nosetests -c nose.cfg

clean :
	find . -name '__pycache__' -print0 | xargs -0 rm -rf
	find . -name '*.pyc' -print0 | xargs -0 rm -rf
	rm -rf output/ reports/
	rm .coverage
