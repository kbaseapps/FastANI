/*
 * A KBase module: FastANI
 */

module FastANI {
    typedef string workspace_ref;

    /* fast_ani input */
    typedef structure {
        string workspace_name;
        list<workspace_ref> reference;
        list<workspace_ref> query;
    } FastANIParams;

    /* fast_ani output */
    typedef structure {
        string report_name;
        string report_ref;
    } FastANIResults;

    funcdef fast_ani(FastANIParams params) returns (FastANIResults results) authentication required;
};
