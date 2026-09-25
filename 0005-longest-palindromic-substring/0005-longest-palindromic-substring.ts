// function longestPalindrome(s: string): string {

//     let len = s.length;
//     if (len == 1) return s;

//     let palin = "";
//     let hold = ""; //`${len}`;

//     for (let i = 0; i < len; i++) {
//         let iLetter = s[i];
//         let end = [];

//         for (let j = len - 1; j > i; j--) {
//             if (iLetter == s[j]) {
//                 end.push(j);
//             }

//             if (end.length > 0 && s[i + end[0] - j] != s[j]) {
//                 end.splice(0, 1);
//                 j++;                        
//             }
//         }

//         if (end.length > 0) hold = s.slice(i, end[0] + 1);
//         else hold = iLetter;

//         if (hold.length >= palin.length) {
//             palin = hold;
//         }
//     }

//     return palin;

// };

function longestPalindrome(s: string): string {
    let check = (i: number, j: number) => {
        let left = i;
        let right = j - 1;

        while (left < right) {
            if (s.charAt(left) !== s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    };

    for (let length = s.length; length > 0; length--) {
        for (let start = 0; start <= s.length - length; start++) {
            if (check(start, start + length)) {
                return s.substring(start, start + length);
            }
        }
    }

    return "";
}