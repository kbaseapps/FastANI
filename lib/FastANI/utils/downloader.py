"""
Download either a Genome or Assembly.
"""
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.AssemblyUtilClient import AssemblyUtil
import os

QUERY = "query"
REF = "reference"

INPUT_TYPES = [QUERY, REF]


def dedupe_input(params):
    """
    Filter params to remove empty or duplicate inputs and ensure there is no intersection between query and reference input
    """
    input_ids = {
        QUERY: set(params[QUERY]),
        REF: set(params[REF]),
    }

    no_input = []
    for input_type in INPUT_TYPES:
        input_set = input_ids[input_type]
        for discard in ["", None]:
            input_set.discard(discard)
        if len(input_set) == 0:
            no_input.append(input_type)

    if len(no_input):
        raise ValueError("No valid inputs found in " + " or ".join(no_input) + " set")

    # check there are no duplicates between query and reference IDs
    shared_ids = input_ids[QUERY] & input_ids[REF]
    if len(shared_ids):
        shared_id_list = sorted(list(shared_ids))
        raise ValueError(
            "IDs found in query and reference sets:\n" + "\n".join(shared_id_list)
        )

    input_ids["all"] = input_ids[QUERY] | input_ids[REF]

    return input_ids


def dump_paths_to_file(paths, scratch):
    args_files = {}

    # make sure that the scratch dir exists
    if not os.path.isdir(scratch):
        os.makedirs(scratch)

    for input_type in INPUT_TYPES:
        file_path = os.path.join(scratch, input_type + ".txt")
        with open(file_path, "w") as file:
            file.write("\n".join(paths[input_type]) + "\n")
        args_files[input_type] = file_path
    return args_files


def get_assembly_ref_from_genome(genome_ref, ws_obj):
    """
    Given a Genome object, find the reference to its Assembly object.
    Arguments:
      ref is a workspace reference ID in the form 'workspace_id/object_id/version'
      ws_obj download workspace object for the genome
    Returns a workspace reference to an assembly object
    """
    # Extract out the assembly reference from the workspace data
    ws_data = ws_obj["data"]
    assembly_ref = ws_data.get("contigset_ref") or ws_data.get("assembly_ref")
    if not assembly_ref:
        name = ws_obj["info"][1]
        raise TypeError(
            "The Genome " + name + " has no assembly or contigset references"
        )
    # Return a reference path of `genome_ref;assembly_ref`
    return genome_ref + ";" + assembly_ref


def download_fasta(params, scratch, cb_url):
    """
    Args:
      params - dictionary with keys 'query' and 'reference', both containing workspace references in the form 'workspace_id/object_id/obj_version'
      scratch - scratch directory for file storage
      cb_url - callback server URL
    Returns a dict with keys 'query' and 'reference' and values a list of file paths
    """

    input_ids = dedupe_input(params)
    paths = {QUERY: [], REF: []}

    dfu = DataFileUtil(cb_url)
    assembly_util = AssemblyUtil(cb_url)
    ws_objects = dfu.get_objects({"object_refs": list(input_ids["all"])})

    for (obj, ref) in zip(ws_objects["data"], list(input_ids["all"])):
        ws_type = obj["info"][2]
        if "KBaseGenomes.Genome" in ws_type:
            assembly_ref = get_assembly_ref_from_genome(ref, obj)
        elif "KBaseGenomeAnnotations.Assembly" in ws_type:
            assembly_ref = ref
        else:
            raise TypeError(
                "Invalid type " + ws_type + ". Must be an Assembly or Genome."
            )
        path = assembly_util.get_assembly_as_fasta({"ref": assembly_ref})["path"]
        if ref in input_ids[QUERY]:
            paths[QUERY].append(path)
        else:
            paths[REF].append(path)

    return dump_paths_to_file(paths, scratch)
