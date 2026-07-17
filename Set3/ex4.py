def build_xml_element(tag, content, **attributes):
    attr_parts = []
    for key, value in attributes.items():
        if key.startswith("_"):
            key = key[1:] + "_"
        attr_parts.append(f'{key}="{value}"')

    attrs_string = " ".join(attr_parts)
    if attrs_string:
        attrs_string = " " + attrs_string

    return f"<{tag}{attrs_string}>{content}</{tag}>"

print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
