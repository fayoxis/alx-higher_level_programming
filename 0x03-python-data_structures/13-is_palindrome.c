#include "lists.h"
#include <stdio.h>

void reverselist(listint_t **head);
int listequiv(listint_t *list1, listint_t *list2);

/**
 * ispalindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int isPalindrome(listint_t **head) {
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
 * listequiv - checks if two linked lists contain identical data and are
 * the same length as each other
 * @list1: list one to compare to list two
 * @list2: list two to compare to list one
 *
 * Return: 1 (equivalent) 0 (not equal)
 */
int listequiv(listint_t *list1, listint_t *list2)
{
	while (list1 || list2)
	{
		if (list1->n != list2->n || !list1 || !list2)
			return (0);
		if (list1)
			list1 = list1->next;
		if (list2)
			list2 = list2->next;
	}
	return (1);
}

/**
 * reverselist - reverses a linked list
 * @head: double pointer to head of linked list so we can modify it
 *
 * Return: always void, modifies head itself.
 */
void reverselist(listint_t **head)
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
