#include "lists.h"
#include <stdio.h>

void reverseLinkedList(Node **head);
int areListsEquivalent(listint_t *list1, listint_t *list2);

/**
 * isPalindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not a palindrome), 1 (is a palindrome)
 */
int isPalindrome(listint_t **head)
{
listint_t *slow, *fast, *prev_slow, *first_half, *second_half, *mid;

if (!head || !(*head) || !((*head)->next))
    return 1;

slow = fast = prev_slow = *head;
second_half = mid = NULL;

do
{
    fast = fast->next;
    if (fast)
    {
        fast = fast->next;
        prev_slow = slow;
        slow = slow->next;
    }
} while (fast && fast->next);

if (fast == NULL)
    second_half = slow;
else
{
    mid = slow;
    second_half = slow->next;
}

prev_slow->next = NULL;
reverseList(&second_half);

if (areListsEqual(*head, second_half))
    return 1;
else
    return 0;
}

/**
 * areListsEquivalent - checks if two linked lists contain identical data and are
 *                     the same length as each other
 * @list1: list one to compare to list two
 * @list2: list two to compare to list one
 *
 * Return: 1 (equivalent) 0 (not equal)
 */
int areListsEquivalent(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->data != list2->data)
            return 0;
        
        list1 = list1->next;
        list2 = list2->next;
    }
    
    if (list1 != NULL || list2 != NULL)
        return 0;
    
    return 1;
}
/**
 * reverseLinkedList - reverses a linked list in place
 * @head: double pointer to the head of the linked list
 *
 * This function reverses the order of a linked list by modifying the pointers
 * of each node. The head pointer itself is modified to point to the new head
 * of the reversed list.
 *
 * Return: void
 */
void reverseLinkedList(Node **head)
{
    Node *current = *head;
    Node *previous = NULL;
    Node *nextNode = NULL;

    while (current != NULL)
    {
        nextNode = current->next;
        current->next = previous;
        previous = current;
        current = nextNode;
    }
    *head = previous;
}
