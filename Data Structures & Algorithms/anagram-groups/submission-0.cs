public class Solution
{
    public List<List<string>> GroupAnagrams(string[] strs)
    {
        Dictionary<string, List<string>> anagrams = new Dictionary<string, List<string>>();

        foreach (string s in strs)
        {
            string code = CreateAnagramCode(s);

            if (!anagrams.ContainsKey(code))
            {
                anagrams[code] = new List<string>();
            }

            anagrams[code].Add(s);
        }

        List<List<string>> result = new List<List<string>>();

        foreach (List<string> group in anagrams.Values)
        {
            result.Add(group);
        }

        return result;
    }

    public string CreateAnagramCode(string s)
    {
        Dictionary<char, int> counts = new Dictionary<char, int>();

        foreach (char letter in s)
        {
            int count = counts.GetValueOrDefault(letter, 0);
            counts[letter] = count + 1;
        }

        string code = "";

        foreach (char l in "abcdefghijklmnopqrstuvwxyz")
        {
            code += l + counts.GetValueOrDefault(l, 0).ToString();
        }

        return code;
    }
}