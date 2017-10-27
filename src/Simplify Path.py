class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        assert path[0] == '/'
        parts = path[1:].split('/')
        curdir = []
        for p in parts:
#             print curdir, p
            if p == '.' or p == '': 
                pass
            elif p == '..':
                if curdir: 
                    del curdir[-1]
            else:
                curdir.append(p)
        
        if curdir:
            return '/' + '/'.join(curdir)
        else:
            return '/'
    
print Solution().simplifyPath('/../')
print Solution().simplifyPath('/')
print Solution().simplifyPath('/home//foo')
print Solution().simplifyPath('/home/')
print Solution().simplifyPath('/a/./b/../../c/')