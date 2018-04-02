/*
A KBase module: FastANI
*/

module FastANI {
    /*
        Insert your typespec information here.
    */
    typedef structure {
    } Params;

    typedef structure {
        float percentage_match;
        int total_fragments;
        int orthologous_matches;
    } Result;

    funcdef fast_ani(Params params) returns (Result results) authentication required;
};
