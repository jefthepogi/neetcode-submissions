class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, bool> existed;
        for (int i=0; i<nums.size(); i++) {
            if (existed.count(nums[i]) <= 0) { 
                existed[nums[i]] = true;
            } else { return true; }
        }
        return false;
    }
};
