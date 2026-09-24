class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        int fresh_cnt = 0;
        Queue<int[]> qu = new ArrayDeque<>();

        int[][] directions = {
            {0, 1},
            {0, -1},
            {1, 0},
            {-1, 0}
        };

        // Count fresh oranges and add initially rotten oranges to queue
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    fresh_cnt++;
                } else if (grid[r][c] == 2) {
                    qu.offer(new int[]{r, c});
                }
            }
        }

        int minutes = 0;

        while (qu.size() > 0 && fresh_cnt > 0) {
            int l = qu.size();
            minutes++;

            for (int i = 0; i < l; i++) {
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

                    // Not a fresh orange
                    if (grid[new_r][new_c] != 1) {
                        continue;
                    }

                    // Make it rotten
                    grid[new_r][new_c] = 2;
                    fresh_cnt--;

                    // Process this orange in the next minute
                    qu.offer(new int[]{new_r, new_c});
                }
            }
        }

        if (fresh_cnt > 0) {
            return -1;
        }

        return minutes;
    }
}
