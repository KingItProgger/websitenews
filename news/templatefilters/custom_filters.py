from django import template

register = template.Library()



non_cenzor_words=[
    'uncenz1','uncenz2','uncenz3','uncenz4'
]


non_cenzor_words=[
    'uncenz1','uncenz2','uncenz3','uncenz4'
]

@register.filter()
def censor(value:str):
    value=value.split()
    for v in range(len(value)):
        if value[v] in non_cenzor_words:
            value[v]='*'*len(value[v])
    value=" ".join(value)

    return value