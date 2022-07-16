terms['{{term}}']=Array();
{% regroup rows by pos as term_by_pos %}
{% for pos in term_by_pos %}
     terms['{{term}}']['{{ pos.grouper }}']=Array();
{% regroup pos.list by sense as term_list %}
{% for t in term_list %}
{% if forloop.first %}
     terms['{{term}}']['{{ pos.grouper }}']['def']=Array();
{% endif %}
{% for item in t.list %}
{% if forloop.first %}
     terms['{{term}}']['{{ pos.grouper }}']['def'][{{ t.grouper }}]="{{ item.sdef }}";
     terms['{{term}}']['{{ pos.grouper }}'][{{ t.grouper }}]={ {% endif %}
     '{{ item.linklem }}':'{{ item.link }}', {% endfor %}
     }
{% endfor %}
{% endfor %}
