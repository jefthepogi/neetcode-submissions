class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j;
        std::map<int,int> index;
        for (int c=0; c<nums.size(); c++) {
            int v = nums[c];
            int d = target - v;
            if (index.find(d) != index.end()) {
                if (index[d] <= c) {
                    i = index[d];
                    j = c;
                } else {
                    i = c;
                    j = index[d];
                } 
            } else {
                index[v] = c;
            }
        }
        return vector<int>{i, j};
    }
};
