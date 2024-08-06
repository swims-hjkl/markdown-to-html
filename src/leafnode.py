from htmlnode import HtmlNode


class LeafNode(HtmlNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("no value present")

        if not self.tag:
            return str(self.value)

        if self.props:
            props_html = self.props_to_html()
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __eq__(self, o):
        return self.value == o.value and self.tag == o.tag and self.props == o.props
