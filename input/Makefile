# ------------------------------------------------
# List of all subdirectories we care about:
#   HC, SHC, bipartite, complete, planar, random, sparse
# ------------------------------------------------

# For each directory, find .edgelist files, e.g. HC/HC_graph1.edgelist.
SRCS_HC       := $(wildcard HC/*.edgelist)
SRCS_SHC      := $(wildcard SHC/*.edgelist)
SRCS_BIP      := $(wildcard bipartite/*.edgelist)
SRCS_COMPLETE := $(wildcard complete/*.edgelist)
SRCS_PLANAR   := $(wildcard planar/*.edgelist)
SRCS_RANDOM   := $(wildcard random/*.edgelist)
SRCS_SPARSE   := $(wildcard sparse/*.edgelist)

# Convert each .edgelist to a corresponding .out path.
# e.g., HC/HC_graph1.edgelist --> output/HC/HC_graph1.out
OBJS_HC       := $(patsubst HC/%.edgelist,       output/HC/%.out,       $(SRCS_HC))
OBJS_SHC      := $(patsubst SHC/%.edgelist,      output/SHC/%.out,      $(SRCS_SHC))
OBJS_BIP      := $(patsubst bipartite/%.edgelist, output/bipartite/%.out,$(SRCS_BIP))
OBJS_COMPLETE := $(patsubst complete/%.edgelist, output/complete/%.out, $(SRCS_COMPLETE))
OBJS_PLANAR   := $(patsubst planar/%.edgelist,   output/planar/%.out,   $(SRCS_PLANAR))
OBJS_RANDOM   := $(patsubst random/%.edgelist,   output/random/%.out,   $(SRCS_RANDOM))
OBJS_SPARSE   := $(patsubst sparse/%.edgelist,   output/sparse/%.out,   $(SRCS_SPARSE))

# ------------------------------------------------
# The 'all' target: build (run) everything
# ------------------------------------------------
all: $(OBJS_HC) $(OBJS_SHC) $(OBJS_BIP) $(OBJS_COMPLETE) \
     $(OBJS_PLANAR) $(OBJS_RANDOM) $(OBJS_SPARSE)

# ------------------------------------------------
# Pattern Rules:
#   output/HC/%.out depends on HC/%.edgelist, etc.
# ------------------------------------------------

output/HC/%.out: HC/%.edgelist
	@mkdir -p output/HC	
	@echo "[HC] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

output/SHC/%.out: SHC/%.edgelist
	@mkdir -p output/SHC
	@echo "[SHC] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

output/bipartite/%.out: bipartite/%.edgelist
	@mkdir -p output/bipartite
	@echo "[bipartite] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

output/complete/%.out: complete/%.edgelist
	@mkdir -p output/complete
	@echo "[complete] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

output/planar/%.out: planar/%.edgelist
	@mkdir -p output/planar
	@echo "[planar] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

output/random/%.out: random/%.edgelist
	@mkdir -p output/random
	@echo "[random] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

output/sparse/%.out: sparse/%.edgelist
	@mkdir -p output/sparse
	@echo "[sparse] Processing $<..."
	python3 ./backtrackingAlg.py $< > $@

# ------------------------------------------------
# Cleanup: remove all output files
# ------------------------------------------------
clean:
	rm -f output/HC/*.out
	rm -f output/SHC/*.out
	rm -f output/bipartite/*.out
	rm -f output/complete/*.out
	rm -f output/planar/*.out
	rm -f output/random/*.out
	rm -f output/sparse/*.out

.PHONY: all clean
