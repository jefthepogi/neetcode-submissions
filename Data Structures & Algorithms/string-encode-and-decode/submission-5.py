class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "_^_"
        encoded_string = "-@-".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "_^_":
            return []
        if len(s) == 0:
            return [""] 
        res = s.split("-@-")
        return res
