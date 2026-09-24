class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int rows = image.length;
        int cols = image[0].length;
        Queue<int[]> qu = new ArrayDeque<>();
        
        int[][] directions = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
        };
        int originalColor = image[sr][sc];
        if (originalColor == color) {
            return image;
        }

        qu.offer(new int[]{sr, sc});
        image[sr][sc]=color;

        while (qu.size() > 0) {
            int[] p = qu.poll();
            int r = p[0];
            int c = p[1];
            
            for (int[] dir : directions) {
                int dx = dir[0];
                int dy = dir[1];

                int new_r = r + dx;
                int new_c = c + dy;

                // Out of bounds
                if (new_r < 0 || new_r >= rows ||
                    new_c < 0 || new_c >= cols) {
                    continue;
                }

                if (image[new_r][new_c] != originalColor) {
                    continue;
                }
                image[new_r][new_c] = color;
                qu.offer(new int[] {new_r, new_c});
            }
        }

        return image;
    }
}

    