def myxml(tag, content='', **kwargs):
    attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f'<{tag}{attrs}>{content}</{tag}>'
