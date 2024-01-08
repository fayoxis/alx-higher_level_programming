#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int listequiv(listint_t *l1, listint_t *l2);

/**
 * ispalindrome - checks if a linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 0 (not palindrome) 1 (is palindrome)
 */
int ispalindrome(listint_t **head)
{
	listint_t *skip_1, *skip_2, *prev_s1, *first_half, *second_half, *mid;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	first_half = skip_1 = skip_2 = prev_s1 = *head;
	second_half = mid = NULL;

	while (skip_1 && skip_2 && skip_2->next)
	{
		prev_s1 = skip_1;
		skip_1 = skip_1->next;
		skip_2 = skip_2->next->next;
	}
	if (skip_2 == NULL) /* Even # of nodes */
		second_half = skip_1;
	else
	{
		mid = skip_1;
		second_half = skip_1->next;
	}
	prev_s1->next = NULL;
	reverse_list(&second_half);

	if (list_equiv(first_half, second_half))
		return (1);
	else
		return (0);
}

/**
 * list_equiv - checks if two linked lists contain identical data and are
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
 * reverse_list - reverses a linked list
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
