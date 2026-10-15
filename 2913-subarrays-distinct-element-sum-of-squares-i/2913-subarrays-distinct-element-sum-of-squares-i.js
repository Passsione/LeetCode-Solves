/**
 * @param {number[]} nums
 * @return {number}
 */
var sumCounts = function(nums) {

    var sumSqu = nums.length;
    
    var setSize = 2;
    while(setSize <= nums.length){
        let l = setSize < nums.length ? nums.length - 1 : 1;
        for(let i = 0; i < l; i++){
            let arr = nums.slice(i, i + setSize);
            if (arr.length < setSize)break;                            

            let temp = new Set(arr);
            sumSqu += temp.size * temp.size;   

        }
        setSize++;
    }

    return sumSqu;   
    
};