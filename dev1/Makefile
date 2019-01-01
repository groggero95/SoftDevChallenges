FILES = $(patsubst pictures/%.jpg, thumbs/%.jpg, $(shell find pictures -type f -iname "*.jpg"))
THUMB = convert -thumbnail 100 $< $@
 
all: ${FILES}
thumbs/%.jpg: pictures/%.jpg
	$(THUMB)
clean:
	rm -rf thumbs/*.jpg
