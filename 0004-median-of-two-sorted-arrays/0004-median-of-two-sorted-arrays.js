/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {

    const m = nums1.length, n = nums2.length;
    let evenTotal = Math.floor((m + n) / 2) == (m + n) / 2;

    // if(n == 0 || m == 0){
    //     const consider = n == 0 ? nums1 : nums2;
    //     let div = consider.length / 2;
    //     if(evenTotal) return (consider[div - 1] + consider[div]) / 2;        
    //     return consider[Math.floor(div)];
    // }
    
    let lesser = n <= m;
    let archor = lesser ? nums1 : nums2;
    let hold = lesser ? nums2 : nums1;

    var limit = archor.length;

    for(let i = 0; i < limit; i++){
    
        if (hold.length <=  0) break;

        let h = hold[0];
        if(h <= archor[i]){
            archor.splice(i, 0, h);
            hold.shift();
            limit++;
        }

        // Early returns
        if(i == (m + n) / 2 && evenTotal){
            return (archor[i - 1] + archor[i]) / 2;
        }else if(i == Math.floor((m + n) / 2) && !evenTotal)
            return archor[i];
    }

    if (hold.length > 0){
        archor.push(...hold);
    }

    let div = archor.length / 2;

    if(evenTotal) return (archor[div - 1] + archor[div]) / 2;
    return archor[Math.floor(div)];
    
};