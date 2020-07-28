<link href="pytm/docs/Stylesheet.css" rel="stylesheet"></link>

<h2> System Description</h2>
&nbsp;

{tm.description}

&nbsp;

<h2> Potential Threats</h2>
&nbsp;
&nbsp;

{findings:repeat:
<details>
<summary>   {{item.name_uuid}}    </summary>
{{item.children:repeat:
<details>
<summary>   {{{{item.cat}}}}:  </summary>
<h6>Target Element</h6>
<p>{{{{item.name}}}}</p>
<h6>Score:</h6>
<p>{{{{item.score}}}}</p>
<h6>CAPEC threats</h6>
{{{{item.children:repeat:
<details>
<summary>{{{{{{{{item.id}}}}}}}} -- {{{{{{{{item.name}}}}}}}}</summary>
<h6>Description of CAPEC Threat:</h6>
<p>{{{{{{{{item.description}}}}}}}}</p>
<h6>CAPEC Score:</h6>
<p>{{{{{{{{item.score}}}}}}}}</p>
<h6>CWEs:</h6>
{{{{{{{{item.children:repeat:
<details>
<summary>{{{{{{{{{{{{{{{{item.id}}}}}}}}}}}}}}}} -- {{{{{{{{{{{{{{{{item.name}}}}}}}}}}}}}}}}</summary>
<h6>CWE Description:</h6>
<p>{{{{{{{{{{{{{{{{item.description}}}}}}}}}}}}}}}}</p>
<h6>CWE Score:</h6>
<p>{{{{{{{{{{{{{{{{item.score}}}}}}}}}}}}}}}}</p>
<h6>Mitigation(s):</h6>
{{{{{{{{{{{{{{{{item.children:repeat:
<p>
{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{item.name}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
</p>
}}}}}}}}}}}}}}}}
</details>
}}}}}}}}
</details>
}}}}
</details>
}}
</details>
&nbsp;
&nbsp;

}

