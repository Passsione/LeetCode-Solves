/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        BigInteger f = trans_ListNode(l1);
        BigInteger s = trans_ListNode(l2);
        BigInteger final_int = f + s;
        char[] final_str = final_int.ToString().ToCharArray();

        ListNode finalLN = new ListNode((int)char.GetNumericValue(final_str[0]));

        for (int i = 1; i < final_str.Length; i++){
            ListNode nextNode = new ListNode((int)char.GetNumericValue(final_str[i]), finalLN);
            finalLN = nextNode;
        } 
        return finalLN;
    }

    public BigInteger trans_ListNode(ListNode l){
        BigInteger val = (BigInteger) l.val;
        ListNode nV = l.next;
        BigInteger mag = 10;
        while (nV != null){
            val = val + nV.val * mag;
            mag = mag * 10;
            nV = nV.next;
        }
        return val;
    }
}