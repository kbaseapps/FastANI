
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
    "query_genome",
    "reference_genome",
    "reference_list"
})
public class FastANIParams {

    @JsonProperty("workspace_name")
    private java.lang.String workspaceName;
    @JsonProperty("query_genome")
    private java.lang.String queryGenome;
    @JsonProperty("reference_genome")
    private java.lang.String referenceGenome;
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

    @JsonProperty("query_genome")
    public java.lang.String getQueryGenome() {
        return queryGenome;
    }

    @JsonProperty("query_genome")
    public void setQueryGenome(java.lang.String queryGenome) {
        this.queryGenome = queryGenome;
    }

    public FastANIParams withQueryGenome(java.lang.String queryGenome) {
        this.queryGenome = queryGenome;
        return this;
    }

    @JsonProperty("reference_genome")
    public java.lang.String getReferenceGenome() {
        return referenceGenome;
    }

    @JsonProperty("reference_genome")
    public void setReferenceGenome(java.lang.String referenceGenome) {
        this.referenceGenome = referenceGenome;
    }

    public FastANIParams withReferenceGenome(java.lang.String referenceGenome) {
        this.referenceGenome = referenceGenome;
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
        return ((((((((((("FastANIParams"+" [workspaceName=")+ workspaceName)+", queryGenome=")+ queryGenome)+", referenceGenome=")+ referenceGenome)+", referenceList=")+ referenceList)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
