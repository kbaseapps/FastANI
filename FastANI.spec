/*
 * A KBase module: FastANI
 */

module FastANI {
    /* fast_ani input */
    typedef structure {
        string workspace_name;
        list<string> query_assembly_refs;
        list<string> reference_assembly_refs;
    } FastANIParams;

    /* fast_ani output */
    typedef structure {
        string report_name;
        string report_ref;
    } FastANIResults;

    funcdef fast_ani(FastANIParams params) returns (FastANIResults results) authentication required;
};
