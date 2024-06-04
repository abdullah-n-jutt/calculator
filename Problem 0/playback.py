def periods(sentance):
    words = sentance.split()
    sentance_periods = '...'.join(words)
    return(sentance_periods)

sentance = input("")
result = periods(sentance)
print(result)
