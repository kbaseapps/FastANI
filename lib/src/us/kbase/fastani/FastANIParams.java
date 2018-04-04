
package us.kbase.fastani;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: FastANIParams</p>
 * <pre>
 * fast_ani input
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "query_assembly_refs",
    "reference_assembly_refs"
})
public class FastANIParams {

    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("query_assembly_refs")
    private List<String> queryAssemblyRefs;
    @JsonProperty("reference_assembly_refs")
    private List<String> referenceAssemblyRefs;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("workspace_name")
    public java.lang.String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public FastANIParams withWorkspaceName(java.lang.String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("query_assembly_refs")
    public List<String> getQueryAssemblyRefs() {
        return queryAssemblyRefs;
    }

    @JsonProperty("query_assembly_refs")
    public void setQueryAssemblyRefs(List<String> queryAssemblyRefs) {
        this.queryAssemblyRefs = queryAssemblyRefs;
    }

    public FastANIParams withQueryAssemblyRefs(List<String> queryAssemblyRefs) {
        this.queryAssemblyRefs = queryAssemblyRefs;
        return this;
    }

    @JsonProperty("reference_assembly_refs")
    public List<String> getReferenceAssemblyRefs() {
        return referenceAssemblyRefs;
    }

    @JsonProperty("reference_assembly_refs")
    public void setReferenceAssemblyRefs(List<String> referenceAssemblyRefs) {
        this.referenceAssemblyRefs = referenceAssemblyRefs;
    }

    public FastANIParams withReferenceAssemblyRefs(List<String> referenceAssemblyRefs) {
        this.referenceAssemblyRefs = referenceAssemblyRefs;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((("FastANIParams"+" [workspaceName=")+ workspaceName)+", queryAssemblyRefs=")+ queryAssemblyRefs)+", referenceAssemblyRefs=")+ referenceAssemblyRefs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
