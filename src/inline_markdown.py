from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


def split_nodes_image(old_nodes):
    lst = []
    for nodes in old_nodes:
        matches = extract_markdown_images(nodes.text)
        print(matches)
        original_text = nodes.text
        for match in matches:
            image_alt = match[0]
            image_link = match[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            print(sections)
            if len(sections) > 1:
                original_text = sections[1]
            lst.append(TextNode(sections[0], TextType.TEXT))
            lst.append(TextNode(image_alt, TextType.IMAGE, image_link))
    return lst


def split_nodes_link(old_nodes):
    lst = []
    for nodes in old_nodes:
        matches = extract_markdown_links(nodes.text)
        original_text = nodes.text
        for match in matches:
            link_alt = match[0]
            link_link = match[1]
            sections = original_text.split(f"![{link_alt}]({link_link})", 1)
            if len(sections) > 1:
                original_text = sections[1]
            lst.append(TextNode(sections[0], TextType.TEXT))
            lst.append(TextNode(link_alt, TextType.IMAGE, link_link))
    return lst
