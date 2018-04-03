
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
    "query_assembly",
    "reference_assembly",
    "reference_list"
})
public class FastANIParams {

    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("query_assembly")
    private java.lang.String queryAssembly;
    @JsonProperty("reference_assembly")
    private java.lang.String referenceAssembly;
    @JsonProperty("reference_list")
    private List<String> referenceList;
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

    @JsonProperty("query_assembly")
    public java.lang.String getQueryAssembly() {
        return queryAssembly;
    }

    @JsonProperty("query_assembly")
    public void setQueryAssembly(java.lang.String queryAssembly) {
        this.queryAssembly = queryAssembly;
    }

    public FastANIParams withQueryAssembly(java.lang.String queryAssembly) {
        this.queryAssembly = queryAssembly;
        return this;
    }

    @JsonProperty("reference_assembly")
    public java.lang.String getReferenceAssembly() {
        return referenceAssembly;
    }

    @JsonProperty("reference_assembly")
    public void setReferenceAssembly(java.lang.String referenceAssembly) {
        this.referenceAssembly = referenceAssembly;
    }

    public FastANIParams withReferenceAssembly(java.lang.String referenceAssembly) {
        this.referenceAssembly = referenceAssembly;
        return this;
    }

    @JsonProperty("reference_list")
    public List<String> getReferenceList() {
        return referenceList;
    }

    @JsonProperty("reference_list")
    public void setReferenceList(List<String> referenceList) {
        this.referenceList = referenceList;
    }

    public FastANIParams withReferenceList(List<String> referenceList) {
        this.referenceList = referenceList;
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
        return ((((((((((("FastANIParams"+" [workspaceName=")+ workspaceName)+", queryAssembly=")+ queryAssembly)+", referenceAssembly=")+ referenceAssembly)+", referenceList=")+ referenceList)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
