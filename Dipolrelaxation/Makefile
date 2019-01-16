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
build/plotElement.pdf: plot.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot.py

build/heizrate_2schritt.pdf: heizrate_2schritt.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python heizrate_2schritt.py

build/heizrate_1_5schritt.pdf: heizrate_1_5schritt.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python heizrate_1_5schritt.py

build/stromtemp_2.pdf: stromtemp_2.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python stromtemp_2.py

build/stromtemp_1_5.pdf: stromtemp_1_5.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python stromtemp_1_5.py

build/stromtemp_2_off.pdf: stromtemp_2_off.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python stromtemp_2_off.py

build/stromtemp_2_off_W1.pdf: stromtemp_2_off_W1.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python stromtemp_2_off_W1.py

build/stromtemp_2_off_W2.pdf: stromtemp_2_off_W2.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python stromtemp_2_off_W2.py

build/relax_2.pdf: relax_2.py header-matplotlib.tex matplotlibrc messung_2schritt.txt | build
		TEXINPUTS="$(call translate,$(pwd):)" python relax_2.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plotElement.pdf build/heizrate_2schritt.pdf build/stromtemp_2.pdf build/stromtemp_2_off.pdf build/stromtemp_2_off_W1.pdf build/stromtemp_2_off_W2.pdf build/relax_2.pdf

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
