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
        return 1;

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
 * list_equiv - checks if two linked lists contain identical data and are
 * the same length as each other
 * @l1: list one to compare to list two
 * @l2: list two to compare to list one
 *
 * Return: 1 (equivalent) 0 (not equal)
 */
int list_equiv(listint_t *l1, listint_t *l2)
{
	while (l1 || l2)
	{
		if (l1->n != l2->n || !l1 || !l2)
			return (0);
		if (l1)
			l1 = l1->next;
		if (l2)
			l2 = l2->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to head of linked list so we can modify it
 *
 * Return: always void, modifies head itself.
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
