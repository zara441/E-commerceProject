from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list,chunk_size):
    """

    creating a custom template tag

    """
    i = 0
    chunk = []
    for x in list:
        chunk.append(x)
        i += 1
        if i == chunk_size:
            yield chunk
            chunk = []
            i = 0
    yield chunk        