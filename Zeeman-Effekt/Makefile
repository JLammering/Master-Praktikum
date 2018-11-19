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
build/plotElement.pdf: plot.py header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot.py

build/kalibrierung_b.pdf: kalibrierung_b.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python kalibrierung_b.py

build/red_ds.pdf: g_J_red.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python g_J_red.py

build/blue_ds.pdf: g_J_blue.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python g_J_blue.py

build/red_quot.pdf: g_J_red.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python g_J_red.py

build/blue_quot.pdf: g_J_blue.py header-matplotlib.tex matplotlibrc | build
	TEXINPUTS="$(call translate,$(pwd):)" python g_J_blue.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plotElement.pdf build/kalibrierung_b.pdf build/red_quot.pdf build/blue_quot.pdf
#build/red_ds.pdf build/blue_ds.pdf

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
