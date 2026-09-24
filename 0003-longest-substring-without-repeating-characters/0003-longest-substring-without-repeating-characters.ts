function lengthOfLongestSubstring(s: string): number {

    let output = 0;
    let hold = "";
    for (let i = 0; i < s.length; i++) {
        let letter = s[i];
        let index = hold.indexOf(letter);
        if (index > -1)
            hold = hold.slice(index + 1)
        
        hold += letter;
        
        if (hold.length >= output) {
            output = hold.length;
        }
    }

    return output;
};