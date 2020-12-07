import wget

def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

wget.download("https://cursofullstack.com.br/python/exemplo-wget.zip", bar=bar_custom)

