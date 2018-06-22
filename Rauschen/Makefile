ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:

build/plotdurchlasseinfach.pdf: eichmessung.py daten/eichung.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python eichmessung.py

build/plotWiderstand1.pdf: widerstand.py eichmessung.py daten/widerstand1.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python widerstand.py

build/plotRauschspektrumOxid.pdf: rauschspektrum.py daten/oxidkurveband.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python rauschspektrum.py

build/plotElement.pdf: elementar.py daten/elementar.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python elementar.py

build/plotKennlinie1.pdf: kennlinie.py daten/kennlinie1.txt header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python kennlinie.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:

build/main.pdf:build/plotdurchlasseinfach.pdf build/plotWiderstand1.pdf build/plotRauschspektrumOxid.pdf build/plotElement.pdf build/plotKennlinie1.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
