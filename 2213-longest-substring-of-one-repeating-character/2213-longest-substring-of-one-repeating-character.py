class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_left = [''] * (4 * n)
        tree_right = [''] * (4 * n)
    
        s_chars = list(s)

        def merge(node, l_child, r_child, l_len, r_len):
            tree_left[node] = tree_left[l_child]
            tree_right[node] = tree_right[r_child]
            
         
            tree_pref[node] = tree_pref[l_child]
            tree_suff[node] = tree_suff[r_child]

            tree_max[node] = max(tree_max[l_child], tree_max[r_child])
   
            if tree_right[l_child] == tree_left[r_child]:
                cross_len = tree_suff[l_child] + tree_pref[r_child]
                tree_max[node] = max(tree_max[node], cross_len)
            
                if tree_pref[l_child] == l_len:
                    tree_pref[node] = l_len + tree_pref[r_child]
             
                if tree_suff[r_child] == r_len:
                    tree_suff[node] = r_len + tree_suff[l_child]

        def build(node, l, r):
            if l == r:
                tree_max[node] = 1
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_left[node] = s_chars[l]
                tree_right[node] = s_chars[l]
                return
            
            mid = (l + r) // 2
            l_child, r_child = 2 * node, 2 * node + 1
            build(l_child, l, mid)
            build(r_child, mid + 1, r)
            
            merge(node, l_child, r_child, mid - l + 1, r - mid)

        def update(node, l, r, idx, ch):
            if l == r:
                tree_left[node] = ch
                tree_right[node] = ch
                return
            
            mid = (l + r) // 2
            l_child, r_child = 2 * node, 2 * node + 1
            
            if idx <= mid:
                update(l_child, l, mid, idx, ch)
            else:
                update(r_child, mid + 1, r, idx, ch)
                
            merge(node, l_child, r_child, mid - l + 1, r - mid)


        build(1, 0, n - 1)
        
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            
            update(1, 0, n - 1, idx, ch)
            ans.append(tree_max[1])
            
        return ans