class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        completed = 0
        start = beginWord
        length = len(beginWord)
        output = length*[0]
        for i in range(completed, len(wordList)):
            for j in range(length):
                if start.replace(start[j], '', 1) == wordList[i].replace(wordList[i][j], '', 1):
                    start = wordList[i]
                    output[completed] =  wordList[i]
                    wordList[i] = wordList[completed]
                    wordList[completed] = output[completed]
                    completed = completed + 1
                    break
            for p in range(length):
                if start.replace(start[p], '', 1) == endWord.replace(endWord[p], '', 1):
                    print(output)
                    return completed + 2
