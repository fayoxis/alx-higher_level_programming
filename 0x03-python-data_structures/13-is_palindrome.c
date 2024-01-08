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
