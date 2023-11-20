from django import template


register = template.Library()

@register.filter()
def censor(text):
    l = text.split()
    restricted_words = ['ipsum']
    res = []
    for w in l:
        m = w.lower()
        if m in restricted_words:
            s = w[0] + '*' * (len(w) - 1)
            res.append(s)
        else:
            res.append(w)
    return ' '.join(res)