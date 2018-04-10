# FastANI for KBase

A [KBase](https://kbase.us) module using the [KBase SDK](https://github.com/kbase/kb_sdk).

[FastANI](https://github.com/ParBLiSS/FastANI) is a whole-genome similarity estimation utility. Refer to its documentation for more details about the algorithm.

This project uses Jinja2 for templating html/css. You can install pip dependencies locally with pipenv and the Pipfile

## Manual tests

I have some manual unit tests that bypass the kb-sdk workflow to support TDD. To get these to run:

* Download and compile fastANI and place the executable in your PATH
* Install R and the genPlotR package
* `python test/test_fast_ani.py`

## Misc. notes about FastANI

Instead of using fastANI's `--rl` and `--ql` parameters, I only run the binary on single genome files, mostly so we can generate visualizations and parallelize it. For multiple assemblies, I run the binary in parallel on every pair of assembly and generate a separate pdf visualization for every one.

Other notes:

* Running genome A as query and B as reference **does not** give equivalent results as running B for query and A for reference (ie. reversing parameters)
* Running with a query-list and reference-list that both have single genomes gives equivalent results to running a single query file to a single reference fie.
* The reference-list or query-list files should have paths relative to the directory in which you run the binary

## Visualization

FastANI has an R-based visualization of the genome similarities that has to get generated with genPlotR. It gets set up in the Dockerfile and run from python inside `lib/fastANI/fast_ani_proc.py`

# License

MIT
