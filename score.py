def score(words, word_score):
    word_scores = list(map(word_score, words))
    return(sum(word_scores))

def word_score(word):
    if len(word) > 7:
        return 11
    scores = { 4: 1, 5: 2, 6: 3, 7: 4 }
    return scores[len(word)]
