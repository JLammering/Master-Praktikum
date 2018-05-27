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
#build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS="$(call translate,$(pwd):)" python plot.py

build/stromspannungskennlinie.pdf: stromspannungskennlinie.py stromspannungskennlinie.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python stromspannungskennlinie.py

build/kalibration.pdf: kalibration.py 18_04_30_Graesser_Lammering/Calib/0Vbeikanal50.txt 18_04_30_Graesser_Lammering/Calib/kanal20.txt 18_04_30_Graesser_Lammering/Calib/kanal40.txt 18_04_30_Graesser_Lammering/Calib/kanal60.txt 18_04_30_Graesser_Lammering/Calib/kanal80.txt 18_04_30_Graesser_Lammering/Calib/kanal100.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python kalibration.py

build/kalibration2.pdf: kalibration2.py 18_04_30_Graesser_Lammering/Calib/0Vbeikanal50.txt 18_04_30_Graesser_Lammering/Calib/kanal20.txt 18_04_30_Graesser_Lammering/Calib/kanal40.txt 18_04_30_Graesser_Lammering/Calib/kanal60.txt 18_04_30_Graesser_Lammering/Calib/kanal80.txt 18_04_30_Graesser_Lammering/Calib/kanal100.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python kalibration2.py

build/Pedestal.pdf: Pedestal.py 18_04_30_Graesser_Lammering/Pedestal.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python Pedestal.py

build/Common_Mode_Shift.pdf: Common_Mode_Shift.py 18_04_30_Graesser_Lammering/Pedestal.txt Berechneter_Pedestal.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python Common_Mode_Shift.py

build/Noise.pdf: Noise.py 18_04_30_Graesser_Lammering/Pedestal.txt Berechneter_Pedestal.txt Berechneter_Common_Mode_Shift.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python Noise.py

build/pitch.pdf: pitch.py 18_04_30_Graesser_Lammering/Laserscan.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python pitch.py

build/pitch2.pdf: pitch2.py 18_04_30_Graesser_Lammering/Laserscan.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python pitch2.py

build/Ausdehnung.pdf: Ausdehnung.py 18_04_30_Graesser_Lammering/Laserscan.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python Ausdehnung.py

build/ccel.pdf: ccel.py 18_04_30_Graesser_Lammering/CCEL/0CCEL.txt 18_04_30_Graesser_Lammering/CCEL/10CCEL.txt 18_04_30_Graesser_Lammering/CCEL/20CCEL.txt 18_04_30_Graesser_Lammering/CCEL/30CCEL.txt 18_04_30_Graesser_Lammering/CCEL/40CCEL.txt 18_04_30_Graesser_Lammering/CCEL/50CCEL.txt 18_04_30_Graesser_Lammering/CCEL/60CCEL.txt 18_04_30_Graesser_Lammering/CCEL/70CCEL.txt 18_04_30_Graesser_Lammering/CCEL/80CCEL.txt 18_04_30_Graesser_Lammering/CCEL/90CCEL.txt 18_04_30_Graesser_Lammering/CCEL/100CCEL.txt 18_04_30_Graesser_Lammering/CCEL/110CCEL.txt 18_04_30_Graesser_Lammering/CCEL/120CCEL.txt 18_04_30_Graesser_Lammering/CCEL/130CCEL.txt 18_04_30_Graesser_Lammering/CCEL/140CCEL.txt 18_04_30_Graesser_Lammering/CCEL/150CCEL.txt 18_04_30_Graesser_Lammering/CCEL/160CCEL.txt 18_04_30_Graesser_Lammering/CCEL/170CCEL.txt 18_04_30_Graesser_Lammering/CCEL/180CCEL.txt 18_04_30_Graesser_Lammering/CCEL/190CCEL.txt 18_04_30_Graesser_Lammering/CCEL/200CCEL.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python ccel.py

build/eindringtiefe.pdf: eindringtiefe.py 18_04_30_Graesser_Lammering/CCEL/0CCEL.txt 18_04_30_Graesser_Lammering/CCEL/10CCEL.txt 18_04_30_Graesser_Lammering/CCEL/20CCEL.txt 18_04_30_Graesser_Lammering/CCEL/30CCEL.txt 18_04_30_Graesser_Lammering/CCEL/40CCEL.txt 18_04_30_Graesser_Lammering/CCEL/50CCEL.txt 18_04_30_Graesser_Lammering/CCEL/60CCEL.txt 18_04_30_Graesser_Lammering/CCEL/70CCEL.txt 18_04_30_Graesser_Lammering/CCEL/80CCEL.txt 18_04_30_Graesser_Lammering/CCEL/90CCEL.txt 18_04_30_Graesser_Lammering/CCEL/100CCEL.txt 18_04_30_Graesser_Lammering/CCEL/110CCEL.txt 18_04_30_Graesser_Lammering/CCEL/120CCEL.txt 18_04_30_Graesser_Lammering/CCEL/130CCEL.txt 18_04_30_Graesser_Lammering/CCEL/140CCEL.txt 18_04_30_Graesser_Lammering/CCEL/150CCEL.txt 18_04_30_Graesser_Lammering/CCEL/160CCEL.txt 18_04_30_Graesser_Lammering/CCEL/170CCEL.txt 18_04_30_Graesser_Lammering/CCEL/180CCEL.txt 18_04_30_Graesser_Lammering/CCEL/190CCEL.txt 18_04_30_Graesser_Lammering/CCEL/200CCEL.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python eindringtiefe.py

build/cceq.pdf: cceq.py 18_04_30_Graesser_Lammering/CCEQ/0_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/10_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/20_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/30_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/40_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/50_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/60_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/70_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/80_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/90_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/100_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/110_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/120_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/130_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/140_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/150_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/160_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/170_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/180_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/190_Cluster_adc_entries.txt 18_04_30_Graesser_Lammering/CCEQ/200_Cluster_adc_entries.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python cceq.py

build/cluster_event.pdf: cluster_event.py 18_04_30_Graesser_Lammering/number_of_clusters.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python cluster_event.py

build/channel_event.pdf: channel_event.py 18_04_30_Graesser_Lammering/cluster_size.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python channel_event.py

build/hitmap.pdf: hitmap.py 18_04_30_Graesser_Lammering/hitmap.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python hitmap.py

build/energiespektrum_adc.pdf: energiespektrum_adc.py 18_04_30_Graesser_Lammering/Cluster_adc_entries.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python energiespektrum_adc.py

build/energiespektrum_keV.pdf: energiespektrum_keV.py 18_04_30_Graesser_Lammering/Cluster_adc_entries.txt Kalibration_Koeffizienten.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python energiespektrum_keV.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/stromspannungskennlinie.pdf build/kalibration.pdf build/kalibration2.pdf build/Pedestal.pdf build/Common_Mode_Shift.pdf build/Noise.pdf build/pitch.pdf build/pitch2.pdf build/Ausdehnung.pdf build/ccel.pdf build/eindringtiefe.pdf build/cceq.pdf build/hitmap.pdf build/energiespektrum_adc.pdf  build/cluster_event.pdf build/channel_event.pdf build/energiespektrum_keV.pdf

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
