class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        map<char, int> frequency;
        for (int i=0; i<s.length(); i++) {
            frequency[s[i]] += 1;
            frequency[t[i]] -= 1;
        }

        for (auto& f : frequency) {
            if (f.second != 0)
                return false;
        }
        return true;
    }
};
