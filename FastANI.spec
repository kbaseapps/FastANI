/*
 * A KBase module: FastANI
 */

module FastANI {
    /* @id ws KBaseGenomeAnnotations.Assembly */
    typedef string workspace_ref;

    /* fast_ani input */
    typedef structure {
        string workspace_name;
        list<workspace_ref> assembly_refs;
    } FastANIParams;

    /* fast_ani output */
    typedef structure {
        string report_name;
        string report_ref;
    } FastANIResults;

    funcdef fast_ani(FastANIParams params) returns (FastANIResults results) authentication required;
};
