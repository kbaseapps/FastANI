/*
 * A KBase module: FastANI
 */

module FastANI {
    /*
     *  Insert your typespec information here.
     */
    typedef structure {
        string workspace_name;
    } Params;

    typedef structure {
        string report_name;
        string report_ref;
        float percentage_match;
        int total_fragments;
        int orthologous_matches;
    } Result;

    funcdef fast_ani(Params params) returns (Result results) authentication required;
};
