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

build/justage_koinzidenz.pdf: justage_koinzidenz.py header-matplotlib.tex justage_koinzidenz.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python justage_koinzidenz.py

build/kalibration.pdf: kalibration.py header-matplotlib.tex matplotlibrc 20180704/kalibration.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python kalibration.py

build/messung.pdf: messung.py header-matplotlib.tex matplotlibrc 20180704/messung.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python messung.py

build/messung_t_u.pdf: messung_theorie_untergrund.py header-matplotlib.tex matplotlibrc 20180704/messung.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python messung_theorie_untergrund.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plotElement.pdf build/justage_koinzidenz.pdf build/kalibration.pdf build/messung.pdf build/messung_t_u.pdf

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
