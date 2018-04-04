# FastANI for KBase

A [KBase](https://kbase.us) module using the [KBase SDK](https://github.com/kbase/kb_sdk).

[FastANI](https://github.com/ParBLiSS/FastANI) is a whole-genome similarity estimation utility. Refer to its documentation for more details about the algorithm.

## Misc. notes about FastANI

Running genome A as query and B as reference **does not** give equivalent results as running B for query and A for reference (ie. reversing parameters)

Running with a query-list and reference-list that both have single genomes gives equivalent results to running a single query file to a single reference fie.

The reference-list or query-list files should have paths relative to the directory in which you run the binary

## Visualization

FastANI has an R-based visualization of the genome similarities that has to get generated with genPlotR. However, it only works with 1:1 comparisons.

I left the visualization out of the KBase report. There is some placeholder code in Dockerfile for setting up the dependencies necessary to build/render the PDF for the visualization. If this is a requested feature, then I can go back and add support to generate the visualization in the KBase report -- please make an issue for it.

# License

MIT
