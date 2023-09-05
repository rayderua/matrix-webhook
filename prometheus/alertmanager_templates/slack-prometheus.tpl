{{ define "slack.prometheus.title" -}}
[{{ .Status | toUpper }} : {{ if eq .Status "firing" -}}{{ .Alerts.Firing | len }}{{- else -}}{{ .Alerts.Resolved | len }}{{- end -}}] {{ .CommonLabels.alertname }} {{if .CommonLabels.tag }} - {{ .CommonLabels.tag }} {{end}}
{{- end }}

{{ define "slack.prometheus.text" -}}
    {{ if eq .Status "firing" -}}
        {{ range .Alerts.Firing -}}
            <table>
              <tr>
                <td>
                  <font color="#ff3300">
                    <h5> [ KO ] {{ .Labels.alertname }} {{if .Labels.tag }} - {{ .Labels.tag }} {{end}} </h5>
                  </font>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>Labels:</strong><br />
                  {{ range .Labels.SortedPairs }}{{ .Name }} = {{ .Value }}<br />{{ end -}}
                  {{ if gt (len .Annotations) 0 }}<strong>Annotations</strong><br />{{ end -}}
                  {{ range .Annotations.SortedPairs }}{{ .Name }} = {{ .Value }}<br />{{ end -}}
                </td>
              </tr>
            </table>
        {{ end }}
    {{- end -}}
    {{ if eq .Status "resolved" -}}
        {{ range .Alerts.Resolved -}}
            <table>
              <tr>
                <td>
                  <font color="#009933">
                    <h5> [ OK ] {{ .Labels.alertname }} {{if .Labels.tag }} - {{ .Labels.tag }} {{end}} </h5>
                  </font>
                </td>
              </tr>
              <tr>
                <td>
                  <strong>Labels:</strong><br />
                  {{ range .Labels.SortedPairs }}{{ .Name }} = {{ .Value }}<br />{{ end -}}
                  {{ if gt (len .Annotations) 0 }}<strong>Annotations</strong><br />{{ end -}}
                  {{ range .Annotations.SortedPairs }}{{ .Name }} = {{ .Value }}<br />{{ end -}}
                </td>
              </tr>
            </table>
        {{ end }}
    {{- end -}}
{{- end -}}

