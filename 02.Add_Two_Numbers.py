class Solution:
    def addTwoNumbers(self, l1, l2):
        base_node = ListNode(0)
        current_node = base_node
        carry = 0

        while l1 or l2 or carry:
            first_value = l1.val if l1 else 0
            second_value = l2.val if l2 else 0

            total = first_value + second_value + carry

            carry = total // 10
            digit = total % 10

            current_node.next = ListNode(digit)
            current_node = current_node.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return base_node.next