all: run

clean:
	rm -rf __pycache__

run:
	python3 basic

.PHONY: all clean run
