from htmlnode import HtmlNode


class ParentNode(HtmlNode):

    def __init__(self, tag, children, props):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("no tag present")
        if not self.children:
            raise ValueError("no children present")
        value = ''.join([node.to_html() for node in self.children])
        if self.props:
            props = self.props_to_html()
            return f"<{self.tag}{props}>{value}</{self.tag}>"
        else:
            return f"<{self.tag}>{value}</{self.tag}>"
