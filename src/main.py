from textnode import *
from htmlnode import *


def main():
    testtextnode = TextNode(
        "this is some anchor text", TextType("bold"), "https://www.boot.dev"
    )
    prop = {"href": "https://www.google.com", "target": "_blank"}
    testhtmlnode = HTMLNode("TAG", "VALUE", None, prop)
    prettyprop = testhtmlnode.props_to_html()
    print(testtextnode, testhtmlnode, prettyprop)


if __name__ == "__main__":
    main()
