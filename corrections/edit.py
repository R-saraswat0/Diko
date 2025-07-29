# corrections/edit_distance.py

def edit_distance(word1, word2):
    """
    Yeh function do words ke beech edit distance calculate karta hai.
    """
    if not word1 or not word2:
        return max(len(word1) if word1 else 0, len(word2) if word2 else 0)
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    return dp[m][n]

def get_closest_words(query, word_list, top_n=3):
    """
    Yeh function query ke sabse kareeb words return karta hai
    edit distance ke basis par.
    """
    distances = []
    for word in word_list:
        try:
            dist = edit_distance(query.lower(), word.lower())
            distances.append((word, dist))
        except Exception:
            continue
    distances.sort(key=lambda x: x[1])
    return [word for word, dist in distances[:top_n]]
