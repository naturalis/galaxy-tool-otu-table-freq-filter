# galaxy-tool-otu-table-freq-filter  
Frequency filter for otu tables with unique otu exception  

## Installation
### Manual  
Clone this repo in your Galaxy ***Tools*** directory:  
`git clone https://github.com/naturalis/galaxy-tool-otu-table-freq-filter`  

Make sure the script are executable:  
`chmod 755 galaxy-tool-otu-table-freq-filter/freq_filter_otutable.sh`  
`chmod 755 galaxy-tool-otu-table-freq-filter/freq_filter_otutable.py`  

Append the file ***tool_conf.xml***:    
`<tool file="/path/to/Tools/galaxy-tool-otu-table-freq-filter/freq_filter_otutable.xml" />`  

### Ansible
Depending on your setup the [ansible.builtin.git](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html) module could be used.  
[Install the tool](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html#examples) by including the following in your dedicated ***.yml** file:  

`  - repo: https://github.com/naturalis/galaxy-tool-otu-table-freq-filter`  
&ensp;&ensp;`freq_filter_otutable.xml`  
&ensp;&ensp;`version: master`  
