

class HtmlNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode<tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}>"

    def to_html(self):
        if self.children is not None:
            return f"<{self.tag}>" + ''.join([child.to_html() for child in self.children]) + f"</{self.tag}>"
        return f"<{self.tag}>" + str(self.value) + f"</{self.tag}>"

    def props_to_html(self):
        output = ""
        for key, value in self.props.items():
            output += f' {key}="{value}"'
        return output
