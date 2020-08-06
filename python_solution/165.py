'''
165. Compare Version Numbers
Medium

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number
to be 0. For example, version number 3.4 has a revision number of 3 and 4
for its first and second level revision number. 
Its third and fourth level revision number are both 0.
'''
from itertools import zip_longest
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list = [int(i) for i in version1.split('.')]
        v2_list = [int(i) for i in version2.split('.')]

        for i , j in zip_longest(v1_list,v2_list,fillvalue=0):
            if i > j:
                return 1
            elif i < j:
                return -1
        else:
            return 0


foo = Solution()
print(foo.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))
#Input: version1 = "7.5.2.4", version2 = "7.5.3" ; output: -1
# Input: version1 = "1.01", version2 = "1.001" rt: 0
# Input: version1 = "1.0", version2 = "1.0.0" ; rt : 0