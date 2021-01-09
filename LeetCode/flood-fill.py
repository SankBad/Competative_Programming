class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        return self.dfs(image, sr, sc, newColor, color)
        
    def dfs(self, image, sr, sc, newColor, color):
        if sr<0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc]!=color:
            return image
        image[sr][sc]= newColor
        self.dfs(image, sr, sc+1, newColor, color)
        self.dfs(image, sr, sc-1, newColor, color)
        self.dfs(image, sr-1, sc, newColor, color)
        self.dfs(image, sr+1, sc, newColor, color)
        return image
