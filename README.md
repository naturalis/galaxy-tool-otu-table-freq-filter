# galaxy-tool-otu-table-freq-filter
Frequency filter for otu tables with unique otu exception
## Getting Started  
(user: **galaxy**)  
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
```
```
git clone https://github.com/naturalis/galaxy-tool-otu-table-freq-filter
```
```
chmod 777 galaxy-tool-otu-table-freq-filter/freq_filter_otutable.py
```
Add the following line to /home/galaxy/galaxy/config/tool_conf.xml
```
<tool file="/home/galaxy/Tools/galaxy-tool-otu-table-freq-filter/freq_filter_otutable.xml" />
```
