/*
A KBase module: FastANI
*/

module FastANI {
    /*
        Insert your typespec information here.
    */
    typedef structure {
        string query_genome;
        list<string> genome_references;
    } Params;

    typedef structure {
        float ani_estimate;
        int total_fragments;
        int orthologous_matches;
    } Result;

    funcdef fast_ani(string workspace, Params params) returns (Result result) authentication required;
};
