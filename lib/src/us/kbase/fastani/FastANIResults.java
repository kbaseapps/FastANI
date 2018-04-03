
package us.kbase.fastani;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: FastANIResults</p>
 * <pre>
 * fast_ani output
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_name",
    "report_ref",
    "percentage_match",
    "total_fragments",
    "orthologous_matches"
})
public class FastANIResults {

    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_ref")
    private String reportRef;
    @JsonProperty("percentage_match")
    private Double percentageMatch;
    @JsonProperty("total_fragments")
    private Long totalFragments;
    @JsonProperty("orthologous_matches")
    private Long orthologousMatches;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public FastANIResults withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public FastANIResults withReportRef(String reportRef) {
        this.reportRef = reportRef;
        return this;
    }

    @JsonProperty("percentage_match")
    public Double getPercentageMatch() {
        return percentageMatch;
    }

    @JsonProperty("percentage_match")
    public void setPercentageMatch(Double percentageMatch) {
        this.percentageMatch = percentageMatch;
    }

    public FastANIResults withPercentageMatch(Double percentageMatch) {
        this.percentageMatch = percentageMatch;
        return this;
    }

    @JsonProperty("total_fragments")
    public Long getTotalFragments() {
        return totalFragments;
    }

    @JsonProperty("total_fragments")
    public void setTotalFragments(Long totalFragments) {
        this.totalFragments = totalFragments;
    }

    public FastANIResults withTotalFragments(Long totalFragments) {
        this.totalFragments = totalFragments;
        return this;
    }

    @JsonProperty("orthologous_matches")
    public Long getOrthologousMatches() {
        return orthologousMatches;
    }

    @JsonProperty("orthologous_matches")
    public void setOrthologousMatches(Long orthologousMatches) {
        this.orthologousMatches = orthologousMatches;
    }

    public FastANIResults withOrthologousMatches(Long orthologousMatches) {
        this.orthologousMatches = orthologousMatches;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("FastANIResults"+" [reportName=")+ reportName)+", reportRef=")+ reportRef)+", percentageMatch=")+ percentageMatch)+", totalFragments=")+ totalFragments)+", orthologousMatches=")+ orthologousMatches)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
