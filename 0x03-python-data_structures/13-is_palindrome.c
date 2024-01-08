#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int list_equiv(listint_t *l1, listint_t *l2);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int is_palindrome(listint_t **head)
{ 
listint_t *slowPtr, *fastPtr, *prevSlowPtr, *firstHalf, *secondHalf, *midPtr;
if (!head || !(*head) || !((*head)->next))
return (1);

    firstHalf = slowPtr = fastPtr = prevSlowPtr = *head;
    secondHalf = midPtr = NULL;

    for (; fastPtr && fastPtr->next; slowPtr = slowPtr->next, fastPtr = fastPtr->next->next) {
        prevSlowPtr = slowPtr;
    }

    if (fastPtr == NULL)
        secondHalf = slowPtr;
    else {
        midPtr = slowPtr;
        secondHalf = slowPtr->next;
    }

    prevSlowPtr->next = NULL;
    reverse_list(&secondHalf);

    if (list_equiv(firstHalf, secondHalf))
        return 1;
    else
        return 0;
}

/**
 * list_equiv - you have to checks if two linked lists contain
 * identical data and are the same length as each other
 * @list1: list one to compare with that of  list two
 * @list2: list two to compare to with that of list one
 *
 * Return: 1 (equivalent) 0 (not equal)
 */
int list_equiv(listint_t *list1, listint_t *list2)
{
	 while (list1 || list2)
    {
        if (!list1 || !list2 || list1->n != list2->n)
            return 0;
        
        list1 = list1->next;
        list2 = list2->next;
    }
    
    return 1;
}

/**
 * reverse_list - it reverses a linked list
 * @head: it double pointer to head of linked list so we can modify it
 *
 * Return: return always void, modifies head itself.
 */
void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *cur;

    cur = *head;
    while (cur)
    {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    *head = prev;
}
